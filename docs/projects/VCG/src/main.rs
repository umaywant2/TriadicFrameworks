// src/main.rs (excerpt)
use serde::Deserialize;

#[derive(Debug, Deserialize, Clone)]
struct Dimension {
    id: String,                // "D1".."D9"
    phase_offset_deg: f64,     // 0, 40, 80, ...
    harmonic: u32,             // 1, 2, 3
    qos_weight: f64,           // not used by RTD, passed through
    numa_node: i32,
    cpu_set: String,
    fs_type: String,
    size_gb: u64,
}

#[derive(Debug, Deserialize)]
struct Config { dimensions: Vec<Dimension> }
