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
