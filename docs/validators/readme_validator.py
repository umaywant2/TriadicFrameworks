import os
import re
import requests
from bs4 import BeautifulSoup

README_PATH = "README.md"
LOG_PATH = "docs/validation/readme_log.md"

def extract_links(content):
    # Match Markdown links: [label](url)
    md_links = re.findall(r',\[.*?\],\((.*?)\)', content)
    # Match HTML hrefs
    html_links = re.findall(r'href="(.*?)"', content)
    # Match image sources
    img_links = re.findall(r'src="(.*?)"', content)
    return md_links + html_links + img_links

def check_link(url):
    if url.startswith("http"):
        try:
            r = requests.head(url, allow_redirects=True, timeout=5)
            return r.status_code == 200
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
