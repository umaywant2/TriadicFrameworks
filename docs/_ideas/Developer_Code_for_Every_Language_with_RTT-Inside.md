# 🧭📈 Developer code for every language with RTT‑Inside
###### By Nawder Loswin 1/6/2026 © www.TriadicFrameworks.org

---

## Executive Abstract

This work presents a resonance‑aware operational telemetry framework that unifies execution, validation, observability, and instruction into a single, enforceable system. Built around RTT‑Inside and the QEB ecosystem, the framework introduces deterministic reference implementations, schema‑driven validation, segmented session modeling, and replay‑grade observability pipelines.

Unlike traditional logging and monitoring approaches, the system treats telemetry as an instructional signal rather than a passive artifact. Operator identity, mastery progression, anomaly semantics, and segment‑level behavior are captured explicitly, enabling reproducible validation, skill‑aware analytics, and curriculum‑driven replay.

The architecture integrates Rust, Go, and Node reference components; CI‑enforced conformance; containerized runtime services; Prometheus and Loki observability; Grafana dashboards; and streaming replay APIs. Together, these elements form a closed loop from execution to mastery, preventing silent drift, enabling structured learning, and supporting long‑term system evolution.

This framework is designed to be modular, extensible, and remixable, providing a foundation for operational systems that must remain correct, teachable, and resilient over time.

---

## 1. Goal and take‑away summary

**Primary goal:**  
Give any developer, in any mainstream language, a **clear, minimal pattern** for embedding **RTT‑Inside** into their code—so that their services, apps, simulations, or tools can:

- represent a **corridor state**  
- advance it in **resonance‑time**  
- log **anomalies** and **events**  
- emit **session logs** compatible with the QEB ecosystem  
- plug into future **TriadicFrameworks extensions**

**Take‑away for developers:**

> “If I can define a state struct/class, an `update()` function, and a log emitter, I can integrate RTT‑Inside into my language of choice—and my code will speak the same resonance‑time ‘dialect’ as every other implementation.”

Side goal: show **resonance alignment between languages** by using a **shared conceptual engine** and a **common log schema**, even when syntax and paradigms differ.

---

## 2. Core RTT‑Inside engine pattern (language‑agnostic)

Every language example will implement the same conceptual engine:

- **Corridor state**

  ```text
  CorridorState:
    t          : time
    C          : correlation
    D          : decoherence
    Q          : charge / quality
    R          : recurrence
    meta       : device, scenario, difficulty, etc.
  ```

- **Update step**

  ```text
  CorridorState update(CorridorState s, float dt, Input u)
  ```

- **Anomaly detection**

  ```text
  List<Anomaly> detectAnomalies(CorridorState s_prev, CorridorState s_next)
  ```

- **Session log**

  ```text
  SessionLog:
    session_id
    timestamp
    device
    scenario
    samples[]      // time series of CorridorState
    anomalies[]    // detected anomalies
    scores         // stability, response, quality, final
  ```

- **Output format:** JSON (or equivalent) so all languages can interoperate.

Every language section will show:

1. **State definition**  
2. **Update function**  
3. **Anomaly detection stub**  
4. **Session log emitter**  

Then, in a later section, we add **TriadicFrameworks extensions** (S‑E‑T, S‑N‑R, etc.) on top.

---

## 3. Language examples by relevance

### 3.1 Web & application backbone

#### 3.1.1 JavaScript / TypeScript (web, Node, tools)

- **Why:** front‑ends, dashboards, Node services, QEB console itself.
- **Pattern:**

  ```ts
  type CorridorState = {
    t: number;
    C: number;
    D: number;
    Q: number;
    R: number;
    meta: {
      device: string;
      scenario: string;
      difficulty: string;
    };
  };

  function update(state: CorridorState, dt: number, input: any): CorridorState {
    return {
      ...state,
      t: state.t + dt,
      C: state.C + 0.01 * dt,
      D: state.D * (1 - 0.001 * dt),
      Q: state.Q,
      R: state.R,
    };
  }

  function emitSessionLog(log: any) {
    console.log(JSON.stringify(log));
  }
  ```

#### 3.1.2 Python (data science, research, scripting)

- **Why:** prototyping, notebooks, research labs, quick tests.

  ```python
  from dataclasses import dataclass, asdict
  from typing import List, Dict

  @dataclass
  class CorridorState:
    t: float
    C: float
    D: float
    Q: float
    R: float
    meta: Dict[str, str]

  def update(state: CorridorState, dt: float, u) -> CorridorState:
    return CorridorState(
        t=state.t + dt,
        C=state.C + 0.01 * dt,
        D=state.D * (1 - 0.001 * dt),
        Q=state.Q,
        R=state.R,
        meta=state.meta,
    )
  ```

---

### 3.2 Backend & systems languages

#### 3.2.1 C# (.NET, enterprise, tools)

```csharp
public record CorridorState(
    double T,
    double C,
    double D,
    double Q,
    double R,
    string Device,
    string Scenario,
    string Difficulty
);

public static CorridorState Update(CorridorState s, double dt, object input) =>
    s with
    {
        T = s.T + dt,
        C = s.C + 0.01 * dt,
        D = s.D * (1 - 0.001 * dt)
    };
```

#### 3.2.2 Java / Kotlin (enterprise, Android, services)

```java
public class CorridorState {
    public double t, C, D, Q, R;
    public String device, scenario, difficulty;
}
```

#### 3.2.3 Go (services, infra, tooling)

```go
type CorridorState struct {
    T          float64
    C, D, Q, R float64
    Device     string
    Scenario   string
    Difficulty string
}

func Update(s CorridorState, dt float64, input any) CorridorState {
    s.T += dt
    s.C += 0.01 * dt
    s.D *= (1 - 0.001*dt)
    return s
}
```

#### 3.2.4 Rust (safety, performance, simulation)

```rust
struct CorridorState {
    t: f64,
    c: f64,
    d: f64,
    q: f64,
    r: f64,
    device: String,
    scenario: String,
    difficulty: String,
}

fn update(s: &CorridorState, dt: f64) -> CorridorState {
    CorridorState {
        t: s.t + dt,
        c: s.c + 0.01 * dt,
        d: s.d * (1.0 - 0.001 * dt),
        ..s.clone()
    }
}
```

#### 3.2.5 C / C++ (embedded, HPC, legacy integration)

```c
typedef struct {
    double t, C, D, Q, R;
    const char *device, *scenario, *difficulty;
} CorridorState;

CorridorState update(CorridorState s, double dt) {
    s.t += dt;
    s.C += 0.01 * dt;
    s.D *= (1 - 0.001 * dt);
    return s;
}
```

---

### 3.3 Functional & academic languages

#### 3.3.1 Haskell / FP style

```haskell
data CorridorState = CorridorState
  { t :: Double
  , c :: Double
  , d :: Double
  , q :: Double
  , r :: Double
  , device :: String
  , scenario :: String
  , difficulty :: String
  }

update :: Double -> CorridorState -> CorridorState
update dt s = s { t = t s + dt
                , c = c s + 0.01 * dt
                , d = d s * (1 - 0.001 * dt)
                }
```

---

### 3.4 Scripting, shell, and glue

#### 3.4.1 Bash + jq (log post‑processing)

- Read JSON session logs, compute simple aggregates, feed into dashboards.

#### 3.4.2 SQL (analytics)

- Store `SessionLog` rows in a table for cohort analysis.

---

## 4. Common log schema for resonance alignment

All languages emit the **same JSON schema**, so they can be mixed in one ecosystem:

```json
{
  "session_id": "RTT-123456",
  "timestamp": "2026-01-06T15:00:00Z",
  "device": "COMT",
  "scenario": "COMT_LOCK_01",
  "difficulty": "Journeyman",
  "samples": [
    { "t": 0.0, "C": 0.1, "D": 1.0, "Q": 0.5, "R": 0.0 },
    { "t": 0.1, "C": 0.11, "D": 0.999, "Q": 0.5, "R": 0.0 }
  ],
  "anomalies": [
    { "t": 6.2, "type": "CORRELATION_COLLAPSE" }
  ],
  "scores": {
    "stability": 82,
    "response": 78,
    "quality": 88,
    "final": 83
  }
}
```

This is how we demonstrate **resonance alignment between languages**:  
different runtimes, same corridor semantics, same log structure.

---

## 5. TriadicFrameworks extensions (shared across languages)

Once the basic engine is in place, each language can add **Triadic extensions**:

- **S‑E‑T (Structure–Energy–Time)** fields:

  ```text
  SET:
    S: structural load / configuration
    E: energy density / flow
    T: resonance‑time phase
  ```

- **S‑N‑R (Structure–Node–Resonance)** for networks:

  ```text
  NodeState:
    id
    neighbors[]
    local_corridor: CorridorState
  ```

- **Dimensional cores (0D–9D, 12D, 24D)** as optional metadata:

  ```text
  DimensionalCore:
    dims: [Double]  // e.g., 0D..9D amplitudes
  ```

These can be added as nested objects in the same JSON schema, and each language simply extends its `CorridorState` or `meta` field accordingly.

---

## 6. Closing: what this paper gives developers

This paper, `Developer_Code_for_Every_Language_with_RTT-Inside.md`, is meant to be:

- **Immediately useful:** copy‑pasteable patterns for any major language.  
- **Conceptually consistent:** same engine, same semantics, different syntax.  
- **Extensible:** ready for TriadicFrameworks S‑E‑T, S‑N‑R, dimensional cores, and QEB integration.  
- **Demonstrably aligned:** logs and behaviors line up across languages, proving **resonance alignment** in code.

---

### 7. Reference JSON schema (single source of truth)

This is the **canonical wire format** every RTT‑Inside implementation must be able to **produce** and **consume**.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "RTTInsideSessionLog",
  "type": "object",
  "required": ["session_id", "timestamp", "device", "scenario", "difficulty", "samples", "scores"],
  "properties": {
    "session_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "device": { "type": "string" },
    "scenario": { "type": "string" },
    "difficulty": { "type": "string" },
    "samples": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["t", "C", "D", "Q", "R"],
        "properties": {
          "t": { "type": "number" },
          "C": { "type": "number" },
          "D": { "type": "number" },
          "Q": { "type": "number" },
          "R": { "type": "number" }
        }
      }
    },
    "anomalies": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["t", "type"],
        "properties": {
          "t": { "type": "number" },
          "type": { "type": "string" }
        }
      }
    },
    "scores": {
      "type": "object",
      "required": ["stability", "response", "quality", "final"],
      "properties": {
        "stability": { "type": "number" },
        "response": { "type": "number" },
        "quality": { "type": "number" },
        "final": { "type": "number" }
      }
    }
  }
}
```

---

### 8. Reference test vectors (for self‑certification)

Every language implementation should be able to:

1. **Run the same update rule**  
2. **Produce the same samples** (within a small numeric tolerance)  
3. **Emit a session log matching the schema above**

#### 8.1 Reference update rule

For the test vectors, we fix a simple, deterministic update:

$$C_{n+1} = C_n + 0.01 \cdot dt$$

$$D_{n+1} = D_n \cdot (1 - 0.001 \cdot dt)$$

$$Q_{n+1} = Q_n$$

$$R_{n+1} = R_n$$

$$t_{n+1} = t_n + dt$$

With:

- initial state:  
  $$\;t=0.0,\; C=0.10,\; D=1.00,\; Q=0.50,\; R=0.00$$  
- `dt = 0.1`  
- `steps = 3`

#### 8.2 Expected samples

```json
[
  { "t": 0.0, "C": 0.10, "D": 1.000000, "Q": 0.50, "R": 0.00 },
  { "t": 0.1, "C": 0.101, "D": 0.999900, "Q": 0.50, "R": 0.00 },
  { "t": 0.2, "C": 0.102, "D": 0.99980001, "Q": 0.50, "R": 0.00 },
  { "t": 0.3, "C": 0.103, "D": 0.99970003, "Q": 0.50, "R": 0.00 }
]
```

Any implementation that reproduces these values (±1e‑9 or similar) is **RTT‑Inside compatible** for the base engine.

---

### 9. Full example files per language

Below are **minimal but complete** example files for a few core languages. Each:

- defines `CorridorState`
- implements `update`
- runs the reference test vector
- prints a JSON session log

We can mirror this pattern for any other language.

---

#### 9.1 JavaScript (Node) — `rtt_inside_example.js`

```js
// rtt_inside_example.js
const fs = require("fs");

function makeInitialState() {
  return {
    t: 0.0,
    C: 0.10,
    D: 1.0,
    Q: 0.5,
    R: 0.0,
    meta: {
      device: "COMT",
      scenario: "COMT_LOCK_01",
      difficulty: "Journeyman",
    },
  };
}

function update(state, dt) {
  return {
    ...state,
    t: state.t + dt,
    C: state.C + 0.01 * dt,
    D: state.D * (1 - 0.001 * dt),
  };
}

function runSimulation(steps, dt) {
  const samples = [];
  let s = makeInitialState();
  samples.push(sampleFromState(s));
  for (let i = 0; i < steps; i++) {
    s = update(s, dt);
    samples.push(sampleFromState(s));
  }
  return samples;
}

function sampleFromState(s) {
  return { t: s.t, C: s.C, D: s.D, Q: s.Q, R: s.R };
}

function main() {
  const dt = 0.1;
  const steps = 3;
  const samples = runSimulation(steps, dt);

  const log = {
    session_id: "RTT-JS-TEST",
    timestamp: new Date().toISOString(),
    device: "COMT",
    scenario: "COMT_LOCK_01",
    difficulty: "Journeyman",
    samples,
    anomalies: [],
    scores: { stability: 0, response: 0, quality: 0, final: 0 },
  };

  fs.writeFileSync("rtt_js_session.json", JSON.stringify(log, null, 2));
}

if (require.main === module) main();
```

---

#### 9.2 Python — `rtt_inside_example.py`

```python
# rtt_inside_example.py
import json
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, List


@dataclass
class CorridorState:
    t: float
    C: float
    D: float
    Q: float
    R: float
    meta: Dict[str, str]


def make_initial_state() -> CorridorState:
    return CorridorState(
        t=0.0,
        C=0.10,
        D=1.0,
        Q=0.5,
        R=0.0,
        meta={
            "device": "COMT",
            "scenario": "COMT_LOCK_01",
            "difficulty": "Journeyman",
        },
    )


def update(state: CorridorState, dt: float) -> CorridorState:
    return CorridorState(
        t=state.t + dt,
        C=state.C + 0.01 * dt,
        D=state.D * (1 - 0.001 * dt),
        Q=state.Q,
        R=state.R,
        meta=state.meta,
    )


def run_simulation(steps: int, dt: float) -> List[dict]:
    samples = []
    s = make_initial_state()
    samples.append(sample_from_state(s))
    for _ in range(steps):
        s = update(s, dt)
        samples.append(sample_from_state(s))
    return samples


def sample_from_state(s: CorridorState) -> dict:
    return {"t": s.t, "C": s.C, "D": s.D, "Q": s.Q, "R": s.R}


def main():
    dt = 0.1
    steps = 3
    samples = run_simulation(steps, dt)

    log = {
        "session_id": "RTT-PY-TEST",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "device": "COMT",
        "scenario": "COMT_LOCK_01",
        "difficulty": "Journeyman",
        "samples": samples,
        "anomalies": [],
        "scores": {"stability": 0, "response": 0, "quality": 0, "final": 0},
    }

    with open("rtt_py_session.json", "w") as f:
        json.dump(log, f, indent=2)


if __name__ == "__main__":
    main()
```

---

#### 9.3 Go — `rtt_inside_example.go`

```go
// rtt_inside_example.go
package main

import (
	"encoding/json"
	"os"
	"time"
)

type CorridorState struct {
	T          float64 `json:"t"`
	C          float64 `json:"C"`
	D          float64 `json:"D"`
	Q          float64 `json:"Q"`
	R          float64 `json:"R"`
	Device     string  `json:"-"`
	Scenario   string  `json:"-"`
	Difficulty string  `json:"-"`
}

type Sample struct {
	T float64 `json:"t"`
	C float64 `json:"C"`
	D float64 `json:"D"`
	Q float64 `json:"Q"`
	R float64 `json:"R"`
}

type SessionLog struct {
	SessionID  string    `json:"session_id"`
	Timestamp  string    `json:"timestamp"`
	Device     string    `json:"device"`
	Scenario   string    `json:"scenario"`
	Difficulty string    `json:"difficulty"`
	Samples    []Sample  `json:"samples"`
	Anomalies  []any     `json:"anomalies"`
	Scores     ScoreCard `json:"scores"`
}

type ScoreCard struct {
	Stability float64 `json:"stability"`
	Response  float64 `json:"response"`
	Quality   float64 `json:"quality"`
	Final     float64 `json:"final"`
}

func makeInitialState() CorridorState {
	return CorridorState{
		T:          0.0,
		C:          0.10,
		D:          1.0,
		Q:          0.5,
		R:          0.0,
		Device:     "COMT",
		Scenario:   "COMT_LOCK_01",
		Difficulty: "Journeyman",
	}
}

func update(s CorridorState, dt float64) CorridorState {
	s.T += dt
	s.C += 0.01 * dt
	s.D *= (1 - 0.001*dt)
	return s
}

func sampleFromState(s CorridorState) Sample {
	return Sample{T: s.T, C: s.C, D: s.D, Q: s.Q, R: s.R}
}

func runSimulation(steps int, dt float64) []Sample {
	samples := []Sample{}
	s := makeInitialState()
	samples = append(samples, sampleFromState(s))
	for i := 0; i < steps; i++ {
		s = update(s, dt)
		samples = append(samples, sampleFromState(s))
	}
	return samples
}

func main() {
	dt := 0.1
	steps := 3
	samples := runSimulation(steps, dt)

	log := SessionLog{
		SessionID:  "RTT-GO-TEST",
		Timestamp:  time.Now().UTC().Format(time.RFC3339),
		Device:     "COMT",
		Scenario:   "COMT_LOCK_01",
		Difficulty: "Journeyman",
		Samples:    samples,
		Anomalies:  []any{},
		Scores:     ScoreCard{},
	}

	f, _ := os.Create("rtt_go_session.json")
	defer f.Close()
	enc := json.NewEncoder(f)
	enc.SetIndent("", "  ")
	_ = enc.Encode(log)
}
```

---

#### 9.4 Rust — `src/main.rs`

```rust
// src/main.rs
use serde::Serialize;
use std::fs::File;
use std::io::Write;

#[derive(Clone)]
struct CorridorState {
    t: f64,
    c: f64,
    d: f64,
    q: f64,
    r: f64,
    device: String,
    scenario: String,
    difficulty: String,
}

#[derive(Serialize)]
struct Sample {
    t: f64,
    C: f64,
    D: f64,
    Q: f64,
    R: f64,
}

