@echo off
echo Creating...
echo . > index.html
echo . > module.json

md kernel
cd kernel
echo . > fft.ai.reader.json
echo . > fft.ai.coherence.json
echo . > fft.ai.drift.monitor.json
echo . > fft.ai.paradox.enum.json
echo . > fft.ai.paradox.resolver.json
echo . > fft.ai.session.context.html
cd..

md operators
cd operators
echo . > IS-Delta.json 
echo . > IS-Omega.json 
echo . > IS-Gradient.json 
echo . > IS-Silence.json 
echo . > IS-ReversalCross.json 
echo . > IS-PhaseMap.json 
cd..

md phases
cd phases 
echo . > rise.md
echo . > saturation.md
echo . > fracture.md
echo . > inversion.md
echo . > collapse.md
echo . > dissolution.md
echo . > silence.md
cd..

md maps
cd maps
echo . > inversion_cycle.json
echo . > operator_dominance.json
echo . > triadic_alignment_flip.json
cd..

md invariants
cd invariants
echo . > inverted_star.invariants.json
cd..

md qmroot
cd qmroot
echo . > qmroot.absence.json
echo . > INV-013.path.json
cd..

md examples
cd examples
echo . > inversion_trace.md
echo . > collapse_sequence.md
cd..

md assets
cd assets
md diagrams
cd diagrams
echo . > inverted_star_cycle.svg
echo . > operator_layers.svg
echo . > silence_boundary.svg
cd..
md css
cd css
echo . > ai-edition.css
