# TFT File Format (.fff)

The `.fff` file format defines the structure of TriadicFrameworks resonance files.  
These files describe:

- Resonant-time values (`τ_r`)
- Triadic operators (`D3`, `D6`, `D9`)
- Frequency elevation (`T_f`)
- Temperature coupling (`ΛΘ`)
- Composite constants (`X = F3 * T_f`)
- Optional metadata and comments

## Structure

A valid `.fff` file contains:

```code
[TFT]
version = 1.3
tau_r = <float>
D3 = <float>
D6 = <float>
D9 = <float>
Tf = <float>
LambdaTheta = <float>
F3 = <float>

Optional:

description = "Human readable notes"
tags = "comma,separated,keywords"
```

## Example

```code
[TFT]
version = 1.3
tau_r = 2.4
D3 = 3
D6 = 6
D9 = 9
Tf = 1.2
LambdaTheta = 0.8
F3 = 1.0
description = "Sample resonance file"
```

## Purpose

`.fff` files are used by:

- `run_tft.sh` — execution  
- `validate_tft.sh` — structural checks  
- `convert_tft.sh` — readable summaries  
- `batch_process.sh` — multi-file workflows  

They serve as the core data format for all TFT_3Pack examples.