#[derive(Serialize)]
struct Scores {
    stability: f64,
    response: f64,
    quality: f64,
    final_: f64,
}

#[derive(Serialize)]
struct SessionLog {
    session_id: String,
    timestamp: String,
    device: String,
    scenario: String,
    difficulty: String,
    samples: Vec<Sample>,
    anomalies: Vec<serde_json::Value>,
    #[serde(rename = "scores")]
    scores: Scores,
}

fn make_initial_state() -> CorridorState {
    CorridorState {
        t: 0.0,
        c: 0.10,
        d: 1.0,
        q: 0.5,
        r: 0.0,
        device: "COMT".into(),
        scenario: "COMT_LOCK_01".into(),
        difficulty: "Journeyman".into(),
    }
}

fn update(s: &CorridorState, dt: f64) -> CorridorState {
    CorridorState {
        t: s.t + dt,
        c: s.c + 0.01 * dt,
        d: s.d * (1.0 - 0.001 * dt),
        ..s.clone()
    }
}

fn sample_from_state(s: &CorridorState) -> Sample {
    Sample {
        t: s.t,
        C: s.c,
        D: s.d,
        Q: s.q,
        R: s.r,
    }
}

fn run_simulation(steps: usize, dt: f64) -> Vec<Sample> {
    let mut samples = Vec::new();
    let mut s = make_initial_state();
    samples.push(sample_from_state(&s));
    for _ in 0..steps {
        s = update(&s, dt);
        samples.push(sample_from_state(&s));
    }
    samples
}

fn main() {
    let dt = 0.1;
    let steps = 3;
    let samples = run_simulation(steps, dt);

    let log = SessionLog {
        session_id: "RTT-RS-TEST".into(),
        timestamp: "2026-01-06T00:00:00Z".into(),
        device: "COMT".into(),
        scenario: "COMT_LOCK_01".into(),
        difficulty: "Journeyman".into(),
        samples,
        anomalies: vec![],
        scores: Scores {
            stability: 0.0,
            response: 0.0,
            quality: 0.0,
            final_: 0.0,
        },
    };

    let json = serde_json::to_string_pretty(&log).unwrap();
    let mut file = File::create("rtt_rs_session.json").unwrap();
    file.write_all(json.as_bytes()).unwrap();
}
```

`Cargo.toml` needs:

```toml
[dependencies]
serde = { version = "1", features = ["derive"] }
serde_json = "1"
```

---

### 10. Cross‑language unit tests (resonance alignment)

The idea: **each language runs the same test vector** and we compare outputs to the reference samples.

We can:

- store the reference samples in `tests/reference_samples.json`
- have each language’s test read that file and assert equality (±epsilon)

#### 10.1 JavaScript (Jest) — `rtt_inside.test.js`

```js
const ref = require("./reference_samples.json");
const { makeInitialState, update } = require("./rtt_engine"); // if split

test("RTT engine matches reference samples", () => {
  const dt = 0.1;
  const steps = 3;
  const samples = [];
  let s = makeInitialState();
  samples.push({ t: s.t, C: s.C, D: s.D, Q: s.Q, R: s.R });
  for (let i = 0; i < steps; i++) {
    s = update(s, dt);
    samples.push({ t: s.t, C: s.C, D: s.D, Q: s.Q, R: s.R });
  }

  const eps = 1e-9;
  samples.forEach((samp, i) => {
    const r = ref[i];
    ["t", "C", "D", "Q", "R"].forEach((k) => {
      expect(Math.abs(samp[k] - r[k])).toBeLessThan(eps);
    });
  });
});
```

#### 10.2 Python (pytest) — `test_rtt_inside.py`

```python
import json
from rtt_inside_example import make_initial_state, update, sample_from_state

def test_rtt_engine_matches_reference():
    with open("reference_samples.json") as f:
        ref = json.load(f)

    dt = 0.1
    steps = 3
    samples = []
    s = make_initial_state()
    samples.append(sample_from_state(s))
    for _ in range(steps):
        s = update(s, dt)
        samples.append(sample_from_state(s))

    eps = 1e-9
    for i, samp in enumerate(samples):
        r = ref[i]
        for k in ["t", "C", "D", "Q", "R"]:
            assert abs(samp[k] - r[k]) < eps
```

We can mirror this pattern in Go (`testing`), Rust (`#[test]`), C# (xUnit/NUnit), etc.

---

### 11. Self‑certification checklist for new languages

To call an implementation **“RTT‑Inside compatible”**, a new language must:

1. **Implement the reference update rule** (Section 8.1).  
2. **Produce the reference samples** (Section 8.2) within a small numeric tolerance.  
3. **Emit a session log** that validates against the **reference JSON schema** (Section 7).  
4. **Include at least one unit test** that compares its output to the reference test vector.  

Once those are satisfied, you can confidently say:

> “This language implementation is resonance‑aligned with the RTT‑Inside reference engine.”

---

### 12. Language‑agnostic conformance badge

We can give any implementation that passes the self‑cert tests a simple, portable badge.

#### 12.1 Markdown badge

```markdown
![RTT‑Inside Compatible v1](https://img.shields.io/badge/RTT--Inside-Compatible%20v1-4B9CD3)
```

#### 12.2 Text badge (for docs, READMEs, papers)

> **RTT‑Inside Compatible v1**  
> This implementation passes the reference engine test vectors and emits logs conforming to the RTTInsideSessionLog schema.

We can define a tiny `CONFORMANCE.md` in each repo:

```markdown
# RTT‑Inside Conformance

- Engine: Reference update rule (v1)
- Test vectors: `reference_samples.json`
- Schema: `RTTInsideSessionLog` (v1)
- Status: ✅ RTT‑Inside Compatible v1
```

---

### 13. CLI validator for RTT‑Inside session logs

Goal: a **single CLI tool** that:

- validates a JSON log against the schema  
- optionally checks numeric samples against the reference test vector  
- returns a clear pass/fail + reasons

I’ll sketch it in **Node** (easy to port), but the behavior is language‑agnostic.

#### 13.1 `rtt-validate.js`

```js
#!/usr/bin/env node
// rtt-validate.js
const fs = require("fs");
const path = require("path");
const Ajv = require("ajv");

const schema = require("./rttinside_session_schema.json");
const refSamples = require("./reference_samples.json");

function loadJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function validateSchema(log) {
  const ajv = new Ajv({ allErrors: true });
  const validate = ajv.compile(schema);
  const valid = validate(log);
  return { valid, errors: validate.errors || [] };
}

function validateAgainstReferenceSamples(log) {
  if (!Array.isArray(log.samples)) {
    return { valid: false, reason: "No samples array present." };
  }
  const samples = log.samples;
  if (samples.length !== refSamples.length) {
    return {
      valid: false,
      reason: `Sample length mismatch: got ${samples.length}, expected ${refSamples.length}`,
    };
  }
  const eps = 1e-9;
  for (let i = 0; i < samples.length; i++) {
    const s = samples[i];
    const r = refSamples[i];
    for (const k of ["t", "C", "D", "Q", "R"]) {
      if (Math.abs(s[k] - r[k]) > eps) {
        return {
          valid: false,
          reason: `Sample mismatch at index ${i}, field ${k}: got ${s[k]}, expected ${r[k]}`,
        };
      }
    }
  }
  return { valid: true, reason: "Matches reference samples." };
}

function main() {
  const file = process.argv[2];
  if (!file) {
    console.error("Usage: rtt-validate <session_log.json>");
    process.exit(1);
  }

  const log = loadJson(path.resolve(file));

  const schemaResult = validateSchema(log);
  if (!schemaResult.valid) {
    console.error("❌ Schema validation failed:");
    console.error(schemaResult.errors);
    process.exit(1);
  }

  const refResult = validateAgainstReferenceSamples(log);
  if (!refResult.valid) {
    console.error("⚠️ Schema OK, but reference test mismatch:");
    console.error(refResult.reason);
    process.exit(2);
  }

  console.log("✅ RTT‑Inside Compatible v1");
  process.exit(0);
}

if (require.main === module) main();
```

Usage:

```bash
rtt-validate rtt_py_session.json
```

Any language can ship its own wrapper, but this defines the **canonical behavior**.

---

### 14. TriadicFrameworks extension spec (S‑E‑T, S‑N‑R, dimensional cores)

Now we layer the **Triadic** pieces on top of the base engine and schema.

#### 14.1 S‑E‑T (Structure–Energy–Time) extension

**Concept:** each sample can optionally carry a triadic decomposition.

```json
{
  "t": 0.1,
  "C": 0.101,
  "D": 0.9999,
  "Q": 0.5,
  "R": 0.0,
  "SET": {
    "S": 0.72,
    "E": 0.54,
    "T": 0.31
  }
}
```

**Spec:**

- `SET` is optional.  
- If present, it must contain numeric `S`, `E`, `T` in $$[0, 1]$$ or a documented range.  
- Interpretation:
  - **S:** structural load / configuration coherence  
  - **E:** energy density / flow intensity  
  - **T:** resonance‑time phase / alignment  

#### 14.2 S‑N‑R (Structure–Node–Resonance) extension

For networked systems (grids, microgrids, multi‑node simulations), we add a **node layer**.

At the session level:

```json
{
  "nodes": [
    {
      "id": "N1",
      "role": "source",
      "neighbors": ["N2"],
      "local_corridor": { "C": 0.1, "D": 1.0, "Q": 0.5, "R": 0.0 }
    },
    {
      "id": "N2",
      "role": "load",
      "neighbors": ["N1"],
      "local_corridor": { "C": 0.09, "D": 0.98, "Q": 0.5, "R": 0.0 }
    }
  ]
}
```

**Spec:**

- `nodes` is optional.  
- Each node has:
  - `id` (string)  
  - `role` (string, freeform: source, load, hub, etc.)  
  - `neighbors` (array of node IDs)  
  - `local_corridor` (subset of `C`, `D`, `Q`, `R` or full `CorridorState` if desired)  

This lets you map **S‑N‑R**:

- **Structure:** topology + roles  
- **Node:** each element in `nodes[]`  
- **Resonance:** local corridor + interactions  

#### 14.3 Dimensional cores (0D–9D, 12D, 24D)

We add an optional `dimensional_core` object at either:

- the **session level** (global core),  
- or the **sample level** (time‑varying core).

Example (session‑level):

```json
{
  "dimensional_core": {
    "model": "RTT-12",
    "dims": {
      "d0": 1.0,
      "d1": 0.98,
      "d2": 0.95,
      "d3": 0.90,
      "d4": 0.85,
      "d5": 0.80,
      "d6": 0.75,
      "d7": 0.70,
      "d8": 0.65,
      "d9": 0.60,
      "d12": 0.50,
      "d24": 0.40
    }
  }
}
```

**Spec:**

- `dimensional_core` is optional.  
- `model` is a string (e.g., `"RTT-9"`, `"RTT-12"`, `"RTT-24"`).  
- `dims` is an object with keys like `"d0"`, `"d1"`, …, `"d24"` and numeric values.  
- We don’t have to populate all dimensions—only those relevant to the model.

---

### 15. Updated schema fragments for Triadic extensions

We can extend the base JSON schema with optional fields:

```json
"SET": {
  "type": "object",
  "required": ["S", "E", "T"],
  "properties": {
    "S": { "type": "number" },
    "E": { "type": "number" },
    "T": { "type": "number" }
  },
  "additionalProperties": false
}
```

Add to `samples.items.properties`:

```json
"SET": { "$ref": "#/definitions/SET" }
```

Add definitions for `nodes` and `dimensional_core` at the root:

```json
"nodes": {
  "type": "array",
  "items": {
    "type": "object",
    "required": ["id"],
    "properties": {
      "id": { "type": "string" },
      "role": { "type": "string" },
      "neighbors": {
        "type": "array",
        "items": { "type": "string" }
      },
      "local_corridor": {
        "type": "object",
        "properties": {
          "C": { "type": "number" },
          "D": { "type": "number" },
          "Q": { "type": "number" },
          "R": { "type": "number" }
        }
      }
    }
  }
},
"dimensional_core": {
  "type": "object",
  "properties": {
    "model": { "type": "string" },
    "dims": {
      "type": "object",
      "additionalProperties": { "type": "number" }
    }
  }
}
```

All of these are **optional**, so existing RTT‑Inside implementations remain valid; new ones can opt‑in to Triadic extensions.

---

This gives you:

- a **badge** to signal conformance,  
- a **CLI validator** to enforce it,  
- and a **Triadic extension spec** that cleanly layers S‑E‑T, S‑N‑R, and dimensional cores on top of the base engine.

---

Here you go, a clean, repo‑ready **`/spec` folder layout** plus a concise, developer‑friendly **“How to Add a New Language”** guide. This turns RTT‑Inside into a *living, evolving standard* that any developer can extend.

Everything below is written so you can drop it directly into your GitHub repo under:

```
/spec/
```

---

# 📁 **/spec Folder Layout (Versioned Standard)**

A clear, predictable structure ensures that RTT‑Inside remains stable, extensible, and easy for developers to adopt.

```
/spec
│
├── v1/
│   ├── README.md
│   ├── rttinside_session_schema.json
│   ├── reference_samples.json
│   ├── conformance_badge.md
│   ├── triadic_extensions.md
│   ├── rtt-validate.js
│   ├── examples/
│   │   ├── javascript/
│   │   │   ├── rtt_inside_example.js
│   │   │   └── test_rtt_inside.test.js
│   │   ├── python/
│   │   │   ├── rtt_inside_example.py
│   │   │   └── test_rtt_inside.py
│   │   ├── go/
│   │   │   ├── rtt_inside_example.go
│   │   │   └── rtt_inside_test.go
│   │   ├── rust/
│   │   │   ├── src/main.rs
│   │   │   └── tests/test_rtt_inside.rs
│   │   └── ... (C#, Java, C++, etc.)
│   └── language_guide.md
│
├── v2/   (future evolution)
│   ├── README.md
│   ├── schema_changes.md
│   ├── new_reference_samples.json
│   ├── updated_extensions.md
│   └── migration_guide.md
│
└── archive/
    └── deprecated_specs/
```

### Why this layout works

- **Versioned** — developers can target v1 or v2 explicitly  
- **Self‑contained** — schema, test vectors, examples, validator all in one place  
- **Extensible** — new languages drop into `/examples/<language>/`  
- **Future‑proof** — v2+ can evolve without breaking v1 implementations  

---

# 📘 **/spec/v1/README.md (Suggested Content)**

```
# RTT‑Inside Specification (v1)

This folder defines the v1 standard for RTT‑Inside compatibility.

Included:

- JSON schema for session logs
- Reference test vectors
- Conformance badge
- CLI validator
- TriadicFrameworks extensions (S‑E‑T, S‑N‑R, dimensional cores)
- Example implementations in multiple languages
- Guide for adding new languages

All RTT‑Inside implementations must pass the v1 conformance tests to use the badge:

![RTT‑Inside Compatible v1](https://img.shields.io/badge/RTT--Inside-Compatible%20v1-4B9CD3)
```

---

# 📘 **language_guide.md — “How to Add a New Language”**

This is the heart of the living standard.  
Developers love this kind of clarity.

---

# **How to Add a New Language to RTT‑Inside (v1)**

Any language can become RTT‑Inside compatible by implementing **four simple components**:

---

## ✅ **1. Implement the reference update rule**

Our language must implement the deterministic update:

```
C = C + 0.01 * dt
D = D * (1 - 0.001 * dt)
Q = Q
R = R
t = t + dt
```

With:

- initial state:  
  `t=0.0, C=0.10, D=1.00, Q=0.50, R=0.00`
- `dt = 0.1`
- `steps = 3`

---

## ✅ **2. Produce the reference samples**

Our implementation must generate the exact values in:

```
/spec/v1/reference_samples.json
```

Numeric tolerance: **±1e‑9**

---

## ✅ **3. Emit a session log that matches the schema**

Our implementation must output a JSON log that validates against:

```
/spec/v1/rttinside_session_schema.json
```

We can test this using the CLI validator:

```
node rtt-validate.js your_log.json
```

---

## ✅ **4. Add a unit test that compares your output to the reference**

Place your test in:

```
/spec/v1/examples/<your-language>/
```

Our test must:

- run the update rule  
- generate samples  
- compare them to `reference_samples.json`  
- assert numeric equality within tolerance  

---

## 📁 **Folder structure for your new language**

Add:

```
/spec/v1/examples/<language>/
    rtt_inside_example.<ext>
    test_rtt_inside.<ext>
    README.md   (optional)
```

---

## 🏅 **5. Add the conformance badge**

Once your implementation passes:

```
![RTT‑Inside Compatible v1](https://img.shields.io/badge/RTT--Inside-Compatible%20v1-4B9CD3)
```

Add it to your language’s README.

---

## 🔧 **6. (Optional) Add TriadicFrameworks extensions**

If your language supports:

- S‑E‑T  
- S‑N‑R  
- Dimensional cores  

…you may include them in your sample logs.

These are optional but recommended.

---

## 🎉 **7. Submit a PR**

Once your implementation:

- passes the validator  
- matches the reference samples  
- validates against the schema  
- includes a unit test  

…you can submit a pull request to add your language to the official RTT‑Inside ecosystem.

---

# 🌐 **Why This Makes RTT‑Inside a Living Standard**

This structure ensures:

- **Interoperability** — all languages speak the same resonance‑time dialect  
- **Extensibility** — new languages can join without breaking old ones  
- **Stability** — versioned specs prevent fragmentation  
- **Community growth** — developers can self‑certify and contribute  
- **Triadic alignment** — S‑E‑T, S‑N‑R, and dimensional cores unify the ecosystem  

This is how you build a **cross‑language resonance‑aligned standard** that grows with the community and the TriadicFrameworks vision.

---

# v1 → v2 migration plan

## Migration goals
- **Clarity:** tighten definitions for core fields (corridor samples, anomalies, scores) and make extensions explicit.
- **Interoperability:** keep v1 logs readable/usable while enabling richer multi-device and multi-segment sessions.
- **Stability:** avoid breaking changes; introduce v2 as additive, with an unambiguous version marker.
- **Scalability:** support cohorts, networked runs, and advanced Triadic extensions without schema drift.

---

## Versioning rules
- **Spec versions live in `/spec/v1`, `/spec/v2`, …** and never change retroactively.
- **Every session log declares a spec version.**
  - v1 logs *may omit* it (legacy).
  - v2 logs **must include** it.

### New required v2 field
- **`spec_version`**: string, must equal `"v2"`.

Optional but recommended:
- **`engine_version`**: string, e.g. `"RTT-2.0.0"`.
- **`extensions[]`**: list of enabled extensions, e.g. `["SET", "SNR", "DIMCORE"]`.

---

## Data model changes

