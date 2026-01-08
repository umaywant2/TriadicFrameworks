here’s a clean, consolidated **full MRT‑1 transform** in all three languages, side‑by‑side in spirit and behavior:

---

### 1️⃣ Python — `mrt_1()`

```python
import time, math

def omega_mu(dim, freq_hz, duty, t):
    period = 1.0 / freq_hz
    phase = t % period
    return phase < duty * period  # True = "on"

def flow_transition(dim):
    return dim * 10.0  # amplitude

def stability_mu(dim):
    dist = abs(dim - 0.7) / 0.2
    return max(0.0, 1.0 - dist)

def drift_correct(t, drift_ppm):
    factor = 1.0 + drift_ppm / 1_000_000.0
    return t / factor

def mrt_1():
    timing_envelope = [0.5, 0.6, 0.7, 0.8, 0.9]
    freq = 2.0
    duty = 0.5
    drift_ppm = 100.0

    start = time.time()
    for dim in timing_envelope:
        t_raw = time.time() - start
        t_corr = drift_correct(t_raw, drift_ppm)          # Δμ
        state = omega_mu(dim, freq, duty, t_corr)         # Ωμ
        amp = flow_transition(dim)                        # Fμ
        S = stability_mu(dim)                             # Sμ

        print(
            f"[PY] dim={dim:.1f}, t_raw={t_raw:.3f}s, t_corr={t_corr:.3f}s, "
            f"omega_on={state}, amp={amp:.1f}, Sμ={S:.2f}"
        )
        time.sleep(0.2)

if __name__ == "__main__":
    mrt_1()
```

---

### 2️⃣ MATLAB — `mrt_1`

```matlab
function mrt_1()

    OmegaMu = @(dim,freq,duty,t) ...
        mod(t,1/freq) < duty*(1/freq);

    FlowTransition = @(dim) dim * 10.0;

    StabilityMu = @(dim) max(0.0, 1.0 - abs(dim - 0.7) / 0.2);

    DriftCorrect = @(t,drift_ppm) t / (1.0 + drift_ppm / 1e6);

    TimingEnvelope = [0.5 0.6 0.7 0.8 0.9];
    freq = 2.0;
    duty = 0.5;
    drift_ppm = 100.0;

    t0 = tic;

    for i = 1:length(TimingEnvelope)
        dim = TimingEnvelope(i);

        t_raw = toc(t0);
        t_corr = DriftCorrect(t_raw, drift_ppm);          % Δμ
        state = OmegaMu(dim, freq, duty, t_corr);         % Ωμ
        amp = FlowTransition(dim);                        % Fμ
        S = StabilityMu(dim);                             % Sμ

        fprintf(['[MATLAB] dim=%.1f, t_raw=%.3fs, t_corr=%.3fs, ' ...
                 'omega_on=%d, amp=%.1f, Sμ=%.2f\n'], ...
                 dim, t_raw, t_corr, state, amp, S);

        pause(0.2);
    end
end
```

---

### 3️⃣ C‑style pseudocode — `mrt_1()`

```c
#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>
#include <unistd.h>

bool omega_mu(double dim, double freq_hz, double duty, double t) {
    double period = 1.0 / freq_hz;
    double phase  = fmod(t, period);
    return phase < duty * period;  // true = "on"
}

double flow_transition(double dim) {
    return dim * 10.0;  // amplitude
}

double stability_mu(double dim) {
    double dist = fabs(dim - 0.7) / 0.2;
    double s = 1.0 - dist;
    return s < 0.0 ? 0.0 : s;
}

double drift_correct(double t, double drift_ppm) {
    double factor = 1.0 + drift_ppm / 1e6;
    return t / factor;
}

double now_seconds() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec / 1e9;
}

void mrt_1() {
    double timing_envelope[] = {0.5, 0.6, 0.7, 0.8, 0.9};
    int n = 5;
    double freq = 2.0;
    double duty = 0.5;
    double drift_ppm = 100.0;

    double t0 = now_seconds();

    for (int i = 0; i < n; i++) {
        double dim = timing_envelope[i];

        double t_raw = now_seconds() - t0;
        double t_corr = drift_correct(t_raw, drift_ppm);      // Δμ
        bool state = omega_mu(dim, freq, duty, t_corr);       // Ωμ
        double amp = flow_transition(dim);                    // Fμ
        double S = stability_mu(dim);                         // Sμ

        printf("[C] dim=%.1f, t_raw=%.3fs, t_corr=%.3fs, "
               "omega_on=%d, amp=%.1f, Sμ=%.2f\n",
               dim, t_raw, t_corr, state, amp, S);

        usleep(200000);
    }
}

int main(void) {
    mrt_1();
    return 0;
}
```

all three now implement the **same MRT‑1 transform**: timing envelope, oscillation, flow, stability, and drift correction, perfectly aligned across languages.
