// src/main.rs
use serde_json::json;
use std::{fs, time::{Duration, Instant}};
use tokio::time::sleep;
use tokio::signal::unix::{signal, SignalKind};
use std::os::unix::net::UnixDatagram;

const RT_SOCK: &str = "/run/vcg/rt.sock";
const STANDALONE: bool = true; // mirror ticks to /run/vcg/dX.sock for early testing

fn deg_to_frac(deg: f64) -> f64 { deg / 360.0 }

fn sock_connect(path: &str) -> std::io::Result<UnixDatagram> {
    let sock = UnixDatagram::unbound()?;
    sock.connect(path)?;
    Ok(sock)
}

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    fs::create_dir_all("/run/vcg")?;
    let mut cfg = load_cfg()?;
    let mut hup = signal(SignalKind::hangup())?;

    // base frequency (Hz) for Gen1 testing; adjust as needed
    let mut base_hz: f64 = 10.0;

    let start = Instant::now();
    let mut seq: u64 = 0;

    loop {
        tokio::select! {
            _ = hup.recv() => {
                cfg = load_cfg()?;
                eprintln!("[RTD] reloaded dimensions.yml");
            }
            _ = tick_once(&cfg, start, seq, base_hz) => {
                seq += 1;
            }
        }
    }
}

fn load_cfg() -> anyhow::Result<Config> {
    let txt = fs::read_to_string("/src/gen1/vcg/config/dimensions.yml")?;
    let cfg: Config = serde_yaml::from_str(&txt)?;
    Ok(cfg)
}

async fn tick_once(cfg: &Config, start: Instant, seq: u64, base_hz: f64) {
    let base_period = Duration::from_secs_f64(1.0 / base_hz);
    let now = Instant::now();
    let next_boundary = start + base_period * (seq as u32 + 1);
    let sleep_dur = next_boundary.saturating_duration_since(now);
    sleep(sleep_dur).await;

    for d in &cfg.dimensions {
        let period = base_period / (d.harmonic as u32);
        let phase = period.mul_f64(deg_to_frac(d.phase_offset_deg));
        let t_start = Instant::now() + phase;
        let t_end = t_start + period;

        let msg = json!({
            "type": "WINDOW_TICK",
            "dimension_id": d.id,
            "seq": seq,
            "t_start_ns": to_ns(t_start, start),
            "t_end_ns": to_ns(t_end, start),
            "phase_deg": d.phase_offset_deg,
            "cadence_hz": (1.0/period.as_secs_f64())
        }).to_string();

        // Publish to RT socket (orchestrator subscribes)
        if let Ok(sock) = sock_connect(RT_SOCK) {
            let _ = sock.send(msg.as_bytes());
        }

        // Standalone: mirror directly to per-dimension socket
        if STANDALONE {
            let dim_sock = format!("/run/vcg/{}.sock", d.id.to_lowercase());
            if let Ok(sock) = sock_connect(&dim_sock) {
                let _ = sock.send(msg.as_bytes());
            }
        }
    }
}

fn to_ns(t: Instant, epoch: Instant) -> u128 {
    let d = t.duration_since(epoch);
    (d.as_secs() as u128) * 1_000_000_000u128 + (d.subsec_nanos() as u128)
}