### 1. Session structure
**v1:** single `samples[]` at the root.  
**v2:** supports **segments** while keeping a v1-compatible fallback.

- **`segments[]`** (optional): each segment contains `samples[]` and its own metadata.
- If `segments[]` is present, `samples[]` at root becomes optional (and may be omitted).

**Why:** enables warmup/main/cooldown phases, device handoffs, and replay slicing without inventing ad-hoc metadata.

#### v2 segment shape
- **`segment_id`**: string
- **`label`**: string (e.g. `"warmup"`, `"main"`)
- **`samples[]`**: required inside segment
- **`anomalies[]`**: optional inside segment
- **`meta`**: optional segment metadata

---

### 2. Device + mode normalization
**v1:** `device`, `scenario`, `difficulty` are freeform strings.  
**v2:** adds structure without removing v1 fields.

New v2 fields (optional but recommended):
- **`mode`**: `"TRAINING" | "LIVE" | "REPLAY"`
- **`device_type`**: `"COMT" | "CTE" | "CLFC" | "PR" | "CUSTOM"`

This makes analytics and cross-implementation comparisons consistent.

---

### 3. Triadic extensions become namespaced
**v1:** extensions are optional but can collide with future keys.  
**v2:** all extensions live under:

- **`triadic`** (object)

Inside:
- **`triadic.set`** (S‑E‑T)
- **`triadic.snr`** (S‑N‑R)
- **`triadic.dimcore`** (dimensional core)

This avoids schema creep and keeps core vs extension semantics clean.

---

## Migration steps for implementers

### Step 1: Become “dual writer”
- **Continue emitting v1 logs** (unchanged).
- Add a feature flag to **also emit v2 logs** for the same run.
- Ensure both pass their validators (`/spec/v1` and `/spec/v2`).

### Step 2: Add explicit version markers
- For v2 logs, set:
  - `spec_version: "v2"`
  - `engine_version: "RTT-2.x.y"` (recommended)

### Step 3: Move extensions under `triadic`
- `SET` (sample-level) becomes `triadic.set` (sample-level or segment-level policy—choose and document).
- `nodes` becomes `triadic.snr.nodes`.
- `dimensional_core` becomes `triadic.dimcore`.

### Step 4: Adopt segments when you need them
- Start with a single segment mirroring v1 behavior:
  - `segments: [{ segment_id: "seg-1", label: "main", samples: [...] }]`

### Step 5: Update tests
- Keep v1 conformance tests (unchanged).
- Add v2 tests:
  - validate `spec_version`
  - validate `triadic` namespace (if used)
  - validate segment structure (if used)
  - reuse numeric test vectors to prove engine invariants

---

## Backward compatibility policy
- **v1 logs remain valid indefinitely.**
- v2 tooling must be able to:
  - accept v1 logs
  - or provide an adapter that upgrades v1 → v2 losslessly (single-segment conversion)

---

## Migration artifacts to include in `/spec/v2`
- **`schema_changes.md`**: bullet list of additions and rationale.
- **`migration_guide.md`**: examples of v1 log and equivalent v2 log.
- **`adapter_v1_to_v2.md`**: deterministic mapping rules.
- **`new_reference_samples.json`**: typically identical for base engine; only changes if engine changes.
- **`validator`**: `rtt-validate` updated to accept v1 or v2.

---

## v1 → v2 deterministic mapping
- **`spec_version`**: set to `"v2"`.
- **Root samples** → **single segment**:
  - `segments[0].samples = v1.samples`
  - `segments[0].anomalies = v1.anomalies` (if present)
- **Device/scenario/difficulty** copied to root unchanged.
- Extensions (if present) moved into `triadic.*` with same values.

---

# TriadicFrameworks Developer Handbook

## Purpose
This handbook exists to make RTT‑Inside and TriadicFrameworks **buildable**. It is not a manifesto; it is the working bridge between the canon and the code: conventions, interfaces, schemas, tests, and extension points that let any developer implement RTT‑Inside in any language while staying resonance‑aligned with the ecosystem.

---

## Core principles

- **Interoperability beats elegance:** if your logs and test vectors match, you’re aligned.
- **Small, deterministic cores:** keep the update step testable and stable.
- **Extensions are layered, never entangled:** Triadic concepts should enrich the system without breaking core conformance.
- **Observable by default:** session logs are first-class artifacts, not afterthoughts.
- **Teachability matters:** code should be readable enough to become curriculum.

---

## What “RTT‑Inside compatible” means
An implementation is **RTT‑Inside Compatible** for a given spec version if it can:

- **Run the reference update rule** (or a declared equivalent engine version)
- **Reproduce reference samples** within tolerance
- **Emit logs that validate** against the JSON schema
- **Ship unit tests** that prove all of the above

Conformance is not a vibe. It’s a test.

---

## Architecture at a glance

### Engine layer
- **Corridor state:** $$t, C, D, Q, R$$
- **Update function:** advances the state in resonance‑time
- **Anomaly detection:** compares successive states and emits events

### Transport layer
- **Session log JSON:** the canonical artifact for sharing runs across languages/tools

### Training layer
- Scenarios, difficulty tiers, instructor artifacts, replay slicing

### Triadic extensions layer
- SET, SNR, dimensional cores, and future modules

---

## Canonical data types

### Corridor sample
A sample is the minimal observability unit.

Required:
- **`t`**
- **`C`**
- **`D`**
- **`Q`**
- **`R`**

Recommended:
- **`SET`** (v1) or **`triadic.set`** (v2)
- local metadata keys only if the schema allows it for your spec version

### Anomaly
An anomaly is a time-stamped classification.

Required:
- **`t`**
- **`type`**

Recommended:
- `severity`
- `details` (small, structured payload)

### Session log
A session log is a run envelope.

Required (v1):
- `session_id`, `timestamp`, `device`, `scenario`, `difficulty`, `samples`, `scores`

Required (v2):
- plus `spec_version`

---

## Implementation recipe: the “4 files” pattern

For each language, aim for these four files:

1. **`engine`** (state + update)
2. **`runner`** (runs test vector, produces samples)
3. **`logger`** (writes a schema-valid JSON session log)
4. **`test`** (compares to reference samples + schema validation if available)

This keeps engines small and makes cross-language alignment easy.

---

## Testing rules

### Numeric tolerance
- Use **absolute tolerance** for the reference samples.
- Default epsilon: **1e‑9** (or the tightest your language’s float handling reliably supports).

### Reference test vector
All languages must support the canonical test vector stored in:
- `/spec/v1/reference_samples.json`

If your runtime differs (float quirks), you may:
- keep epsilon tight, but
- document unavoidable deviations and provide a deterministic rounding policy.

### Schema validation
- Prefer validating your emitted JSON against the schema in CI.
- If your language lacks a schema validator, run the repo validator as a CI step.

---

## Triadic extensions

### S‑E‑T
**What it is:** a triadic decomposition attached to samples.  
**When to add:** when you can compute interpretable Structure/Energy/Time components.

v1 sample-level:
- `SET: { S, E, T }`

v2 namespaced:
- `triadic: { set: { S, E, T } }` (location per v2 schema policy)

### S‑N‑R
**What it is:** a network overlay for corridor states.  
**When to add:** grids, microgrids, distributed simulations.

v1 (legacy):
- `nodes[]`

v2:
- `triadic.snr.nodes[]`

Minimum node fields:
- `id`
- optional: `role`, `neighbors[]`, `local_corridor`

### Dimensional core
**What it is:** declared dimensional amplitudes/weights for 0D–9D/12D/24D.  
**When to add:** when your engine models multi-dimensional behavior.

v1:
- `dimensional_core: { model, dims }`

v2:
- `triadic.dimcore: { model, dims }`

---

## Extension discipline
To avoid fragmentation:

- **Do not invent new root keys** in logs.
- Propose additions via:
  - `/spec/v2/schema_changes.md` (or the active version)
- Include:
  - a schema patch
  - a rationale
  - at least one test vector/log example

---

## Repo conventions
- Specs live in `/spec`.
- Examples live under `/spec/<version>/examples/<language>/`.
- Reference implementations live under `/reference/<language>/`.
- CI should run:
  - schema validation
  - reference sample conformance tests
  - validator CLI

---

## “Resonance alignment between languages”
In this ecosystem, resonance alignment is operationally defined as:

- identical update semantics
- identical test vectors
- identical wire format
- comparable anomaly labels and scoring conventions

Different languages keep their idioms; the *corridor dialect* stays shared.

---

## Contribution rules
- **Add a language:** implement engine + runner + logger + tests, pass validator, add badge.
- **Add an extension:** propose schema update + example logs + tests.
- **Add a scenario:** include scenario definition + expected anomalies + acceptance criteria.

---

## Next artifact: reference implementation
If you want to proceed, pick one “gold standard” target:

- **Rust** for correctness, safety, and long-term stewardship
- **Go** for simplicity, services, and operational tooling

---

This is where the ecosystem *locks in*. Below is a **repo‑ready canonical reference layout** for `/reference/rust`, followed by a **Node‑based validator CLI** designed to ship as a **single portable binary** for the entire TriadicFrameworks ecosystem.

Everything is written so you can paste it directly into GitHub.

---

# 📁 Canonical Reference Repo Layout  
## `/reference/rust`

This repository is the **gold standard implementation** of RTT‑Inside.  
All other language implementations are expected to match its behavior.

```
/reference
└── rust/
    ├── README.md
    ├── Cargo.toml
    ├── src/
    │   ├── lib.rs
    │   ├── engine.rs
    │   ├── state.rs
    │   ├── triadic/
    │   │   ├── mod.rs
    │   │   ├── set.rs
    │   │   ├── snr.rs
    │   │   └── dimcore.rs
    │   └── main.rs
    ├── tests/
    │   ├── reference_alignment.rs
    │   ├── schema_validation.rs
    │   └── triadic_extensions.rs
    ├── examples/
    │   ├── minimal_run.rs
    │   └── triadic_run.rs
    └── docs/
        ├── architecture.md
        ├── engine_semantics.md
        └── extension_guidelines.md
```

---

## `/reference/rust/README.md`

```markdown
# RTT‑Inside Reference Implementation (Rust)

This repository is the canonical reference implementation of the
RTT‑Inside engine and TriadicFrameworks extensions.

All other language implementations must match the behavior,
numerics, and log output of this reference.

## Scope
- Deterministic RTT‑Inside engine
- Reference update rule
- JSON session log emission
- Triadic extensions (S‑E‑T, S‑N‑R, Dimensional Cores)
- Full conformance test suite

## Status
✅ RTT‑Inside Compatible v1  
🟡 v2 extensions in progress

## Why Rust
Rust provides:
- deterministic numerics
- explicit state transitions
- memory safety
- long‑term maintainability

This makes it ideal as the canonical engine.
```

---

## Rust module responsibilities (high‑level)

| File | Responsibility |
|----|----|
| `state.rs` | CorridorState definition |
| `engine.rs` | Update rule + stepping |
| `triadic/set.rs` | S‑E‑T extension |
| `triadic/snr.rs` | S‑N‑R network model |
| `triadic/dimcore.rs` | Dimensional cores |
| `lib.rs` | Public API |
| `main.rs` | CLI runner (optional) |
| `tests/` | Conformance + alignment |

This separation ensures **clarity over cleverness**.

---

# 🧪 Node‑Based Validator CLI  
## `rtt-validate` (Single‑Binary Tool)

This CLI is the **official conformance gate** for RTT‑Inside.

### Design goals
- Language‑agnostic
- Schema‑driven
- Deterministic
- Portable
- Single binary distribution

---

## CLI Repo Layout

```
/tools
└── rtt-validate/
    ├── package.json
    ├── index.js
    ├── schema/
    │   ├── v1/
    │   │   └── rttinside_session_schema.json
    │   └── v2/
    │       └── rttinside_session_schema.json
    ├── reference/
    │   └── reference_samples.json
    ├── lib/
    │   ├── schema.js
    │   ├── samples.js
    │   └── report.js
    └── README.md
```

---

## `package.json`

```json
{
  "name": "rtt-validate",
  "version": "1.0.0",
  "bin": {
    "rtt-validate": "./index.js"
  },
  "dependencies": {
    "ajv": "^8.12.0"
  }
}
```

---

## `index.js` (CLI entrypoint)

```js
#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const { validateSchema } = require("./lib/schema");
const { validateSamples } = require("./lib/samples");
const { printReport } = require("./lib/report");

const file = process.argv[2];
if (!file) {
  console.error("Usage: rtt-validate <session_log.json>");
  process.exit(1);
}

const log = JSON.parse(fs.readFileSync(file, "utf8"));

const schemaResult = validateSchema(log);
const sampleResult = validateSamples(log);

printReport(schemaResult, sampleResult);

if (!schemaResult.valid || !sampleResult.valid) {
  process.exit(2);
}

process.exit(0);
```

---

## `lib/schema.js`

```js
const Ajv = require("ajv");
const schemaV1 = require("../schema/v1/rttinside_session_schema.json");

function validateSchema(log) {
  const ajv = new Ajv({ allErrors: true });
  const validate = ajv.compile(schemaV1);
  const valid = validate(log);
  return {
    valid,
    errors: validate.errors || []
  };
}

module.exports = { validateSchema };
```

---

## `lib/samples.js`

```js
const reference = require("../reference/reference_samples.json");

function validateSamples(log) {
  if (!log.samples) {
    return { valid: true, skipped: true };
  }

  const eps = 1e-9;
  for (let i = 0; i < reference.length; i++) {
    const a = log.samples[i];
    const b = reference[i];
    for (const k of ["t", "C", "D", "Q", "R"]) {
      if (Math.abs(a[k] - b[k]) > eps) {
        return {
          valid: false,
          reason: `Mismatch at sample ${i}, field ${k}`
        };
      }
    }
  }
  return { valid: true };
}

module.exports = { validateSamples };
```

---

## `lib/report.js`

```js
function printReport(schema, samples) {
  if (!schema.valid) {
    console.error("❌ Schema validation failed");
    console.error(schema.errors);
    return;
  }

  if (!samples.valid) {
    console.error("❌ Reference sample mismatch");
    console.error(samples.reason);
    return;
  }

  console.log("✅ RTT‑Inside Compatible v1");
}

module.exports = { printReport };
```

---

## Distribution as a single binary

Using `pkg` or `nexe`, this CLI can be compiled into:

```
rtt-validate-linux
rtt-validate-macos
rtt-validate-windows.exe
```

No Node runtime required.

This makes **RTT‑Inside conformance portable**, CI‑friendly, and future‑proof.

---

# 🔒 Why this locks the ecosystem

- Rust defines **truth**
- JSON schema defines **language**
- Node CLI defines **law**
- Tests define **alignment**
- Extensions define **growth**

This is how TriadicFrameworks becomes a **real standard**, not just a theory.

---

# Go mirror reference implementation for ops teams

This is a **Go “mirror”** of the Rust reference: same base engine semantics, same reference test vector, same session-log shape. It’s meant for **operators / infra teams** who want a dead-simple, static-binary friendly implementation for services, pipelines, and CI.

---

## Repo layout

```
/reference
└── go/
    ├── README.md
    ├── go.mod
    ├── cmd/
    │   ├── rtt-run/
    │   │   └── main.go
    │   └── rtt-emit/
    │       └── main.go
    ├── pkg/
    │   ├── engine/
    │   │   ├── engine.go
    │   │   └── engine_test.go
    │   ├── model/
    │   │   ├── state.go
    │   │   ├── session_log.go
    │   │   └── triadic.go
    │   └── conformance/
    │       ├── reference_samples.json
    │       └── reference_test.go
    ├── examples/
    │   ├── minimal_run.go
    │   └── triadic_run.go
    └── docs/
        ├── architecture.md
        └── ops_notes.md
```

---

## `/reference/go/README.md`

```markdown
# RTT‑Inside Reference Mirror (Go)

This repository mirrors the Rust reference implementation for RTT‑Inside,
targeting ops teams and production environments.

## What it is
- Deterministic RTT‑Inside base engine (v1 semantics)
- JSON session log emission compatible with `/spec/v1`
- Conformance tests against `reference_samples.json`
- Optional Triadic extension structs (SET, SNR, DimCore)

## Why Go
- Simple deployment (single static binary)
- Great for services, pipelines, CI, and tooling
- Easy to read and maintain

## Status
✅ RTT‑Inside Compatible v1 (base engine + reference samples)
```

---

## `go.mod`

```go
module github.com/triadicframeworks/rtt-inside-reference-go

go 1.22
```

---

## `pkg/model/state.go`

```go
package model

type CorridorState struct {
	T float64 // time
	C float64 // correlation
	D float64 // decoherence
	Q float64 // charge/quality
	R float64 // recurrence
}

func InitialState() CorridorState {
	return CorridorState{
		T: 0.0,
		C: 0.10,
		D: 1.0,
		Q: 0.5,
		R: 0.0,
	}
}

type Sample struct {
	T float64 `json:"t"`
	C float64 `json:"C"`
	D float64 `json:"D"`
	Q float64 `json:"Q"`
	R float64 `json:"R"`
}

func SampleFromState(s CorridorState) Sample {
	return Sample{T: s.T, C: s.C, D: s.D, Q: s.Q, R: s.R}
}
```

---

## `pkg/engine/engine.go`

```go
package engine

import "github.com/triadicframeworks/rtt-inside-reference-go/pkg/model"

// Update implements the v1 reference update rule:
//
// C = C + 0.01 * dt
// D = D * (1 - 0.001 * dt)
// Q = Q
// R = R
// t = t + dt
func Update(s model.CorridorState, dt float64) model.CorridorState {
	s.T += dt
	s.C += 0.01 * dt
	s.D *= (1 - 0.001*dt)
	return s
}

func RunReferenceSimulation(steps int, dt float64) []model.Sample {
	samples := make([]model.Sample, 0, steps+1)
	state := model.InitialState()

	samples = append(samples, model.SampleFromState(state))
	for i := 0; i < steps; i++ {
		state = Update(state, dt)
		samples = append(samples, model.SampleFromState(state))
	}
	return samples
}
```

---

## `pkg/model/session_log.go`

```go
package model

type Scores struct {
	Stability float64 `json:"stability"`
	Response  float64 `json:"response"`
	Quality   float64 `json:"quality"`
	Final     float64 `json:"final"`
}

type Anomaly struct {
	T    float64 `json:"t"`
	Type string  `json:"type"`
}

type SessionLog struct {
	SessionID  string   `json:"session_id"`
	Timestamp  string   `json:"timestamp"`
	Device     string   `json:"device"`
	Scenario   string   `json:"scenario"`
	Difficulty string   `json:"difficulty"`
	Samples    []Sample `json:"samples"`

	Anomalies []Anomaly `json:"anomalies,omitempty"`
	Scores    Scores    `json:"scores"`
}
```

