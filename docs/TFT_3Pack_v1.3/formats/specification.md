\# TFT File Format Specification (.fff)



The `.fff` file format defines the structure of TriadicFrameworks resonance files.  

These files describe:



\- Resonant-time values (`τ\_r`)

\- Triadic operators (`D3`, `D6`, `D9`)

\- Frequency elevation (`T\_f`)

\- Temperature coupling (`ΛΘ`)

\- Composite constants (`X = F3 \* T\_f`)

\- Optional metadata and comments



\## Structure



A valid `.fff` file contains:



```code

\[TFT]

version = 1.3

tau\_r = <float>

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



\## Example



```code

\[TFT]

version = 1.3

tau\_r = 2.4

D3 = 3

D6 = 6

D9 = 9

Tf = 1.2

LambdaTheta = 0.8

F3 = 1.0

description = "Sample resonance file"

```



\## Purpose



`.fff` files are used by:



\- `run\_tft.sh` — execution  

\- `validate\_tft.sh` — structural checks  

\- `convert\_tft.sh` — readable summaries  

\- `batch\_process.sh` — multi-file workflows  



They serve as the core data format for all TFT\_3Pack examples.

