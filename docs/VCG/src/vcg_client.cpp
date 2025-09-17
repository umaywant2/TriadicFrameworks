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