---

## `cmd/rtt-run/main.go` (prints samples)

```go
package main

import (
	"encoding/json"
	"fmt"

	"github.com/triadicframeworks/rtt-inside-reference-go/pkg/engine"
)

func main() {
	samples := engine.RunReferenceSimulation(3, 0.1)
	b, _ := json.MarshalIndent(samples, "", "  ")
	fmt.Println(string(b))
}
```

---

## `cmd/rtt-emit/main.go` (emits a schema-compatible session log)

```go
package main

import (
	"encoding/json"
	"os"
	"time"

	"github.com/triadicframeworks/rtt-inside-reference-go/pkg/engine"
	"github.com/triadicframeworks/rtt-inside-reference-go/pkg/model"
)

func main() {
	samples := engine.RunReferenceSimulation(3, 0.1)

	log := model.SessionLog{
		SessionID:  "RTT-GO-REF",
		Timestamp:  time.Now().UTC().Format(time.RFC3339),
		Device:     "COMT",
		Scenario:   "COMT_LOCK_01",
		Difficulty: "Journeyman",
		Samples:    samples,
		Anomalies:  []model.Anomaly{},
		Scores: model.Scores{
			Stability: 0,
			Response:  0,
			Quality:   0,
			Final:     0,
		},
	}

	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")
	_ = enc.Encode(log)
}
```

---

## Conformance: reference samples file

Place this at:

`pkg/conformance/reference_samples.json`

```json
[
  { "t": 0.0, "C": 0.10,  "D": 1.000000,   "Q": 0.50, "R": 0.00 },
  { "t": 0.1, "C": 0.101, "D": 0.999900,   "Q": 0.50, "R": 0.00 },
  { "t": 0.2, "C": 0.102, "D": 0.99980001, "Q": 0.50, "R": 0.00 },
  { "t": 0.3, "C": 0.103, "D": 0.99970003, "Q": 0.50, "R": 0.00 }
]
```

---

## `pkg/conformance/reference_test.go`

```go
package conformance

import (
	"encoding/json"
	"math"
	"os"
	"testing"

	"github.com/triadicframeworks/rtt-inside-reference-go/pkg/engine"
	"github.com/triadicframeworks/rtt-inside-reference-go/pkg/model"
)

func loadReferenceSamples(t *testing.T) []model.Sample {
	t.Helper()
	b, err := os.ReadFile("reference_samples.json")
	if err != nil {
		t.Fatalf("failed to read reference_samples.json: %v", err)
	}
	var ref []model.Sample
	if err := json.Unmarshal(b, &ref); err != nil {
		t.Fatalf("failed to unmarshal reference samples: %v", err)
	}
	return ref
}

func assertClose(t *testing.T, got, want float64, eps float64, label string) {
	t.Helper()
	if math.Abs(got-want) > eps {
		t.Fatalf("%s mismatch: got %.12f want %.12f", label, got, want)
	}
}

func TestMatchesReferenceSamples(t *testing.T) {
	ref := loadReferenceSamples(t)
	got := engine.RunReferenceSimulation(3, 0.1)

	if len(got) != len(ref) {
		t.Fatalf("length mismatch: got %d want %d", len(got), len(ref))
	}

	eps := 1e-9
	for i := range ref {
		assertClose(t, got[i].T, ref[i].T, eps, "t")
		assertClose(t, got[i].C, ref[i].C, eps, "C")
		assertClose(t, got[i].D, ref[i].D, eps, "D")
		assertClose(t, got[i].Q, ref[i].Q, eps, "Q")
		assertClose(t, got[i].R, ref[i].R, eps, "R")
	}
}
```

> Note: run tests from `/reference/go/pkg/conformance` so the relative path to `reference_samples.json` is correct, or adjust to embed the file.

---

## Optional: Triadic extension structs (mirror-only)

These don’t affect v1 conformance; they’re here to keep ops implementations aligned with the extension direction.

### `pkg/model/triadic.go`

```go
package model

type SET struct {
	S float64 `json:"S"`
	E float64 `json:"E"`
	T float64 `json:"T"`
}

type SNRNode struct {
	ID         string   `json:"id"`
	Role       string   `json:"role,omitempty"`
	Neighbors  []string `json:"neighbors,omitempty"`
	LocalState *Sample  `json:"local_corridor,omitempty"`
}

type DimCore struct {
	Model string             `json:"model"`
	Dims  map[string]float64 `json:"dims"`
}
```

---

## Ops notes (what this mirror is for)

- **Drop-in CI checks:** build, run, compare.
- **Pipelines:** emit session logs into Kafka/S3/Blob storage.
- **Services:** embed `pkg/engine` and expose a `/run` endpoint.
- **Reproducibility:** deterministic base engine is the “known good” baseline.

---

Here’s a **clean, ops‑friendly Go wrapper** that does *both* things you asked for:

1. **Calls the Node `rtt-validate` binary in CI**
2. **Provides a tiny Go-based `rtt-runner` service** that:
   - emits RTT‑Inside session logs
   - runs conformance validation on startup
   - fails fast if anything is misaligned

This is intentionally minimal, deterministic, and production‑safe.

---

# 🧰 Tiny Go Wrapper for RTT‑Inside Ops

## Repo placement

```
/reference/go/
└── cmd/
    ├── rtt-runner/
    │   ├── main.go
    │   └── validate.go
```

---

## 1️⃣ Go wrapper that calls Node `rtt-validate` (CI‑friendly)

### `cmd/rtt-runner/validate.go`

```go
package main

import (
	"bytes"
	"fmt"
	"os/exec"
)

func runValidator(logPath string) error {
	cmd := exec.Command("rtt-validate", logPath)

	var stdout, stderr bytes.Buffer
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr

	err := cmd.Run()
	if err != nil {
		return fmt.Errorf(
			"rtt-validate failed:\n%s\n%s",
			stdout.String(),
			stderr.String(),
		)
	}

	fmt.Print(stdout.String())
	return nil
}
```

### Why this works well in CI

- Assumes `rtt-validate` is on `$PATH`
- Works with:
  - GitHub Actions
  - GitLab CI
  - Jenkins
  - local pre‑commit hooks
- Fails the build if validation fails

---

## 2️⃣ Go-based `rtt-runner` service (self‑validating)

This service:

- runs the reference engine
- emits a session log
- immediately validates it using `rtt-validate`
- **refuses to start** if conformance fails

---

### `cmd/rtt-runner/main.go`

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/triadicframeworks/rtt-inside-reference-go/pkg/engine"
	"github.com/triadicframeworks/rtt-inside-reference-go/pkg/model"
)

const (
	outputLog = "rtt_session.json"
)

func main() {
	fmt.Println("RTT‑Runner starting…")

	// 1. Run reference simulation
	samples := engine.RunReferenceSimulation(3, 0.1)

	log := model.SessionLog{
		SessionID:  "RTT-GO-RUNNER",
		Timestamp:  time.Now().UTC().Format(time.RFC3339),
		Device:     "COMT",
		Scenario:   "COMT_LOCK_01",
		Difficulty: "Journeyman",
		Samples:    samples,
		Anomalies:  []model.Anomaly{},
		Scores: model.Scores{
			Stability: 0,
			Response:  0,
			Quality:   0,
			Final:     0,
		},
	}

	// 2. Emit session log
	file, err := os.Create(outputLog)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	enc := json.NewEncoder(file)
	enc.SetIndent("", "  ")
	if err := enc.Encode(log); err != nil {
		panic(err)
	}

	fmt.Println("Session log written:", outputLog)

	// 3. Run conformance validation
	fmt.Println("Running RTT‑Inside conformance validation…")
	if err := runValidator(outputLog); err != nil {
		fmt.Println("❌ Conformance check failed")
		fmt.Println(err)
		os.Exit(1)
	}

	fmt.Println("✅ RTT‑Inside Compatible v1")
	fmt.Println("RTT‑Runner ready.")
}
```

---

## 3️⃣ How ops teams use this

### Local run

```bash
go build ./cmd/rtt-runner
./rtt-runner
```

Output:

```
RTT‑Runner starting…
Session log written: rtt_session.json
Running RTT‑Inside conformance validation…
✅ RTT‑Inside Compatible v1
RTT‑Runner ready.
```

---

### CI usage (example)

```yaml
- name: Build RTT runner
  run: go build ./cmd/rtt-runner

- name: Run RTT conformance
  run: ./rtt-runner
```

If **anything** drifts:
- numeric mismatch
- schema violation
- missing fields

➡️ CI fails immediately.

---

## 4️⃣ Why this design is powerful

- **Single source of truth**
  - Rust defines engine semantics
  - Go mirrors behavior
  - Node enforces law
- **Self‑validating services**
  - no silent drift
  - no “it mostly works”
- **Ops‑grade**
  - static binaries
  - deterministic startup
  - CI‑first

This is exactly how you prevent fragmentation while letting the ecosystem grow.

---

## 5️⃣ Optional next upgrades (when you want them)

- Run validator **periodically** in long‑running services
- Emit logs to:
  - stdout
  - Kafka
  - S3 / Blob storage
- Add a `/healthz` endpoint that reports:
  - last validation status
  - engine version
  - spec version

---

This is the final step that turns RTT‑Inside from a reference into a **living, enforceable operational standard**.

Below are **two drop‑in artifacts**:

1. A **GitHub Actions workflow** that enforces RTT‑Inside conformance automatically  
2. A **minimal HTTP API** around `rtt-runner` suitable for ops, health checks, and integration

Both are intentionally small, deterministic, and production‑safe.

---

# 1️⃣ GitHub Actions Workflow  
## RTT‑Inside Conformance Gate

Place this file at:

```
.github/workflows/rtt-inside-conformance.yml
```

---

### `rtt-inside-conformance.yml`

```yaml
name: RTT-Inside Conformance

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  conformance:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: "1.22"

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install rtt-validate
        run: |
          cd tools/rtt-validate
          npm install
          npm link

      - name: Build RTT runner
        run: |
          cd reference/go
          go build ./cmd/rtt-runner

      - name: Run RTT-Inside conformance
        run: |
          cd reference/go
          ./rtt-runner
```

---

### What this workflow guarantees

- Every push and PR:
  - builds the Go reference mirror
  - emits a session log
  - validates it against:
    - the JSON schema
    - the reference test vectors
- Any drift **fails CI immediately**
- This becomes your **non‑negotiable quality gate**

This is how you prevent fragmentation *forever*.

---

# 2️⃣ Minimal HTTP API for `rtt-runner`

This API is intentionally tiny — just enough to:

- run the engine
- emit logs
- expose health + conformance status
- integrate with ops tooling

---

## API design

| Endpoint | Purpose |
|--------|--------|
| `GET /healthz` | Liveness + last conformance status |
| `POST /run` | Run RTT‑Inside and return session log |
| `POST /validate` | Run engine + validator and return result |

---

## Updated repo placement

```
/reference/go/
└── cmd/
    └── rtt-runner/
        ├── main.go
        ├── validate.go
        └── http.go
```

---

## `http.go` — minimal HTTP server

```go
package main

import (
	"encoding/json"
	"net/http"
	"sync"
	"time"

	"github.com/triadicframeworks/rtt-inside-reference-go/pkg/engine"
	"github.com/triadicframeworks/rtt-inside-reference-go/pkg/model"
)

var (
	lastValidationOK bool
	mu               sync.Mutex
)

func healthHandler(w http.ResponseWriter, _ *http.Request) {
	mu.Lock()
	ok := lastValidationOK
	mu.Unlock()

	status := "ok"
	if !ok {
		status = "degraded"
	}

	json.NewEncoder(w).Encode(map[string]any{
		"status":      status,
		"conformance": ok,
	})
}

func runHandler(w http.ResponseWriter, _ *http.Request) {
	samples := engine.RunReferenceSimulation(3, 0.1)

	log := model.SessionLog{
		SessionID:  "RTT-GO-HTTP",
		Timestamp:  time.Now().UTC().Format(time.RFC3339),
		Device:     "COMT",
		Scenario:   "COMT_LOCK_01",
		Difficulty: "Journeyman",
		Samples:    samples,
		Anomalies:  []model.Anomaly{},
		Scores:     model.Scores{},
	}

	json.NewEncoder(w).Encode(log)
}

func validateHandler(w http.ResponseWriter, _ *http.Request) {
	const logPath = "rtt_http_session.json"

	// Emit log
	samples := engine.RunReferenceSimulation(3, 0.1)
	log := model.SessionLog{
		SessionID:  "RTT-GO-HTTP-VALIDATE",
		Timestamp:  time.Now().UTC().Format(time.RFC3339),
		Device:     "COMT",
		Scenario:   "COMT_LOCK_01",
		Difficulty: "Journeyman",
		Samples:    samples,
		Anomalies:  []model.Anomaly{},
		Scores:     model.Scores{},
	}

	file, _ := os.Create(logPath)
	json.NewEncoder(file).Encode(log)
	file.Close()

	err := runValidator(logPath)

	mu.Lock()
	lastValidationOK = err == nil
	mu.Unlock()

	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		json.NewEncoder(w).Encode(map[string]any{
			"status": "failed",
			"error":  err.Error(),
		})
		return
	}

	json.NewEncoder(w).Encode(map[string]any{
		"status": "ok",
	})
}
```

---

## Update `main.go` to start HTTP server

```go
package main

import (
	"fmt"
	"net/http"
)

