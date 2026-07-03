import os
import re
import socket
import ipaddress
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

README_PATH = "README.md"
LOG_PATH = "docs/validation/readme_log.md"
ALLOWED_LINK_HOSTS = {
    host.strip().lower()
    for host in os.getenv(
        "README_LINK_ALLOWED_HOSTS",
        "github.com,raw.githubusercontent.com,pypi.org,python.org,readthedocs.io"
    ).split(",")
    if host.strip()
}

def _is_allowed_host(url):
    try:
        host = (urlparse(url).hostname or "").lower()
        if not host:
            return False
        return any(host == allowed or host.endswith("." + allowed) for allowed in ALLOWED_LINK_HOSTS)
    except:
        return False

def extract_links(content):
    # Match Markdown links: [label](url)
    md_links = re.findall(r',\[.*?\],\((.*?)\)', content)
    # Match HTML hrefs
    html_links = re.findall(r'href="(.*?)"', content)
    # Match image sources
    img_links = re.findall(r'src="(.*?)"', content)
    return md_links + html_links + img_links

def _is_public_http_url(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False
        if not parsed.hostname:
            return False

        host = parsed.hostname
        try:
            host_ip = ipaddress.ip_address(host)
            return not (
                host_ip.is_private
                or host_ip.is_loopback
                or host_ip.is_link_local
                or host_ip.is_reserved
                or host_ip.is_multicast
            )
        except ValueError:
            pass

        addrinfos = socket.getaddrinfo(host, None)
        for info in addrinfos:
            ip_text = info[4][0]
            resolved_ip = ipaddress.ip_address(ip_text)
            if (
                resolved_ip.is_private
                or resolved_ip.is_loopback
                or resolved_ip.is_link_local
                or resolved_ip.is_reserved
                or resolved_ip.is_multicast
            ):
                return False
        return True
    except:
        return False

def check_link(url):
    if url.startswith("http"):
        current_url = url
        max_redirects = 5
        try:
            for _ in range(max_redirects + 1):
                if not _is_public_http_url(current_url):
                    return False
                if not _is_allowed_host(current_url):
                    return False

                r = requests.head(current_url, allow_redirects=False, timeout=5)
                if r.status_code == 200:
                    return True

                if r.status_code in (301, 302, 303, 307, 308):
                    location = r.headers.get("Location")
                    if not location:
                        return False
                    current_url = urljoin(current_url, location)
                    continue

                return False
            return False
        except:
            return False
    else:
        return os.path.exists(url)

def validate_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    links = extract_links(content)
    broken = [link for link in links if not check_link(link)]

    soup = BeautifulSoup(content, "html.parser")
    html_blocks = soup.find_all(["table", "script", "link", "div"])

    return broken, html_blocks

def log_results(broken, html_blocks):
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(f"## README Validation — {os.path.basename(README_PATH)}\n")

        if broken:
            log.write("❌ Broken Links:\n")
            for b in broken:
                log.write(f"- {b}\n")
        else:
            log.write("✅ All links valid.\n")

        log.write(f"\n🔍 HTML Blocks Detected: {len(html_blocks)}\n")
        for block in html_blocks:
            log.write(f"- <{block.name}> block found\n")

        log.write("\n")

if __name__ == "__main__":
    broken_links, html_blocks = validate_readme()
    log_results(broken_links, html_blocks)
