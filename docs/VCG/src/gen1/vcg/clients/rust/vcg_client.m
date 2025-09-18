# vcg_client – Rust helper for Gen1 workloads

## Purpose
Provide a minimal, reusable Rust API for communicating with the VCG orchestrator and Resonant Time Daemon.

---

## Functions

### `await_window(sock_path: &str) -> std::io::Result<()>`
Blocks until a `WINDOW_TICK` message is received for the current dimension.

### `send_route(from_d: &str, to_d: &str, payload: &str) -> std::io::Result<()>`
Sends a payload to another dimension via the VCG orchestrator.

### `recv_route(dimension_id: &str) -> std::io::Result<Option<serde_json::Value>>`
Receives the next routed payload for this dimension, if available.

---

## Implementation

```rust
use std::os::unix::net::UnixDatagram;
use std::path::Path;
use serde_json::{Value, json};
use std::fs;

const BUFFER_SIZE: usize = 65535;
const VCG_ROUTE_SOCK: &str = "/run/vcg/vcg_route.sock";

pub fn await_window(sock_path: &str) -> std::io::Result<()> {
    let sock = UnixDatagram::unbound()?;
    sock.connect(sock_path)?;
    let mut buf = vec![0u8; BUFFER_SIZE];
    loop {
        let size = sock.recv(&mut buf)?;
        let msg: Value = serde_json::from_slice(&buf[..size])?;
        if msg.get("type") == Some(&Value::String("WINDOW_TICK".into())) {
            return Ok(());
        }
    }
}

pub fn send_route(from_d: &str, to_d: &str, payload: &str) -> std::io::Result<()> {
    let sock = UnixDatagram::unbound()?;
    sock.connect(VCG_ROUTE_SOCK)?;
    let msg = json!({
        "type": "VCG_ROUTE",
        "from_d": from_d,
        "to_d": to_d,
        "payload": payload
    });
    let data = serde_json::to_vec(&msg)?;
    sock.send(&data)?;
    Ok(())
}

pub fn recv_route(dimension_id: &str) -> std::io::Result<Option<Value>> {
    let sock_path = format!("/run/vcg/{}.sock", dimension_id.to_lowercase());
    if !Path::new(&sock_path).exists() {
        return Err(std::io::Error::new(std::io::ErrorKind::NotFound, "Socket not found"));
    }
    let sock = UnixDatagram::unbound()?;
    sock.connect(&sock_path)?;
    let mut buf = vec![0u8; BUFFER_SIZE];
    let size = sock.recv(&mut buf)?;
    let msg: Value = serde_json::from_slice(&buf[..size])?;
    if msg.get("type") == Some(&Value::String("VCG_ROUTE".into())) {
        if let Some(payload) = msg.get("payload") {
            let parsed: Value = serde_json::from_str(payload.as_str().unwrap_or(""))?;
            return Ok(Some(parsed));
        }
    }
    Ok(None)
}
```
## Usage Example
```rust
use vcg_client::{await_window, send_route, recv_route};

fn main() -> std::io::Result<()> {
    let dim_id = "D2";
    let sock_path = format!("/run/vcg/{}.sock", dim_id.to_lowercase());

    await_window(&sock_path)?;
    send_route(dim_id, "D4", r#"{"msg": "hello"}"#)?;
    if let Some(msg) = recv_route(dim_id)? {
        println!("Received: {:?}", msg);
    }
    Ok(())
}
```