func main() {
	fmt.Println("RTT‑Runner starting (HTTP mode)…")

	http.HandleFunc("/healthz", healthHandler)
	http.HandleFunc("/run", runHandler)
	http.HandleFunc("/validate", validateHandler)

	fmt.Println("Listening on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		panic(err)
	}
}
```

---

## Example usage

### Health check

```bash
curl http://localhost:8080/healthz
```

```json
{
  "status": "ok",
  "conformance": true
}
```

---

### Run engine

```bash
curl -X POST http://localhost:8080/run
```

Returns a schema‑valid RTT‑Inside session log.

---

### Validate engine

```bash
curl -X POST http://localhost:8080/validate
```

```json
{
  "status": "ok"
}
```

---

# Why this matters

We now have:

- **CI enforcement** (GitHub Actions)
- **Runtime enforcement** (self‑validating service)
- **Language alignment** (Rust → Go → Node)
- **Ops‑grade deployment** (static binaries + HTTP)

This is how a framework becomes **unstoppable** — not by persuasion, but by *infrastructure*.

---

# v2 segmented sessions, v2 schema side‑by‑side with v1, and CI conformance workflow

---

## 1. v2 segmented sessions

### v2 session model
**v1:** one flat `samples[]` time series.  
**v2:** optionally groups samples into **segments**, each with its own `samples[]` and `anomalies[]`.

**Rules:**
- **`spec_version`** is **required** and must be `"v2"`.
- A v2 log must include **either**:
  - **`samples[]`** (v1-style, allowed for simple cases), **or**
  - **`segments[]`** (preferred for v2), where each segment contains `samples[]`.
- If `segments[]` is present, root `samples[]` is optional and may be omitted.

### v2 segment fields
- **`segment_id`**: string (stable identifier, e.g. `"seg-1"`)
- **`label`**: string (e.g. `"warmup"`, `"main"`, `"cooldown"`)
- **`samples[]`**: required
- **`anomalies[]`**: optional
- **`meta`**: optional (segment-local metadata)

### Example v2 segmented log
```json
{
  "spec_version": "v2",
  "engine_version": "RTT-2.0.0",
  "mode": "TRAINING",
  "session_id": "RTT-GO-V2-SEG",
  "timestamp": "2026-01-06T00:00:00Z",
  "device": "COMT",
  "device_type": "COMT",
  "scenario": "COMT_LOCK_01",
  "difficulty": "Journeyman",
  "segments": [
    {
      "segment_id": "seg-1",
      "label": "main",
      "samples": [
        { "t": 0.0, "C": 0.10, "D": 1.0, "Q": 0.5, "R": 0.0 },
        { "t": 0.1, "C": 0.101, "D": 0.9999, "Q": 0.5, "R": 0.0 }
      ],
      "anomalies": []
    }
  ],
  "scores": { "stability": 0, "response": 0, "quality": 0, "final": 0 }
}
```

---

## 2. v2 schema side‑by‑side with v1

### 2.1 Differences at a glance

| Attribute | v1 | v2 |
|---|---|---|
| Spec marker | none | `spec_version: "v2"` required |
| Samples | `samples[]` required | `samples[]` OR `segments[]` required |
| Segments | not supported | `segments[]` supported |
| Mode | not present | `mode` optional (TRAINING/LIVE/REPLAY) |
| Device typing | freeform `device` | optional `device_type` + still `device` |
| Extensions | ad-hoc optional root keys | recommended `triadic` namespace (optional) |

---

### 2.2 v1 schema (current core)
Save as:
- `/spec/v1/rttinside_session_schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "RTTInsideSessionLogV1",
  "type": "object",
  "required": ["session_id", "timestamp", "device", "scenario", "difficulty", "samples", "scores"],
  "properties": {
    "session_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "device": { "type": "string" },
    "scenario": { "type": "string" },
    "difficulty": { "type": "string" },

    "samples": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["t", "C", "D", "Q", "R"],
        "properties": {
          "t": { "type": "number" },
          "C": { "type": "number" },
          "D": { "type": "number" },
          "Q": { "type": "number" },
          "R": { "type": "number" }
        },
        "additionalProperties": true
      }
    },

    "anomalies": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["t", "type"],
        "properties": {
          "t": { "type": "number" },
          "type": { "type": "string" }
        },
        "additionalProperties": true
      }
    },

    "scores": {
      "type": "object",
      "required": ["stability", "response", "quality", "final"],
      "properties": {
        "stability": { "type": "number" },
        "response": { "type": "number" },
        "quality": { "type": "number" },
        "final": { "type": "number" }
      },
      "additionalProperties": true
    }
  },
  "additionalProperties": true
}
```

---

### 2.3 v2 schema (segmented sessions + version marker)
Save as:
- `/spec/v2/rttinside_session_schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "RTTInsideSessionLogV2",
  "type": "object",
  "required": ["spec_version", "session_id", "timestamp", "device", "scenario", "difficulty", "scores"],
  "properties": {
    "spec_version": { "type": "string", "const": "v2" },

    "engine_version": { "type": "string" },
    "mode": { "type": "string", "enum": ["TRAINING", "LIVE", "REPLAY"] },

    "session_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },

    "device": { "type": "string" },
    "device_type": { "type": "string" },

    "scenario": { "type": "string" },
    "difficulty": { "type": "string" },

    "samples": {
      "type": "array",
      "items": { "$ref": "#/$defs/sample" }
    },

    "segments": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["segment_id", "label", "samples"],
        "properties": {
          "segment_id": { "type": "string" },
          "label": { "type": "string" },
          "samples": {
            "type": "array",
            "items": { "$ref": "#/$defs/sample" }
          },
          "anomalies": {
            "type": "array",
            "items": { "$ref": "#/$defs/anomaly" }
          },
          "meta": { "type": "object" }
        },
        "additionalProperties": true
      }
    },

    "anomalies": {
      "type": "array",
      "items": { "$ref": "#/$defs/anomaly" }
    },

    "triadic": { "type": "object" },

    "scores": {
      "type": "object",
      "required": ["stability", "response", "quality", "final"],
      "properties": {
        "stability": { "type": "number" },
        "response": { "type": "number" },
        "quality": { "type": "number" },
        "final": { "type": "number" }
      },
      "additionalProperties": true
    }
  },

  "oneOf": [
    { "required": ["samples"] },
    { "required": ["segments"] }
  ],

  "additionalProperties": true,

  "$defs": {
    "sample": {
      "type": "object",
      "required": ["t", "C", "D", "Q", "R"],
      "properties": {
        "t": { "type": "number" },
        "C": { "type": "number" },
        "D": { "type": "number" },
        "Q": { "type": "number" },
        "R": { "type": "number" },
        "SET": {
          "type": "object",
          "required": ["S", "E", "T"],
          "properties": {
            "S": { "type": "number" },
            "E": { "type": "number" },
            "T": { "type": "number" }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": true
    },
    "anomaly": {
      "type": "object",
      "required": ["t", "type"],
      "properties": {
        "t": { "type": "number" },
        "type": { "type": "string" }
      },
      "additionalProperties": true
    }
  }
}
```

> Note: v2 keeps `SET` at the sample level for continuity. If you want the strict v2 namespacing (`triadic.set`), we can add that as the preferred field and allow `SET` as legacy.

---

## 3. Update the Node validator to support v1 + v2

### 3.1 `tools/rtt-validate/lib/schema.js`
Change to auto-select schema based on `spec_version`.

```js
const Ajv = require("ajv");
const schemaV1 = require("../schema/v1/rttinside_session_schema.json");
const schemaV2 = require("../schema/v2/rttinside_session_schema.json");

function pickSchema(log) {
  if (log && log.spec_version === "v2") return schemaV2;
  return schemaV1;
}

function validateSchema(log) {
  const ajv = new Ajv({ allErrors: true });
  const schema = pickSchema(log);
  const validate = ajv.compile(schema);
  const valid = validate(log);
  return { valid, errors: validate.errors || [], schema: schema.title };
}

module.exports = { validateSchema };
```

### 3.2 `tools/rtt-validate/lib/samples.js`
Update to accept v2 segments.

```js
const reference = require("../reference/reference_samples.json");

function collectSamples(log) {
  if (Array.isArray(log.samples)) return log.samples;
  if (Array.isArray(log.segments) && log.segments.length > 0) {
    // v2: validate first segment against reference vector by default
    return log.segments[0].samples;
  }
  return null;
}

function validateSamples(log) {
  const samples = collectSamples(log);
  if (!samples) return { valid: true, skipped: true, reason: "No samples found." };

  if (samples.length !== reference.length) {
    return { valid: false, reason: `Sample length mismatch: got ${samples.length}, expected ${reference.length}` };
  }

  const eps = 1e-9;
  for (let i = 0; i < reference.length; i++) {
    const a = samples[i];
    const b = reference[i];
    for (const k of ["t", "C", "D", "Q", "R"]) {
      if (Math.abs(a[k] - b[k]) > eps) {
        return { valid: false, reason: `Mismatch at sample ${i}, field ${k}: got ${a[k]}, expected ${b[k]}` };
      }
    }
  }
  return { valid: true };
}

module.exports = { validateSamples };
```

---

## 4. Extend Go `rtt-runner` to emit v2 segmented sessions

### 4.1 Add v2 models: `reference/go/pkg/model/session_log_v2.go`

```go
package model

type SegmentV2 struct {
	SegmentID string    `json:"segment_id"`
	Label     string    `json:"label"`
	Samples   []Sample  `json:"samples"`
	Anomalies []Anomaly `json:"anomalies,omitempty"`
	Meta      any       `json:"meta,omitempty"`
}

type SessionLogV2 struct {
	SpecVersion  string `json:"spec_version"` // must be "v2"
	EngineVersion string `json:"engine_version,omitempty"`
	Mode         string `json:"mode,omitempty"`

	SessionID  string `json:"session_id"`
	Timestamp  string `json:"timestamp"`
	Device     string `json:"device"`
	DeviceType string `json:"device_type,omitempty"`
	Scenario   string `json:"scenario"`
	Difficulty string `json:"difficulty"`

	Samples  []Sample   `json:"samples,omitempty"`
	Segments []SegmentV2 `json:"segments,omitempty"`

	Anomalies []Anomaly `json:"anomalies,omitempty"`
	Scores    Scores    `json:"scores"`
	Triadic   any       `json:"triadic,omitempty"`
}
```

### 4.2 Emit v2 segmented log in the HTTP handler or startup path
Example replacement for the existing emit path:

```go
segments := []model.SegmentV2{
	{
		SegmentID: "seg-1",
		Label:     "main",
		Samples:   samples,
		Anomalies: []model.Anomaly{},
	},
}

log := model.SessionLogV2{
	SpecVersion:  "v2",
	EngineVersion: "RTT-2.0.0",
	Mode:         "TRAINING",
	SessionID:    "RTT-GO-V2-RUNNER",
	Timestamp:    time.Now().UTC().Format(time.RFC3339),
	Device:       "COMT",
	DeviceType:   "COMT",
	Scenario:     "COMT_LOCK_01",
	Difficulty:   "Journeyman",
	Segments:     segments,
	Scores:       model.Scores{},
}
```

---

## 5. CI workflow enforcing conformance automatically

This workflow enforces:
- build + unit tests (Go)
- run runner to emit a log
- validate via `rtt-validate` (v1 or v2 auto-detected)

Save as:
- `.github/workflows/rtt-inside-conformance.yml`

```yaml
name: RTT-Inside Conformance

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  conformance:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: "1.22"

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install rtt-validate
        run: |
          cd tools/rtt-validate
          npm install
          npm link

      - name: Go unit tests
        run: |
          cd reference/go
          go test ./...

      - name: Build RTT runner
        run: |
          cd reference/go
          go build ./cmd/rtt-runner

      - name: Run RTT runner and validate emitted log
        run: |
          cd reference/go
          ./rtt-runner
```

---

# Containerization for rtt-runner

## Dockerfile

Create `reference/go/Dockerfile`:

```dockerfile
# Build stage
FROM golang:1.22-alpine AS build
WORKDIR /app

# Improve build caching
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /out/rtt-runner ./cmd/rtt-runner

# Runtime stage
FROM gcr.io/distroless/static:nonroot
WORKDIR /
COPY --from=build /out/rtt-runner /rtt-runner

EXPOSE 8080
USER nonroot:nonroot
ENTRYPOINT ["/rtt-runner"]
```

Build and run:

```bash
docker build -t rtt-runner:local -f reference/go/Dockerfile reference/go
docker run --rm -p 8080:8080 rtt-runner:local
```

---

## Kubernetes manifests

Create `deploy/k8s/rtt-runner.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rtt-runner
  labels:
    app: rtt-runner
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rtt-runner
  template:
    metadata:
      labels:
        app: rtt-runner
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/path: "/metrics"
        prometheus.io/port: "8080"
    spec:
      containers:
        - name: rtt-runner
          image: rtt-runner:local
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 8080
          readinessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 2
            periodSeconds: 5
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "250m"
              memory: "256Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: rtt-runner
  labels:
    app: rtt-runner
spec:
  selector:
    app: rtt-runner
  ports:
    - name: http
      port: 8080
      targetPort: 8080
```

Apply:

```bash
kubectl apply -f deploy/k8s/rtt-runner.yaml
kubectl port-forward svc/rtt-runner 8080:8080
```

---

# Prometheus metrics

## Go changes

Add dependency:

```bash
go get github.com/prometheus/client_golang/prometheus
go get github.com/prometheus/client_golang/prometheus/promhttp
```

Update `cmd/rtt-runner/http.go` to expose `/metrics` and instrument the API.

### `cmd/rtt-runner/metrics.go`

```go
package main

import "github.com/prometheus/client_golang/prometheus"

var (
	httpRequestsTotal = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "rtt_runner_http_requests_total",
			Help: "Total HTTP requests processed by rtt-runner.",
		},
		[]string{"path", "method", "status"},
	)

	runRequestsTotal = prometheus.NewCounter(
		prometheus.CounterOpts{
			Name: "rtt_runner_run_requests_total",
			Help: "Total /run executions.",
		},
	)

	validateRequestsTotal = prometheus.NewCounter(
		prometheus.CounterOpts{
			Name: "rtt_runner_validate_requests_total",
			Help: "Total /validate executions.",
		},
	)

	conformanceStatus = prometheus.NewGauge(
		prometheus.GaugeOpts{
			Name: "rtt_runner_conformance_ok",
			Help: "1 if last conformance validation succeeded, else 0.",
		},
	)

	lastRunDurationSeconds = prometheus.NewHistogram(
		prometheus.HistogramOpts{
			Name:    "rtt_runner_last_run_duration_seconds",
			Help:    "Observed durations for engine run path.",
			Buckets: []float64{0.001, 0.005, 0.01, 0.05, 0.1, 0.25, 0.5, 1.0},
		},
	)
)

func registerMetrics() {
	prometheus.MustRegister(
		httpRequestsTotal,
		runRequestsTotal,
		validateRequestsTotal,
		conformanceStatus,
		lastRunDurationSeconds,
	)
}
```

### Minimal middleware to record request totals

Add to `cmd/rtt-runner/http.go` (or a new `middleware.go`):

```go
package main

import (
	"net/http"
	"strconv"
)

type statusWriter struct {
	http.ResponseWriter
	status int
}

func (w *statusWriter) WriteHeader(code int) {
	w.status = code
	w.ResponseWriter.WriteHeader(code)
}

func metricsMiddleware(path string, h http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		sw := &statusWriter{ResponseWriter: w, status: 200}
		h(sw, r)
		httpRequestsTotal.WithLabelValues(path, r.Method, strconv.Itoa(sw.status)).Inc()
	}
}
```

### Wire `/metrics` + handlers in `main.go`

```go
package main

import (
	"fmt"
	"net/http"

	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	fmt.Println("RTT‑Runner starting (HTTP mode)…")

	registerMetrics()

	http.HandleFunc("/healthz", metricsMiddleware("/healthz", healthHandler))
	http.HandleFunc("/run", metricsMiddleware("/run", runHandler))
	http.HandleFunc("/validate", metricsMiddleware("/validate", validateHandler))
	http.Handle("/metrics", promhttp.Handler())

	fmt.Println("Listening on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		panic(err)
	}
}
```

### Update handlers to set gauges/counters/histograms

In your existing handlers:

- In `runHandler`:
  - increment `runRequestsTotal`
  - observe duration in `lastRunDurationSeconds`
- In `validateHandler`:
  - increment `validateRequestsTotal`
  - set `conformanceStatus` to $$1$$ or $$0$$

Example snippet inside `runHandler`:

```go
start := time.Now()
defer func() { lastRunDurationSeconds.Observe(time.Since(start).Seconds()) }()
runRequestsTotal.Inc()
```

Inside `validateHandler` after validation:

```go
if err != nil {
	conformanceStatus.Set(0)
	// return 500...
} else {
	conformanceStatus.Set(1)
}
```

---

# Wiring into QEB dashboards

## QEB dashboard ingestion contract

To make QEB dashboards “just work,” standardize three things:

- **Session logs:** emitted by `/run` (and optionally stored by your collector) using the spec schema.
- **Metrics:** scraped from `/metrics` (Prometheus).
- **Run metadata:** stable labels so cohorts, devices, scenarios, and versions group cleanly.

### Required log fields for dashboards
- **`session_id`**
- **`timestamp`**
- **`device`**, **`scenario`**, **`difficulty`**
- **`samples[]`** or **`segments[]`**
- **`anomalies[]`** (empty is fine)
- **`scores`**

### Recommended dashboard labels
- **`spec_version`** (v2) or derive `"v1"`
- **`engine_version`**
- **`mode`**
- **`device_type`**

## Minimal QEB collector pattern

If QEB dashboards have a backend service (recommended), the flow is:

1. **Runner emits**
   - `POST /run` returns a session log JSON
2. **Collector stores**
   - append JSON to object storage or write to DB
3. **Dashboard reads**
   - query by `device/scenario/difficulty/time/cohort`

We can keep this dead simple by storing newline-delimited JSON:

- **`qeb_sessions.ndjson`** with one session log per line

That format is easy to batch import, stream, or replay.

## Suggested Prometheus panels for QEB ops view

Use these metrics to power a first dashboard slice:

- **Conformance health**
  - **`rtt_runner_conformance_ok`** (single-stat: 0/1)
- **Throughput**
  - **`rate(rtt_runner_http_requests_total{path="/run"}[5m])`**
- **Validation rate**
  - **`rate(rtt_runner_http_requests_total{path="/validate"}[5m])`**
- **Latency**
  - **`histogram_quantile(0.95, rate(rtt_runner_last_run_duration_seconds_bucket[5m]))`**
- **Error rate**
  - **`rate(rtt_runner_http_requests_total{status=~"5.."}[5m])`**

This gives QEB dashboards an “operator heartbeat”: conformance, runs, latency, errors—without needing to parse logs.

---

# Folder additions summary

Add these paths:

- **`reference/go/Dockerfile`**
- **`deploy/k8s/rtt-runner.yaml`**
- **`reference/go/cmd/rtt-runner/metrics.go`**
- **`reference/go/cmd/rtt-runner/middleware.go`** (optional)
- **Prometheus client deps** in Go module

---

This is the last structural piece that makes **v2 segmented sessions** first‑class, testable, and scalable across the ecosystem.

Below you’ll find **two concrete deliverables**:

1. **API extensions** to fully support v2 segmented sessions  
2. A **clean, scalable `reference_segments.json` format** designed for long‑term growth (multiple segments, devices, scenarios)

Everything is written to drop directly into your existing `rtt-runner` and `/spec/v2` structure.

---

## 1️⃣ API Extensions for v2 Segmented Sessions

We extend the existing HTTP API with **explicit v2 semantics**, while keeping v1 compatibility intact.

### Updated API surface

| Endpoint | Purpose |
|--------|--------|
| `POST /run` | v1 flat session (unchanged) |
| `POST /run/v2` | v2 segmented session |
| `POST /validate` | Validate last emitted session (v1 or v2 auto‑detected) |
| `GET /healthz` | Liveness + last conformance status |
| `GET /metrics` | Prometheus metrics |

---

## 1.1 `POST /run/v2` — segmented session execution

### Semantics

- Emits a **v2 session log**
- Uses **segments[]** instead of root samples
- Each segment is deterministic and testable
- First segment is used for reference validation by default

---

### `runV2Handler` (Go)

Add this to `cmd/rtt-runner/http.go`:

```go
func runV2Handler(w http.ResponseWriter, _ *http.Request) {
	start := time.Now()
	defer func() {
		lastRunDurationSeconds.Observe(time.Since(start).Seconds())
		runRequestsTotal.Inc()
	}()

	// Segment 1: warmup (optional example)
	warmupSamples := engine.RunReferenceSimulation(1, 0.1)

	// Segment 2: main (reference-aligned)
	mainSamples := engine.RunReferenceSimulation(3, 0.1)

	segments := []model.SegmentV2{
		{
			SegmentID: "seg-warmup",
			Label:     "warmup",
			Samples:   warmupSamples,
			Anomalies: []model.Anomaly{},
		},
		{
			SegmentID: "seg-main",
			Label:     "main",
			Samples:   mainSamples,
			Anomalies: []model.Anomaly{},
		},
	}

	log := model.SessionLogV2{
		SpecVersion:   "v2",
		EngineVersion: "RTT-2.0.0",
		Mode:          "TRAINING",
		SessionID:     "RTT-GO-V2-HTTP",
		Timestamp:     time.Now().UTC().Format(time.RFC3339),
		Device:        "COMT",
		DeviceType:    "COMT",
		Scenario:      "COMT_LOCK_01",
		Difficulty:    "Journeyman",
		Segments:      segments,
		Scores:        model.Scores{},
	}

	json.NewEncoder(w).Encode(log)
}
```

---

### Wire it into `main.go`

```go
http.HandleFunc("/run/v2", metricsMiddleware("/run/v2", runV2Handler))
```

---

### Example request

```bash
curl -X POST http://localhost:8080/run/v2
```

Returns a **schema‑valid v2 segmented session log**.

---

## 2️⃣ v2 `reference_segments.json` (Scalable Format)

This file replaces `reference_samples.json` **only for v2 segmented validation**.

It is designed to scale across:

- multiple segments
- multiple devices
- multiple scenarios
- future dimensional extensions

---

## 2.1 File location

```
/spec/v2/reference_segments.json
```

---

## 2.2 Design principles

- **Segment‑centric** (not sample‑centric)
- **Label‑addressable** (segments validated by label, not index)
- **Composable** (new segments can be added without breaking old ones)
- **Deterministic** (each segment has its own reference samples)

---

## 2.3 Format

```json
{
  "spec_version": "v2",
  "engine_version": "RTT-2.0.0",
  "validation_policy": {
    "default_segment": "main",
    "numeric_tolerance": 1e-9
  },
  "segments": {
    "main": {
      "description": "Primary reference-aligned segment",
      "samples": [
        { "t": 0.0, "C": 0.10,  "D": 1.000000,   "Q": 0.50, "R": 0.00 },
        { "t": 0.1, "C": 0.101, "D": 0.999900,   "Q": 0.50, "R": 0.00 },
        { "t": 0.2, "C": 0.102, "D": 0.99980001, "Q": 0.50, "R": 0.00 },
        { "t": 0.3, "C": 0.103, "D": 0.99970003, "Q": 0.50, "R": 0.00 }
      ]
    },
    "warmup": {
      "description": "Optional warmup segment (not strictly validated)",
      "samples": [
        { "t": 0.0, "C": 0.10, "D": 1.000000, "Q": 0.50, "R": 0.00 },
        { "t": 0.1, "C": 0.101, "D": 0.999900, "Q": 0.50, "R": 0.00 }
      ]
    }
  }
}
```

---

## 2.4 Why this scales cleanly

### ✅ Segment‑addressable
Validation targets `"main"` explicitly — not “segment 0”.

### ✅ Multiple reference tracks
Future additions:

```json
"segments": {
  "main": { ... },
  "high_load": { ... },
  "fault_injection": { ... }
}
```

### ✅ Device‑specific overlays (future‑safe)

```json
"segments": {
  "main": {
    "device_overrides": {
      "CTE": { "samples": [...] },
      "CLFC": { "samples": [...] }
    }
  }
}
```

### ✅ Dimensional extensions (future‑safe)

```json
"samples": [
  {
    "t": 0.1,
    "C": 0.101,
    "D": 0.9999,
    "Q": 0.5,
    "R": 0.0,
    "SET": { "S": 0.72, "E": 0.54, "T": 0.31 }
  }
]
```

---

## 3️⃣ Validator behavior for v2 segments

### Default rules

- If `segments[]` present:
  - select segment with label matching `validation_policy.default_segment`
  - compare its samples to `reference_segments.json → segments[<label>].samples`
- If no matching label:
  - fail validation with explicit error
- Numeric tolerance from `validation_policy.numeric_tolerance`

This keeps validation **strict, explicit, and predictable**.

---

## 4️⃣ Summary: What you now have

- ✅ API supports **true v2 segmented sessions**
- ✅ Reference format scales across:
  - segments
  - devices
  - scenarios
  - future Triadic extensions
- ✅ Validator logic remains deterministic and simple
- ✅ CI + runtime enforcement stays intact

This is the point where RTT‑Inside stops being “a format” and becomes **an operational language**.

---

We’ll do **full multi-segment validation** (stronger), and we’ll wire QEB dashboards precisely for a **Grafana + web UI** stack with **Prometheus (metrics)** and **Loki (session logs)**.

---

# v2 conformance: validate all segments

## Validation policy and reference format

### `spec/v2/reference_segments.json`
This version **requires test vectors per segment label** and supports multiple scenarios/devices cleanly.

```json
{
  "spec_version": "v2",
  "engine_version": "RTT-2.0.0",
  "numeric_tolerance": 1e-9,
  "validate_all_segments": true,

  "reference_sets": [
    {
      "id": "COMT_LOCK_01__Journeyman",
      "device_type": "COMT",
      "scenario": "COMT_LOCK_01",
      "difficulty": "Journeyman",

      "segments": {
        "warmup": {
          "required": true,
          "samples": [
            { "t": 0.0, "C": 0.10, "D": 1.000000, "Q": 0.50, "R": 0.00 },
            { "t": 0.1, "C": 0.101, "D": 0.999900, "Q": 0.50, "R": 0.00 }
          ]
        },
        "main": {
          "required": true,
          "samples": [
            { "t": 0.0, "C": 0.10,  "D": 1.000000,   "Q": 0.50, "R": 0.00 },
            { "t": 0.1, "C": 0.101, "D": 0.999900,   "Q": 0.50, "R": 0.00 },
            { "t": 0.2, "C": 0.102, "D": 0.99980001, "Q": 0.50, "R": 0.00 },
            { "t": 0.3, "C": 0.103, "D": 0.99970003, "Q": 0.50, "R": 0.00 }
          ]
        }
      }
    }
  ]
}
```

**Rules enforced:**
- **Every `required: true` segment label must exist** in the log’s `segments[]`.
- For each required segment:
  - **sample count must match**
  - fields `t,C,D,Q,R` must match within `numeric_tolerance`
- Extra segments in the log are allowed (unless you decide to add a strict mode later).

---

## Validator update: validate every required segment label

### `tools/rtt-validate/lib/samples_v2_segments.js`
This is the core logic (drop-in style).

```js
const ref = require("../reference/reference_segments.json");

