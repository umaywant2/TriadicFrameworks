@echo off
echo Creating...

set bot=chess
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > stockfish_shim.md
echo . > leela_shim.md
cd..

set bot=go
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
echo . > katago_shim.md
echo . > leela_zero_shim.md
cd..

set bot=poker
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > openholdem_shim.md
echo . > generic_poker_shim.md
cd..

set bot=tic_tac_toe
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > basic_shim.md
cd..

set bot=backgammon
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > gnu_bg_shim.md
echo . > generic_bg_shim.md
cd..

set bot=checkers
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > generic_checkers_shim.md
cd..

set bot=mee6
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > mee6_shim.md
cd..

set bot=rythm
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > rythm_shim.md
cd..

set bot=groovy
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > groovy_shim.md
cd..

set bot=dyno
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > dyno_shim.md
cd..

set bot=carl-bot
cd %bot%
md logic
cd logic
echo . > notes.md
cd..
md rtt
cd rtt
echo . > lumen.md
echo . > hephaestus.md
echo . > aurion.md
echo . > harmonia.md
cd..
md examples
cd examples
echo . > rtt_%bot%_examples.md
cd..
md analysis
cd analysis
echo . > regime_maps.md
echo . > resonance_fields.md
cd..
md shim
cd shim
echo . > carl_bot_shim.md
cd..
