# vcg_client – C++ helper for Gen1 workloads
## Purpose

Provide a minimal C++ API for communicating with the VCG orchestrator and Resonant Time Daemon using Unix domain datagram sockets. Matches the Python/Rust client semantics.

---

## Public interface
- **await_window(sock_path):** Block until a WINDOW_TICK arrives for this dimension.
- **send_route(from_d, to_d, payload):** Route a payload to another dimension via the orchestrator.
- **recv_route(dimension_id):** Receive next routed payload for this dimension.

---

### Header file
```cpp
// include/vcg_client.hpp
#pragma once
#include <string>
#include <optional>
#include <nlohmann/json.hpp>

namespace vcg {

struct Result {
  bool ok;
  std::string error;
};

Result await_window(const std::string& sock_path);

Result send_route(const std::string& from_d,
                  const std::string& to_d,
                  const std::string& payload,
                  const std::string& route_sock = "/run/vcg/vcg_route.sock");

std::optional<nlohmann::json> recv_route(const std::string& dimension_id);

} // namespace vcg
```

### Implementation
```cpp
// src/vcg_client.cpp
#include "vcg_client.hpp"
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <vector>

namespace vcg {

static int connect_dgram(const std::string& path, std::string& err) {
  int fd = ::socket(AF_UNIX, SOCK_DGRAM, 0);
  if (fd < 0) { err = "socket() failed"; return -1; }
  sockaddr_un addr{};
  addr.sun_family = AF_UNIX;
  std::snprintf(addr.sun_path, sizeof(addr.sun_path), "%s", path.c_str());
  if (::connect(fd, reinterpret_cast<sockaddr*>(&addr), sizeof(addr)) < 0) {
    err = "connect() failed to " + path; ::close(fd); return -1;
  }
  return fd;
}

Result await_window(const std::string& sock_path) {
  std::string err;
  int fd = connect_dgram(sock_path, err);
  if (fd < 0) return {false, err};
  std::vector<char> buf(65535);
  for (;;) {
    ssize_t n = ::recv(fd, buf.data(), buf.size(), 0);
    if (n <= 0) continue;
    try {
      auto msg = nlohmann::json::parse(std::string(buf.data(), n));
      if (msg.contains("type") && msg["type"] == "WINDOW_TICK") {
        ::close(fd);
        return {true, ""};
      }
    } catch (...) {}
  }
}

Result send_route(const std::string& from_d,
                  const std::string& to_d,
                  const std::string& payload,
                  const std::string& route_sock) {
  std::string err;
  int fd = connect_dgram(route_sock, err);
  if (fd < 0) return {false, err};
  nlohmann::json msg = {
    {"type","VCG_ROUTE"},
    {"from_d",from_d},
    {"to_d",to_d},
    {"payload",payload}
  };
  auto data = msg.dump();
  ::send(fd, data.data(), data.size(), 0);
  ::close(fd);
  return {true, ""};
}

std::optional<nlohmann::json> recv_route(const std::string& dimension_id) {
  std::string sock = "/run/vcg/" + std::string{dimension_id};
  for (auto& c : sock) c = std::tolower(c);
  sock += ".sock";
  std::string err;
  int fd = connect_dgram(sock, err);
  if (fd < 0) return std::nullopt;
  std::vector<char> buf(65535);
  ssize_t n = ::recv(fd, buf.data(), buf.size(), 0);
  ::close(fd);
  if (n <= 0) return std::nullopt;
  try {
    auto msg = nlohmann::json::parse(std::string(buf.data(), n));
    if (msg.contains("type") && msg["type"] == "VCG_ROUTE" && msg.contains("payload")) {
      return nlohmann::json::parse(msg["payload"].get<std::string>());
    }
  } catch (...) {}
  return std::nullopt;
}

} // namespace vcg
```

## Build notes
- **Deps:** nlohmann/json (single‑header), glibc, Linux UDS.
- **Compile:** g++ -O2 -std=c++20 -Iinclude src/vcg_client.cpp -o libvcg_client.a (or build as a static lib).
- **Link:** Add -lrt if your distro requires it for CLOCK_MONOTONIC_RAW usage elsewhere.

---
