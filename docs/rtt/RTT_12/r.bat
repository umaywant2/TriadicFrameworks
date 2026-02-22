@echo off
echo Creating...
rem /docs/rtt/RTT_12/
copy con README.md
copy con overview.md
copy con harmonic_ladder.md
md operators
cd operators
copy con G1.md
copy con G2.md
copy con G3.md
cd..
md triads
cd triads
copy con structural_triads.md
copy con harmonic_triads.md
copy con coherence_rules.md
cd..
md mapping
cd mapping
copy con structural_to_harmonic.md
copy con harmonic_to_structural.md
copy con triad_mapping.md
cd..
md notation
cd notation
copy con notation_standards.md
cd..
md validation
cd validation
copy con theoretical.md
copy con computational.md
copy con sector_specific.md
copy con experimental.md
copy con peer_review.md
copy con industry.md
cd..
md contributors
cd contributors
copy con guidelines.md
copy con versioning.md
cd..
md future
cd future
copy con extensions.md
cd..