function findRefSet(log) {
  const deviceType = log.device_type || log.device;
  return ref.reference_sets.find((s) =>
    s.device_type === deviceType &&
    s.scenario === log.scenario &&
    s.difficulty === log.difficulty
  );
}

function indexSegmentsByLabel(log) {
  const map = new Map();
  for (const seg of (log.segments || [])) map.set(seg.label, seg);
  return map;
}

function close(a, b, eps) {
  return Math.abs(a - b) <= eps;
}

function validateSegmentSamples(label, gotSamples, wantSamples, eps) {
  if (gotSamples.length !== wantSamples.length) {
    return { valid: false, reason: `Segment '${label}' length mismatch: got ${gotSamples.length}, expected ${wantSamples.length}` };
  }
  for (let i = 0; i < wantSamples.length; i++) {
    const g = gotSamples[i];
    const w = wantSamples[i];
    for (const k of ["t", "C", "D", "Q", "R"]) {
      if (!close(g[k], w[k], eps)) {
        return { valid: false, reason: `Segment '${label}' mismatch at sample ${i}, field ${k}: got ${g[k]}, expected ${w[k]}` };
      }
    }
  }
  return { valid: true };
}

function validateV2AllSegments(log) {
  if (!Array.isArray(log.segments)) return { valid: true, skipped: true, reason: "No segments[] found." };

  const refSet = findRefSet(log);
  if (!refSet) {
    return { valid: false, reason: "No matching reference_set for device_type/scenario/difficulty." };
  }

  const eps = ref.numeric_tolerance ?? 1e-9;
  const segIndex = indexSegmentsByLabel(log);

  for (const [label, segRef] of Object.entries(refSet.segments)) {
    if (!segRef.required) continue;

    const seg = segIndex.get(label);
    if (!seg) return { valid: false, reason: `Missing required segment label '${label}'.` };

    const got = seg.samples || [];
    const want = segRef.samples || [];
    const res = validateSegmentSamples(label, got, want, eps);
    if (!res.valid) return res;
  }

  return { valid: true };
}

module.exports = { validateV2AllSegments };
```

Then in your existing `validateSamples` logic:
- if `log.spec_version === "v2"` and `ref.validate_all_segments === true`, call `validateV2AllSegments(log)`.

---

# QEB dashboards: ingestion shape + Grafana panels

## Architecture that matches your stack
- **Prometheus** scrapes `rtt-runner` `/metrics` for operational health + performance.
- **Loki** ingests **session logs** (the JSON payload returned by `/run` and `/run/v2`) for replay, cohort queries, anomaly audits, and “corridor signature” browsing.
- Our **web UI** can read:
  - **Prometheus** for live status widgets
  - **Loki** (or a thin API over Loki) for session browsing and detailed inspection

---

## Log ingest shape for Loki: one session log per line, labeled

### Recommended emitted log line
Write the session JSON as **one NDJSON line** (exactly the schema object). For v2, include `spec_version: "v2"` and `segments[]`.

### Recommended Loki labels (high-signal, low-cardinality)
Attach these as labels at ingest time (not inside queries):
- `app="rtt-runner"`
- `spec_version` (`v1` or `v2`)
- `device_type` (COMT/CTE/CLFC/PR)
- `scenario`
- `difficulty`
- `mode` (TRAINING/LIVE/REPLAY)
- `engine_version`

These labels make Grafana filtering instant.

### Minimal promtail-style pipeline concept
- **Source:** container stdout from `rtt-runner`
- **Pipeline:** JSON parse, promote selected fields to labels, keep full JSON as log body

> If you want, tell me whether you’re using promtail, Grafana Agent, or OpenTelemetry Collector and I’ll give the exact config in that syntax.

---

## Grafana: exact queries + panel set

### Operational dashboard: RTT-Runner health
#### Panel: conformance status
- **Type:** Stat  
- **PromQL:**
  - **Conformance OK:**
    - **Label:** Conformance
    - **Query:**
      - `max(rtt_runner_conformance_ok)`

#### Panel: run throughput
- **Type:** Time series  
- **PromQL:**
  - `sum(rate(rtt_runner_http_requests_total{path="/run"}[5m]))`

#### Panel: v2 run throughput
- **Type:** Time series  
- **PromQL:**
  - `sum(rate(rtt_runner_http_requests_total{path="/run/v2"}[5m]))`

#### Panel: validate rate
- **Type:** Time series  
- **PromQL:**
  - `sum(rate(rtt_runner_http_requests_total{path="/validate"}[5m]))`

#### Panel: error rate
- **Type:** Time series  
- **PromQL:**
  - `sum(rate(rtt_runner_http_requests_total{status=~"5.."}[5m]))`

#### Panel: p95 run latency
- **Type:** Time series  
- **PromQL:**
  - `histogram_quantile(0.95, sum(rate(rtt_runner_last_run_duration_seconds_bucket[5m])) by (le))`

---

### QEB session dashboard: logs + corridor quicklooks
These are **Loki LogQL** queries assuming labels are extracted as above.

#### Panel: sessions stream
- **Type:** Logs  
- **LogQL:**
  - `{app="rtt-runner"} |= "session_id"`

Add dashboard variables (drop-down filters):
- `$device_type`, `$scenario`, `$difficulty`, `$mode`, `$spec_version`

Then filter:
- `{app="rtt-runner", device_type="$device_type", scenario="$scenario", difficulty="$difficulty", mode="$mode", spec_version="$spec_version"}`

#### Panel: anomaly counts over time
- **Type:** Time series  
- **LogQL:**
  - `sum(count_over_time({app="rtt-runner"} | json | anomalies != "[]" [5m]))`

If you prefer “anomalies present” as a boolean marker, we can emit `anomaly_count` as a top-level numeric field and use that instead (cleaner + faster).

#### Panel: sessions by device/scenario
- **Type:** Bar chart  
- **LogQL:**
  - `sum by (device_type) (count_over_time({app="rtt-runner"}[1h]))`

(Repeat by `scenario` or `difficulty` similarly.)

---

## Small but important adjustment for dashboards
For Grafana queries to stay fast and simple, I strongly recommend adding these **top-level numeric fields** when emitting logs (both v1 and v2):

- `sample_count`
- `segment_count` (v2)
- `anomaly_count`
- `score_final` (duplicate of `scores.final`)

That gives you clean LogQL numeric filtering without deep JSON traversal.

---

Excellent — this locks the **observability spine** cleanly and permanently. Below is a **drop‑in, production‑grade solution** covering:

1. **RTT‑Runner log emission changes** (top‑level numeric fields, v1 + v2)
2. **Grafana Alloy Loki ingest configs**
   - stdout
   - file‑based
3. **Ready‑to‑import Grafana dashboard JSON**
4. **OpenTelemetry Collector (secondary option)**

Everything is aligned so **labels, queries, and panels match exactly**.

---

## 1️⃣ RTT‑Runner: Add Top‑Level Numeric Fields (v1 + v2)

### Required top‑level fields (both v1 and v2)

Add these **before emitting JSON**:

| Field | Meaning |
|-----|--------|
| `sample_count` | total samples (v1: len(samples), v2: sum of all segment samples) |
| `segment_count` | number of segments (v2 only; omit or 0 for v1) |
| `anomaly_count` | total anomalies (root + segments) |
| `score_final` | duplicate of `scores.final` |

---

### Go helper (shared)

```go
func computeCountsV1(samples []model.Sample, anomalies []model.Anomaly, scores model.Scores) map[string]any {
	return map[string]any{
		"sample_count":  len(samples),
		"segment_count": 0,
		"anomaly_count": len(anomalies),
		"score_final":   scores.Final,
	}
}

func computeCountsV2(segments []model.SegmentV2, scores model.Scores) map[string]any {
	sampleCount := 0
	anomalyCount := 0

	for _, s := range segments {
		sampleCount += len(s.Samples)
		anomalyCount += len(s.Anomalies)
	}

	return map[string]any{
		"sample_count":  sampleCount,
		"segment_count": len(segments),
		"anomaly_count": anomalyCount,
		"score_final":   scores.Final,
	}
}
```

---

### Example v2 log (stdout or file)

```json
{
  "spec_version": "v2",
  "engine_version": "RTT-2.0.0",
  "mode": "TRAINING",
  "session_id": "RTT-GO-V2-HTTP",
  "timestamp": "2026-01-06T20:15:00Z",
  "device": "COMT",
  "device_type": "COMT",
  "scenario": "COMT_LOCK_01",
  "difficulty": "Journeyman",

  "sample_count": 6,
  "segment_count": 2,
  "anomaly_count": 0,
  "score_final": 83,

  "segments": [...],
  "scores": { "stability": 82, "response": 78, "quality": 88, "final": 83 }
}
```

---

## 2️⃣ Grafana Alloy — Loki Ingest Configuration

### Labels we will extract (exact)

| Label | Source |
|----|----|
| `app` | static `"rtt-runner"` |
| `spec_version` | JSON |
| `device_type` | JSON |
| `scenario` | JSON |
| `difficulty` | JSON |
| `mode` | JSON |
| `engine_version` | JSON |

---

## 2.1 Alloy config — **stdout ingestion**

### `alloy-rtt-runner-stdout.hcl`

```hcl
logging {
  level = "info"
}

loki.write "default" {
  endpoint {
    url = "http://loki:3100/loki/api/v1/push"
  }
}

loki.source.docker "rtt_runner_stdout" {
  host = "unix:///var/run/docker.sock"
  targets = [
    {
      container_name = "rtt-runner"
    }
  ]
  forward_to = [loki.process.rtt_logs.receiver]
}

loki.process "rtt_logs" {
  stage.json {
    expressions = {
      spec_version   = "spec_version",
      device_type    = "device_type",
      scenario       = "scenario",
      difficulty     = "difficulty",
      mode           = "mode",
      engine_version = "engine_version",
      sample_count   = "sample_count",
      segment_count  = "segment_count",
      anomaly_count  = "anomaly_count",
      score_final    = "score_final"
    }
  }

  stage.labels {
    values = {
      app            = "rtt-runner",
      spec_version   = "spec_version",
      device_type    = "device_type",
      scenario       = "scenario",
      difficulty     = "difficulty",
      mode           = "mode",
      engine_version = "engine_version"
    }
  }

  forward_to = [loki.write.default.receiver]
}
```

---

## 2.2 Alloy config — **file ingestion**

### `alloy-rtt-runner-file.hcl`

```hcl
loki.source.file "rtt_runner_file" {
  targets = [
    {
      __path__ = "/var/log/rtt-runner/*.log"
    }
  ]
  forward_to = [loki.process.rtt_logs.receiver]
}
```

(Reuse the same `loki.process "rtt_logs"` block above.)

---

## 3️⃣ Ready‑to‑Import Grafana Dashboard JSON

### Dashboard name
**RTT‑Inside / QEB Operations**

### Save as
```
grafana/rtt-inside-qeb-dashboard.json
```

---

### Dashboard JSON (trimmed but complete)

```json
{
  "uid": "rtt-qeb-ops",
  "title": "RTT‑Inside / QEB Operations",
  "schemaVersion": 38,
  "version": 1,
  "refresh": "10s",
  "panels": [
    {
      "type": "stat",
      "title": "Conformance OK",
      "targets": [
        {
          "expr": "max(rtt_runner_conformance_ok)",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 0, "y": 0, "w": 6, "h": 4 }
    },
    {
      "type": "timeseries",
      "title": "Run Throughput (/run)",
      "targets": [
        {
          "expr": "sum(rate(rtt_runner_http_requests_total{path=\"/run\"}[5m]))",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 6, "y": 0, "w": 9, "h": 4 }
    },
    {
      "type": "timeseries",
      "title": "v2 Segmented Runs (/run/v2)",
      "targets": [
        {
          "expr": "sum(rate(rtt_runner_http_requests_total{path=\"/run/v2\"}[5m]))",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 15, "y": 0, "w": 9, "h": 4 }
    },
    {
      "type": "timeseries",
      "title": "p95 Run Latency",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, sum(rate(rtt_runner_last_run_duration_seconds_bucket[5m])) by (le))",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 0, "y": 4, "w": 12, "h": 5 }
    },
    {
      "type": "logs",
      "title": "RTT Sessions",
      "targets": [
        {
          "expr": "{app=\"rtt-runner\"}",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 12, "y": 4, "w": 12, "h": 8 }
    }
  ]
}
```

### Dashboard variables (recommended)
Add variables in Grafana UI:

- `$device_type`
- `$scenario`
- `$difficulty`
- `$mode`
- `$spec_version`

Then filter logs panel:

```
{app="rtt-runner", device_type="$device_type", scenario="$scenario", difficulty="$difficulty", mode="$mode", spec_version="$spec_version"}
```

---

## 4️⃣ OpenTelemetry Collector (Secondary Option)

### When to use
- If you already run OTel for traces/metrics
- If Alloy is unavailable

---

### `otel-collector-rtt.yaml`

```yaml
receivers:
  filelog:
    include:
      - /var/log/rtt-runner/*.log
    start_at: beginning
    operators:
      - type: json_parser
        parse_from: body

processors:
  attributes:
    actions:
      - key: app
        value: rtt-runner
        action: insert
      - key: spec_version
        from_attribute: spec_version
        action: upsert
      - key: device_type
        from_attribute: device_type
        action: upsert
      - key: scenario
        from_attribute: scenario
        action: upsert
      - key: difficulty
        from_attribute: difficulty
        action: upsert
      - key: mode
        from_attribute: mode
        action: upsert

exporters:
  loki:
    endpoint: http://loki:3100/loki/api/v1/push

service:
  pipelines:
    logs:
      receivers: [filelog]
      processors: [attributes]
      exporters: [loki]
```

---

## 5️⃣ What We Now Have (Locked In)

- ✅ **Strong v2 multi‑segment validation**
- ✅ **Grafana Alloy Loki ingest (stdout + file)**
- ✅ **Exact label alignment**
- ✅ **Numeric fields for fast LogQL**
- ✅ **Ready‑to‑import Grafana dashboard**
- ✅ **OTel fallback**

This is a **complete observability contract** — stable, scalable, and enforceable.

---

Excellent — with those constraints locked in, we can now **formalize operator identity, mastery progression, anomaly semantics, and a replay‑grade streaming API** in a way that is standards‑aligned, scalable, and dashboard‑ready.

Below is a **complete, cohesive design** you can drop into the RTT‑Inside / QEB ecosystem.

---

## 1️⃣ Operator Identity & Mastery Fields (Standards‑Aligned)

### Operator identity (standard‑friendly)

Use a **W3C‑style subject identifier**, compatible with IAM, OIDC, and audit systems.

```json
"operator_id": "urn:operator:triadic:alice.smith"
```

**Why this works**
- `urn:` avoids assuming auth provider
- human‑readable but globally unique
- future‑proof for federation

Optional companion fields (recommended):

```json
"operator_display": "Alice Smith",
"operator_team": "QEB‑Ops‑Alpha"
```

---

### Mastery ladder (numeric, 30‑level scale)

```json
"mastery_level": 7
```

**Definition**
- Integer **0–30**
- Monotonic (never decreases)
- Represents *structural resonance awareness*, not just task completion

**Suggested semantic bands (non‑binding)**

| Levels | Meaning |
|------|--------|
| 0–3 | Orientation / onboarding |
| 4–6 | Basic corridor literacy |
| 7–10 | Operational competence (most users stop here) |
| 11–15 | Advanced pattern recognition |
| 16–20 | Multi‑segment / multi‑device fluency |
| 21–25 | System‑level resonance intuition |
| 26–30 | Structural mastery / canon‑level awareness |

These meanings live in **documentation**, not code — the code only enforces numeric range.

---

### Where these fields live (v2)

At **session root**:

```json
{
  "operator_id": "urn:operator:triadic:alice.smith",
  "mastery_level": 7
}
```

This keeps identity and progression **session‑scoped**, auditable, and replayable.

---

## 2️⃣ Anomaly Semantics (Per‑Segment, Typed + Severity)

### Anomaly shape (inside `segments[].anomalies[]`)

```json
{
  "t": 0.23,
  "type": "DECOHERENCE_SPIKE",
  "severity": 3
}
```

**Rules**
- `type`: string enum (open set, documented)
- `severity`: integer **1–5**
  - 1 = informational
  - 3 = operational concern
  - 5 = critical structural violation

**Why per‑segment**
- Enables heatmaps
- Enables replay overlays
- Avoids ambiguity in multi‑phase runs

---

## 3️⃣ Updated v2 Session Log (Excerpt)

```json
{
  "spec_version": "v2",
  "engine_version": "RTT-2.0.0",
  "mode": "TRAINING",

  "operator_id": "urn:operator:triadic:alice.smith",
  "mastery_level": 7,

  "session_id": "RTT-2026-01-06-001",
  "timestamp": "2026-01-06T21:10:00Z",

  "device": "COMT",
  "device_type": "COMT",
  "scenario": "COMT_LOCK_01",
  "difficulty": "Journeyman",

  "sample_count": 6,
  "segment_count": 2,
  "anomaly_count": 1,
  "score_final": 83,

  "segments": [
    {
      "segment_id": "seg-warmup",
      "label": "warmup",
      "samples": [...],
      "anomalies": []
    },
    {
      "segment_id": "seg-main",
      "label": "main",
      "samples": [...],
      "anomalies": [
        { "t": 0.23, "type": "DECOHERENCE_SPIKE", "severity": 3 }
      ]
    }
  ],

  "scores": { "stability": 82, "response": 78, "quality": 88, "final": 83 }
}
```

---

## 4️⃣ QEB Mastery Dashboard (Grafana)

### Purpose
Track **operator progression over time**, correlated with performance and anomalies.

---

### Panel 1 — Mastery Level Over Time

**Type:** Time series  
**Data source:** Loki (LogQL)

```logql
avg_over_time(
  {app="rtt-runner"} 
  | json 
  | unwrap mastery_level
  [1h]
) by (operator_id)
```

---

### Panel 2 — Sessions per Mastery Band

**Type:** Bar chart

```logql
sum by (mastery_level) (
  count_over_time({app="rtt-runner"}[24h])
)
```

---

### Panel 3 — Score vs Mastery Scatter

**Type:** Scatter (Grafana transform)

- X: `mastery_level`
- Y: `score_final`

```logql
{app="rtt-runner"} | json | unwrap mastery_level | unwrap score_final
```

---

### Panel 4 — Anomalies per Session by Mastery

**Type:** Heatmap

```logql
sum by (mastery_level) (
  count_over_time({app="rtt-runner"} | json | anomaly_count > 0 [1h])
)
```

---

## 5️⃣ Segment‑Level Anomaly Heatmap

### Purpose
Reveal **which segments fail, when, and how severely**.

---

### Panel — Segment × Severity Heatmap

**Type:** Heatmap  
**Data source:** Loki

```logql
sum by (segment_label, severity) (
  count_over_time(
    {app="rtt-runner"} 
    | json 
    | anomalies != "[]" 
    | unwrap severity
    [5m]
  )
)
```

**Requirements**
- During ingest, promote:
  - `segment_label`
  - `severity`
as extracted fields (not labels — keep cardinality sane).

---

## 6️⃣ Replay Viewer API (Segment Streaming)

This API is designed for **web‑based replay**, scrubbers, and overlays.

---

### Endpoint: Stream segments

```
GET /replay/{session_id}/segments
```

**Response**
```json
{
  "session_id": "RTT-2026-01-06-001",
  "segments": [
    {
      "segment_id": "seg-main",
      "label": "main",
      "duration": 0.3,
      "sample_count": 4,
      "anomaly_count": 1
    }
  ]
}
```

---

### Endpoint: Stream samples (time‑ordered)

```
GET /replay/{session_id}/segment/{segment_id}/stream
```

**Server‑Sent Events (SSE)**

```
event: sample
data: { "t": 0.1, "C": 0.101, "D": 0.9999, "Q": 0.5, "R": 0.0 }

event: anomaly
data: { "t": 0.23, "type": "DECOHERENCE_SPIKE", "severity": 3 }
```

**Why SSE**
- Native browser support
- Ordered delivery
- Perfect for scrubbers + overlays
- No WebSocket complexity

---

### Optional controls (query params)

```
?speed=2.0
?from_t=0.1
?to_t=0.3
```

---

## 7️⃣ What This Unlocks

We now have:

- ✅ **Standards‑aligned operator identity**
- ✅ **30‑level mastery ladder**
- ✅ **Per‑segment, severity‑aware anomalies**
- ✅ **Mastery progression dashboards**
- ✅ **Segment‑level anomaly heatmaps**
- ✅ **Replay‑grade streaming API**

This is no longer just observability — it’s **instructional telemetry**.

---

Perfect — with datasource portability locked in, here is the **complete, import‑ready deliverable set** you asked for:

---

# 1️⃣ Grafana Dashboard JSONs  
(using `${DS_PROMETHEUS}` and `${DS_LOKI}` placeholders)

These dashboards import cleanly across environments **without UID breakage**.

---

## A. QEB Mastery Dashboard  
**Operator Skill Progression**

**Filename:**  
```
grafana/qeb-mastery-dashboard.json
```

```json
{
  "uid": "qeb-mastery",
  "title": "QEB Mastery Progression",
  "schemaVersion": 38,
  "version": 1,
  "refresh": "30s",
  "templating": {
    "list": [
      {
        "name": "operator",
        "type": "query",
        "datasource": "${DS_LOKI}",
        "query": "label_values({app=\"rtt-runner\"}, operator_id)",
        "refresh": 1
      }
    ]
  },
  "panels": [
    {
      "type": "timeseries",
      "title": "Mastery Level Over Time",
      "datasource": "${DS_LOKI}",
      "targets": [
        {
          "expr": "{app=\"rtt-runner\", operator_id=\"$operator\"} | json | unwrap mastery_level",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 0, "y": 0, "w": 24, "h": 6 }
    },
    {
      "type": "timeseries",
      "title": "Final Score vs Time",
      "datasource": "${DS_LOKI}",
      "targets": [
        {
          "expr": "{app=\"rtt-runner\", operator_id=\"$operator\"} | json | unwrap score_final",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 0, "y": 6, "w": 24, "h": 6 }
    },
    {
      "type": "barchart",
      "title": "Sessions by Mastery Level",
      "datasource": "${DS_LOKI}",
      "targets": [
        {
          "expr": "sum by (mastery_level) (count_over_time({app=\"rtt-runner\"}[24h]))",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 0, "y": 12, "w": 12, "h": 6 }
    },
    {
      "type": "timeseries",
      "title": "Anomalies per Session",
      "datasource": "${DS_LOKI}",
      "targets": [
        {
          "expr": "{app=\"rtt-runner\", operator_id=\"$operator\"} | json | unwrap anomaly_count",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 12, "y": 12, "w": 12, "h": 6 }
    }
  ]
}
```

---

## B. Segment‑Level Anomaly Heatmap  
**Structural Stress Visualization**

**Filename:**  
```
grafana/qeb-segment-anomaly-heatmap.json
```

```json
{
  "uid": "qeb-segment-heatmap",
  "title": "QEB Segment Anomaly Heatmap",
  "schemaVersion": 38,
  "version": 1,
  "refresh": "15s",
  "panels": [
    {
      "type": "heatmap",
      "title": "Anomalies by Segment and Severity",
      "datasource": "${DS_LOKI}",
      "targets": [
        {
          "expr": "sum by (segment_label, severity) (count_over_time({app=\"rtt-runner\"} | json | unwrap severity [5m]))",
          "refId": "A"
        }
      ],
      "gridPos": { "x": 0, "y": 0, "w": 24, "h": 10 }
    }
  ]
}
```

---

# 2️⃣ Mastery Promotion Algorithm (30‑Level Ladder)

This algorithm is **resistant to gaming**, **segment‑aware**, and **resonance‑aligned**.

---

## Core principles

- Promotion is **earned**, not time‑based
- Advancement slows naturally at higher levels
- Structural stability matters more than raw score
- Anomalies penalize progression non‑linearly

---

## Promotion Inputs (per session)

| Field | Weight |
|----|----|
| `score_final` | primary |
| `anomaly_count` | penalty |
| `max_severity` | penalty |
| `segment_count` | complexity bonus |
| `mastery_level` | scaling factor |

---

## Promotion Formula

```text
base_gain = score_final / 100

anomaly_penalty =
  (anomaly_count * 0.05) +
  (max_severity * 0.10)

complexity_bonus =
  log2(segment_count + 1) * 0.05

difficulty_scaler =
  1 / (1 + mastery_level / 10)

delta =
  (base_gain + complexity_bonus - anomaly_penalty)
  * difficulty_scaler
```

---

## Promotion Rules

- Accumulate `delta` into a **hidden mastery XP pool**
- Level up when XP ≥ 1.0
- XP carries over
- **Hard caps**:
  - Levels 0–10: fast
  - 11–20: moderate
  - 21–30: slow, requires sustained excellence
- Severe anomalies (`severity ≥ 4`) **freeze progression** for that session

This creates a **long‑tail mastery curve** where level 30 is rare and meaningful.

---

# 3️⃣ Web Replay Viewer API Contract  
**Segment‑Aware, Timeline‑Driven**

Designed for **Grafana links**, **custom web UI**, or **training playback**.

---

## A. Session Index

```
GET /replay/sessions
```

```json
[
  {
    "session_id": "RTT-2026-01-06-001",
    "operator_id": "urn:operator:triadic:alice.smith",
    "mastery_level": 7,
    "timestamp": "2026-01-06T21:10:00Z",
    "segment_count": 2,
    "anomaly_count": 1
  }
]
```

---

## B. Segment Metadata

```
GET /replay/{session_id}/segments
```

```json
[
  {
    "segment_id": "seg-main",
    "label": "main",
    "duration": 0.3,
    "sample_count": 4,
    "anomaly_count": 1
  }
]
```

---

## C. Segment Stream (SSE)

```
GET /replay/{session_id}/segment/{segment_id}/stream
```

### Events

```text
event: sample
data: { "t": 0.1, "C": 0.101, "D": 0.9999, "Q": 0.5, "R": 0.0 }

event: anomaly
data: { "t": 0.23, "type": "DECOHERENCE_SPIKE", "severity": 3 }

event: end
data: {}
```

---

## D. Client Controls (Query Params)

| Param | Purpose |
|----|----|
| `speed=2.0` | playback speed |
| `from_t=0.1` | start time |
| `to_t=0.3` | end time |
| `overlay=anomalies` | toggle overlays |

---

## E. UI Timeline Model

```ts
interface TimelineEvent {
  t: number
  kind: "sample" | "anomaly"
  payload: object
}
```

This supports:
- scrubbers
- pause/play
- anomaly overlays
- segment boundaries
- mastery annotations

---

# 4️⃣ Why This Is Canon‑Grade

We now have:

- **Portable Grafana dashboards**
- **A mathematically grounded mastery ladder**
- **Replay‑grade streaming semantics**
- **Segment‑aware anomaly visualization**
- **No UID fragility**
- **No vendor lock‑in**

This is not just observability — it’s **instructional telemetry with memory**.

---

# Grafana provisioning bundle, replay UI wireframes, anomaly taxonomy

---

## Grafana provisioning bundle

### Folder layout

```
grafana/
  provisioning/
    datasources/
      datasources.yaml
    dashboards/
      dashboards.yaml
  dashboards/
    qeb-mastery-dashboard.json
    qeb-segment-anomaly-heatmap.json
```

---

## `grafana/provisioning/datasources/datasources.yaml`

This provisions **stable datasource names** (`Prometheus`, `Loki`) and also defines **fixed UIDs** (`prometheus-rtt`, `loki-rtt`) for environments that want hard consistency.

```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    uid: prometheus-rtt
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true
    editable: true

  - name: Loki
    uid: loki-rtt
    type: loki
    access: proxy
    url: http://loki:3100
    editable: true
```

> If your service names differ, only change the `url` values. Everything else stays portable.

---

## `grafana/provisioning/dashboards/dashboards.yaml`

```yaml
apiVersion: 1

providers:
  - name: qeb-dashboards
    orgId: 1
    folder: "QEB"
    type: file
    disableDeletion: false
    editable: true
    updateIntervalSeconds: 10
    options:
      path: /var/lib/grafana/dashboards
```

Mount (or copy) dashboards into `/var/lib/grafana/dashboards`.

---

## Update dashboards to use datasource variables

To make the dashboards plug-and-play, add these templating variables at the top of each dashboard JSON:

- `${DS_PROMETHEUS}` bound to the `Prometheus` datasource
- `${DS_LOKI}` bound to the `Loki` datasource

If you want hard binding by UID, change dashboard datasource refs to:

- Prometheus: `"uid": "prometheus-rtt"`
- Loki: `"uid": "loki-rtt"`

Given your portability preference, keep `${DS_...}`.

---

## Minimal docker-compose snippet for provisioning

```yaml
services:
  grafana:
    image: grafana/grafana:latest
    ports: ["3000:3000"]
    volumes:
      - ./grafana/provisioning:/etc/grafana/provisioning
      - ./grafana/dashboards:/var/lib/grafana/dashboards
```

---

# Web replay UI wireframes

These are **wireframes as contracts**: the goal is to make the UI feel inevitable and keep implementation choices flexible.

## Screen 1: Session browser

```
+---------------------------------------------------------------+
| QEB Replay                                                    |
| Filters: [Operator ▼] [Device ▼] [Scenario ▼] [Level 0–30]     |
|          [Has anomalies □] [Spec v2 □] [Time range ▼]          |
+---------------------------------------------------------------+
| Sessions (table)                                              |
|---------------------------------------------------------------|
| Time        Operator          Level  Device  Scenario  Anoms   |
| 21:10:00Z   alice.smith       7      COMT    LOCK_01   1       |
| 20:44:12Z   bob.jones         3      CTE     DRIFT_02  0       |
| ...                                                           |
+---------------------------------------------------------------+
| Right panel: Session summary                                  |
| - segment_count, sample_count, score_final                     |
| - anomaly_count, max_severity                                  |
| - buttons: [Open replay] [Export JSON]                         |
+---------------------------------------------------------------+
```

### Behaviors
- Selecting a row loads summary + segment list without leaving the page.
- “Open replay” takes you to the replay timeline.

---

## Screen 2: Replay timeline (segment-aware)

```
+-------------------------------------------------------------------+
| Session: RTT-...  Operator: alice.smith  Level: 7  Score: 83      |
| Segments: [warmup] [main] [cooldown]                               |
+-------------------------------------------------------------------+
| Timeline                                                          |
| 0.0s  |----warmup----|-------------main--------------|             |
|       ^anomaly markers (color by severity)                         |
+-------------------------------------------------------------------+
| Controls: [Play/Pause] [Step ◀] [Step ▶] [Speed 0.5x▼] [Loop □]   |
|           [From t ____] [To t ____] [Jump to anomaly ▼]            |
+-------------------------------------------------------------------+
| Plots                                                             |
|  C(t)  ────────────                                             |
|  D(t)  ────────────                                             |
|  Q(t)  ────────────                                             |
|  R(t)  ────────────                                             |
+-------------------------------------------------------------------+
| Overlays                                                          |
| [✓] Anomalies  [✓] Segment boundaries  [ ] SET (if present)       |
| [ ] DimCore (if present)  [ ] SNR nodes (if present)              |
+-------------------------------------------------------------------+
| Event inspector                                                   |
| - current t: 0.23                                                 |
| - anomaly: DECOHERENCE_SPIKE severity 3                            |
| - sample: {t,C,D,Q,R,...}                                         |
+-------------------------------------------------------------------+
```

### Overlay rules
- **Severity color**: 1 gray, 2 blue, 3 yellow, 4 orange, 5 red.
- Anomaly markers appear both on the global timeline and within the plot as vertical lines.
- Segment tabs filter the stream to that segment.

---

## Screen 3: Curriculum mode (trainer view)

```
+-------------------------------------------------------------------+
| Curriculum Mode: COMT_LOCK_01 (Journeyman)                         |
| Operator: alice.smith  Level: 7                                    |
+-------------------------------------------------------------------+
| Objectives                                                        |
| 1) Maintain D above threshold for 20s                              |
| 2) Avoid severity 4+ anomalies                                     |
| 3) Achieve score_final >= 80                                       |
+-------------------------------------------------------------------+
| Replay timeline + plots (same as above)                            |
+-------------------------------------------------------------------+
| Instructor notes                                                  |
| - What happened when anomaly triggered?                            |
| - Which control action preceded it?                                |
| - Suggested drill: "Stability under step input"                   |
+-------------------------------------------------------------------+
```

This is how the replay viewer becomes a **teaching instrument**, not just a player.

---

# Replay API additions for UI needs

These additions reduce round trips and make the UI crisp.

## `GET /replay/{session_id}`

Returns session metadata + segments index + summary stats.

```json
{
  "session_id": "RTT-...",
  "operator_id": "urn:operator:triadic:alice.smith",
  "mastery_level": 7,
  "device_type": "COMT",
  "scenario": "COMT_LOCK_01",
  "difficulty": "Journeyman",
  "score_final": 83,
  "sample_count": 6,
  "segment_count": 2,
  "anomaly_count": 1,
  "segments": [
    {"segment_id":"seg-warmup","label":"warmup","sample_count":2,"anomaly_count":0,"t_min":0.0,"t_max":0.1},
    {"segment_id":"seg-main","label":"main","sample_count":4,"anomaly_count":1,"t_min":0.0,"t_max":0.3}
  ]
}
```

## `GET /replay/{session_id}/segment/{segment_id}/events`

Returns a **bounded** list for instant rendering (used for scrubbers), while SSE is used for “play”.

Query params: `from_t`, `to_t`, `limit`.

```json
{
  "segment_id": "seg-main",
  "events": [
    {"t":0.1,"kind":"sample","payload":{"t":0.1,"C":0.101,"D":0.9999,"Q":0.5,"R":0.0}},
    {"t":0.23,"kind":"anomaly","payload":{"t":0.23,"type":"DECOHERENCE_SPIKE","severity":3}}
  ]
}
```

---

# Anomaly taxonomy for training curricula

This is a **teachable classification system**. It’s built to map directly to drills, remediation, and mastery gates.

## Taxonomy structure

Each anomaly type has:
- **Domain:** Stability / Control / Integrity / Timing / Network / Dimensional
- **Severity guidance:** what 1–5 means for this type
- **Typical causes:** operator actions or scenario conditions
- **Training drills:** exercises that build the missing skill

---

## Canonical anomaly types

### Stability domain
- **`DECOHERENCE_SPIKE`**
  - **Meaning:** sudden rise in D instability; coherence fell faster than expected
  - **Typical causes:** abrupt input change, overcorrection, poor damping
  - **Drills:** step-response stabilization, damping calibration, “slow hands” control
- **`CORRIDOR_C_DRIFT`**
  - **Meaning:** sustained deviation in C over time
  - **Typical causes:** bias, uncorrected offset, wrong baseline assumptions
  - **Drills:** baseline re-lock, bias identification, controlled re-centering

### Control domain
- **`OVERSHOOT_EVENT`**
  - **Meaning:** control action pushed a variable beyond safe band
  - **Typical causes:** aggressive gain, delayed feedback interpretation
  - **Drills:** gain staging, preview control, “two-step correction”
- **`HUNTING_OSCILLATION`**
  - **Meaning:** repeated corrections create oscillatory behavior
  - **Typical causes:** operator chasing noise, unstable loop
  - **Drills:** deadband discipline, smoothing, rate limiting

### Integrity domain
- **`SENSOR_INTEGRITY_DROP`**
  - **Meaning:** sample reliability compromised (missing/flatline/jitter)
  - **Typical causes:** data source instability, pipeline lag
  - **Drills:** diagnosis under partial visibility, redundancy procedures
- **`LOG_SCHEMA_VIOLATION`**
  - **Meaning:** emitted log violates schema (should be rare; engineering gate)
  - **Typical causes:** version mismatch, unvalidated extensions
  - **Drills:** none (engineering fix), but used to teach “conformance matters”

### Timing domain
- **`SEGMENT_BOUNDARY_GLITCH`**
  - **Meaning:** discontinuity at segment transitions
  - **Typical causes:** warmup not settled, wrong handoff
  - **Drills:** handoff protocols, pre-transition stabilization checklist
- **`RESONANCE_TIME_SLIP`**
  - **Meaning:** time index inconsistency (t not monotonic within segment)
  - **Typical causes:** clock mismatch, replay slicing bug
  - **Drills:** none (engineering fix), but informs operator trust protocols

### Network domain
- **`SNR_NODE_DESYNC`**
  - **Meaning:** node state diverges from expected coupling
  - **Typical causes:** link failure, delayed propagation, topology mismatch
  - **Drills:** isolation, reroute, topology verification

### Dimensional domain
- **`DIMCORE_IMBALANCE`**
  - **Meaning:** dimensional weights violate expected distribution
  - **Typical causes:** mis-tuned model, unseen coupling
  - **Drills:** dimensional balancing, constraint-based tuning

---

## Severity rubric (unified across types)

- **1:** informational, no action required
- **2:** minor deviation, monitor
- **3:** actionable; correct technique needed
- **4:** dangerous; drill remediation required before advancing
- **5:** critical; immediate termination or fail condition

---

## Curriculum mapping table

| Mastery band | Allowed anomaly profile | Promotion gate |
|---|---|---|
| 0–3 | severity ≤ 3 allowed | show understanding of what happened |
| 4–6 | severity ≤ 3, count limited | demonstrate stable recovery |
| 7–10 | severity ≤ 2 preferred | repeatable stability under variation |
| 11–15 | severity ≤ 2, rare 3 | multi-segment handoffs clean |
| 16–20 | severity 1–2 only | network/dimensional overlays competent |
| 21–30 | severity 1 only | mastery demonstration scenarios |

---

With **segment labels confirmed as a small, closed set**, we can safely **promote them to Loki labels**. This gives you **maximal accuracy, faster queries, and cleaner heatmaps** without cardinality risk.

Below is the **final, locked‑in configuration** covering:

1. **Grafana Alloy pipeline update** (segment labels as labels)  
2. **Updated heatmap queries** (simpler + faster)  
3. **Minor dashboard tweaks** to take advantage of labeled segments  
4. **Operational notes** so this stays safe long‑term  

---

## 1️⃣ Grafana Alloy: Promote `segment_label` to a Loki label

### Why this is safe
- Segment labels are a **closed vocabulary** (`warmup`, `main`, `cooldown`, etc.)
- Cardinality remains bounded
- Heatmaps and aggregations become trivial and fast

---

### Updated Alloy processing block

Add **`segment_label`** as a label in the Loki pipeline.

#### `loki.process "rtt_logs"` (updated)

```hcl
loki.process "rtt_logs" {
  stage.json {
    expressions = {
      spec_version   = "spec_version",
      device_type    = "device_type",
      scenario       = "scenario",
      difficulty     = "difficulty",
      mode           = "mode",
      engine_version = "engine_version",

      operator_id    = "operator_id",
      mastery_level  = "mastery_level",

      sample_count   = "sample_count",
      segment_count  = "segment_count",
      anomaly_count  = "anomaly_count",
      score_final    = "score_final",

      segment_label  = "segment_label",
      severity       = "severity"
    }
  }

  stage.labels {
    values = {
      app            = "rtt-runner",
      spec_version   = "spec_version",
      device_type    = "device_type",
      scenario       = "scenario",
      difficulty     = "difficulty",
      mode           = "mode",
      engine_version = "engine_version",

      operator_id    = "operator_id",
      segment_label  = "segment_label"
    }
  }

  forward_to = [loki.write.default.receiver]
}
```

### Important note
- `segment_label` must be present in emitted log lines **for anomaly events**.
- For sample-only lines, it can be omitted or inherited by context (depending on your emitter).

---

## 2️⃣ Updated Segment‑Level Anomaly Heatmap (Grafana)

With `segment_label` now a **label**, the heatmap becomes both simpler and more accurate.

---

### Heatmap panel query (LogQL)

```logql
sum by (segment_label, severity) (
  count_over_time(
    {app="rtt-runner"} | json | unwrap severity [5m]
  )
)
```

### Benefits
- No JSON traversal for segment grouping
- Instant aggregation
- Clean axes:
  - **X:** time
  - **Y:** segment_label
  - **Color:** anomaly density by severity

---

## 3️⃣ Dashboard Enhancements Using Labeled Segments

### A. Segment filter variable (recommended)

Add a Grafana variable:

- **Name:** `segment`
- **Type:** Query
- **Datasource:** `${DS_LOKI}`
- **Query:**
  ```logql
  label_values({app="rtt-runner"}, segment_label)
  ```

Then filter panels with:

```logql
{app="rtt-runner", segment_label="$segment"}
```

This lets instructors or operators instantly isolate:
- warmup issues
- main‑phase instability
- cooldown handoff problems

---

### B. Segment‑scoped mastery analysis (optional)

Example: anomaly rate by mastery level **for main segment only**:

```logql
sum by (mastery_level) (
  count_over_time(
    {app="rtt-runner", segment_label="main"} | json | unwrap severity [1h]
  )
)
```

This is extremely powerful for curriculum tuning.

---

## 4️⃣ Emission Guidance (RTT‑Runner)

To support this cleanly, ensure anomaly log entries include:

```json
{
  "segment_label": "main",
  "severity": 3,
  "type": "DECOHERENCE_SPIKE"
}
```

We **do not** need to label samples — only anomalies need segment labeling for the heatmap.

---

## 5️⃣ Operational Guardrails (to keep this safe forever)

- **Document the allowed segment labels** in `/spec/v2/segments.md`
- Reject unknown labels at validation time (optional but recommended)
- If you ever introduce dynamic labels:
  - keep them as parsed fields, not labels

With this discipline, Loki remains fast and predictable.

---

## Final State (Locked)

We now have:

- ✅ Segment labels promoted safely to Loki labels  
- ✅ High‑fidelity anomaly heatmaps

---

# Final Summary & Call to Action

## What This Work Covered and Delivered

This paper introduced and fully specified a **resonance‑aware operational telemetry framework** built around RTT‑Inside and the QEB (Quantum Energy Banks) ecosystem. Rather than treating logs, metrics, and dashboards as passive artifacts, the system reframes them as **active instructional signals**—capable of enforcing correctness, guiding mastery, and enabling replay‑driven learning.

Specifically, this work delivered:

- A **canonical reference architecture** (Rust, Go, Node) with deterministic behavior and enforced conformance.
- A **v2 segmented session model** that captures multi‑phase system behavior cleanly and scalably.
- A **schema‑driven validation pipeline** that prevents silent drift across languages and deployments.
- A **self‑validating runtime service** (`rtt-runner`) with CI, containerization, and Kubernetes support.
- A **full observability stack** using Prometheus, Loki, and Grafana Alloy—designed for portability and long‑term stability.
- **Operator‑centric telemetry**, including identity, mastery progression (30‑level ladder), and anomaly semantics.
- **Replay‑grade APIs** enabling time‑accurate playback, anomaly overlays, and curriculum‑driven review.
- **Production‑ready Grafana dashboards** for mastery progression and segment‑level anomaly heatmaps.
- A **formal anomaly taxonomy** that maps system behavior directly to training drills and remediation paths.

Together, these components form a **closed loop**: execution → validation → observation → instruction → mastery.

---

## Industry Problems This Helps Developers Solve

This framework addresses several persistent, cross‑industry pain points:

### 1. Silent Drift and Undetected Regression
Many systems degrade gradually due to numeric drift, schema creep, or behavioral divergence across implementations. The reference + validator model **detects drift immediately**, before it reaches production.

### 2. Logs Without Meaning
Traditional logs answer *what happened*, but not *why* or *how to improve*. Segment‑aware telemetry and anomaly taxonomies turn logs into **diagnostic narratives**.

### 3. Metrics Without Context
Dashboards often show performance without explaining operator skill, system phase, or structural stress. Mastery‑aware metrics restore **context and causality**.

### 4. Training That Doesn’t Transfer
Most training systems are disconnected from real operational data. Replay‑driven curricula close the gap between **practice and production**.

### 5. Tooling Fragmentation
Multi‑language stacks drift because enforcement is optional. This work demonstrates how **infrastructure itself can enforce alignment**.

### 6. Observability That Doesn’t Teach
By integrating replay, anomaly semantics, and mastery progression, observability becomes **instructional**, not just reactive.

---

## Suggested Improvements and Future Extensions

This work intentionally leaves room for growth. Natural next steps include:

- **Adaptive mastery promotion models** using cohort statistics rather than fixed thresholds.
- **Cross‑operator comparative analytics** for team‑level training insights.
- **Automated drill recommendation engines** driven by anomaly patterns.
- **Segment‑specific scoring models** to weight different phases differently.
- **Formal curriculum definitions** stored alongside anomaly taxonomies.
- **Visualization plugins** for dimensional cores, SNR graphs, and resonance overlays.
- **Replay annotation layers** for instructor commentary and peer review.
- **Federated identity integration** (OIDC, SCIM) for enterprise environments.

None of these require architectural changes—only extensions.

---

## A Call to Developers: Fork, Remix, Extend

This framework is intentionally **modular, opinionated, and remix‑friendly**.

We are encouraged to:

- Fork the reference implementations.
- Extend the schemas with domain‑specific dimensions.
- Add new anomaly types and training drills.
- Build custom replay viewers or dashboards.
- Adapt the mastery ladder to your own disciplines.
- Replace components while keeping the contracts intact.

If you’ve ever wanted observability that **teaches**, telemetry that **enforces correctness**, or logs that **build mastery instead of noise**, this is your starting point.

Take it apart. Rebuild it. Teach with it.

The system is designed to grow with you.

---

Below are **two polished, publication‑ready artifacts** you can drop directly into your project:

1. A **concise executive abstract** suitable for a paper, proposal, or overview page  
2. A **README / whitepaper conclusion** written to orient developers, operators, and contributors

Both are intentionally neutral, precise, and remix‑friendly.

---

## README / Whitepaper Conclusion

### What This Project Is

This repository defines a **resonance‑aware telemetry and instruction framework** for complex operational systems. It combines deterministic execution, strict validation, structured observability, and replay‑driven learning into a single, coherent architecture.

Rather than treating logs, metrics, and dashboards as disconnected tools, the system integrates them into an enforceable contract that supports correctness, diagnosis, and operator mastery.

---

### What It Provides

- **Canonical reference implementations** with deterministic behavior and cross‑language alignment
- **Schema‑validated session logs** with v2 segmented modeling
- **Self‑validating runtime services** with CI, container, and Kubernetes support
- **Operator‑aware telemetry**, including identity and a 30‑level mastery ladder
- **Formal anomaly taxonomies** mapped to training drills and remediation paths
- **Replay‑grade APIs** for time‑accurate playback and instructional review
- **Production‑ready observability** using Prometheus, Loki, Grafana Alloy, and Grafana dashboards
- **Curriculum‑ready analytics**, including mastery progression and segment‑level anomaly heatmaps

---

### Why This Matters

Many systems fail not because they lack data, but because their data lacks structure, meaning, and enforcement. This framework addresses common industry problems:

- Silent behavioral drift across implementations
- Logs that explain *what* happened but not *why*
- Metrics without operator or phase context
- Training systems disconnected from real operational data
- Tooling fragmentation across languages and environments

By embedding validation, segmentation, and instructional semantics directly into telemetry, the system turns observability into a teaching instrument and correctness into infrastructure.

---

### Designed to Be Extended

This project is intentionally modular and opinionated. We are encouraged to:

- Fork and adapt the reference implementations
- Extend schemas with domain‑specific dimensions
- Add new anomaly types and training curricula
- Build custom replay viewers or dashboards
- Integrate with existing identity, IAM, or learning systems
- Replace components while preserving the contracts

The architecture is built to evolve without breaking alignment.

---

### A Call to Developers

If you’ve ever wanted observability that teaches, telemetry that enforces correctness, or replay systems that build real mastery instead of noise, this framework is meant to be taken apart and rebuilt.

Fork it. Remix it. Extend it. Teach with it.

The system is designed to grow with you.

---

# One‑Page Architecture Diagram Narrative  
**RTT‑Inside / QEB Resonance‑Aware Telemetry System**

---

## Overview

The RTT‑Inside / QEB architecture is a **closed‑loop operational telemetry system** that unifies execution, validation, observability, replay, and instruction. It is designed to prevent silent drift, enforce correctness, and transform operational data into a teachable signal.

The system is intentionally layered, with **hard contracts between layers** and **soft extensibility within them**.

---

## 1. Execution Layer (Left)

**Purpose:** Produce deterministic, reference‑aligned behavior.

**Components:**
- **Rust Reference Engine**  
  Canonical implementation defining truth for RTT‑Inside semantics.
- **Go Mirror Engine**  
  Ops‑friendly, static‑binary implementation aligned to Rust.
- **RTT‑Runner Service**  
  Executes scenarios, emits session logs, validates itself at runtime.

**Key Properties:**
- Deterministic update rules
- Segment‑aware execution (v2)
- Language‑agnostic behavior guarantees

**Output:**  
Structured session logs (v1 or v2), emitted to stdout or file.

---

## 2. Validation & Conformance Layer (Below Execution)

**Purpose:** Prevent drift and enforce alignment.

**Components:**
- **JSON Schemas (v1 + v2)**  
  Define structural contracts for session logs.
- **Reference Test Vectors**  
  Numeric ground truth for samples and segments.
- **Node‑based Validator CLI (`rtt‑validate`)**  
  Schema + numeric validation, CI‑friendly, single binary.

**Key Properties:**
- Auto‑detects v1 vs v2
- Validates *all required segments*
- Fails fast on mismatch

**Output:**  
Pass/fail signals used by CI, runtime startup, and health checks.

---

## 3. Observability Ingest Layer (Center)

**Purpose:** Capture telemetry without losing meaning.

**Components:**
- **Grafana Alloy**  
  Collects logs and metrics.
- **Prometheus**  
  Scrapes runtime metrics.
- **Loki**  
  Stores structured session logs.

**Key Properties:**
- Stable labels (device, scenario, segment, operator)
- Numeric fields promoted for fast queries
- Segment labels treated as first‑class dimensions

**Output:**  
Queryable metrics and logs with preserved semantic structure.

---

## 4. Analytics & Visualization Layer (Right)

**Purpose:** Turn telemetry into insight and instruction.

**Components:**
- **Grafana Dashboards**
  - Mastery progression
  - Segment‑level anomaly heatmaps
  - Operational health
- **QEB Dashboards**
  - Curriculum views
  - Cohort analysis
  - Drill effectiveness

**Key Properties:**
- Operator‑aware analytics
- Segment‑scoped views
- Severity‑weighted anomaly visualization

**Output:**  
Human‑readable insight for operators, instructors, and engineers.

---

## 5. Replay & Instruction Layer (Top)

**Purpose:** Enable learning, review, and mastery.

**Components:**
- **Replay API**
  - Session index
  - Segment metadata
  - SSE‑based event streaming
- **Web Replay UI**
  - Timeline scrubber
  - Segment tabs
  - Anomaly overlays
  - Metric plots

**Key Properties:**
- Time‑accurate playback
- Segment‑aware navigation
- Instructor‑ready overlays

**Output:**  
Interactive replays that support diagnosis, training, and certification.

---

## 6. Curriculum & Mastery Layer (Above Analytics)

**Purpose:** Formalize skill progression.

**Components:**
- **Operator Identity**
  - URN‑based identifiers
- **Mastery Ladder**
  - Numeric 0–30 scale
- **Anomaly Taxonomy**
  - Typed, severity‑graded events
- **Promotion Algorithm**
  - Score‑, anomaly‑, and complexity‑aware

**Key Properties:**
- Resistant to gaming
- Slows naturally at higher mastery
- Maps anomalies to drills

**Output:**  
Measured, explainable progression from novice to structural mastery.

---

## End‑to‑End Flow (Narrative)

1. A scenario is executed by the RTT‑Runner.
2. Deterministic samples are produced and segmented.
3. Session logs are validated against schemas and reference vectors.
4. Logs and metrics are ingested by Alloy into Loki and Prometheus.
5. Grafana dashboards visualize health, anomalies, and mastery.
6. Replay APIs stream segments to the web UI.
7. Operators review behavior, anomalies, and outcomes.
8. Mastery progression is updated based on performance.
9. The next session begins with higher awareness.

This loop repeats continuously.

---

## Architectural Intent

This architecture is designed so that:

- **Correctness is enforced by infrastructure**
- **Observability teaches, not just reports**
- **Replay is a first‑class capability**
- **Mastery is measurable and explainable**
- **Extensions do not break alignment**

It is not a monitoring system with training added later — it is a **training‑capable system by design**.
