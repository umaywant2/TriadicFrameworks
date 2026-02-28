@echo off
echo Creating...
copy con README.md
md awareness_model
cd awareness_model
copy con overview.md
copy con local_signals.md
copy con server_signals.md
copy con merge_logic.md
copy con state_machine.md
cd..
md api
cd api
copy con awareness_endpoint.md
copy con caching_rules.md
copy con error_handling.md
cd..
md ui
cd ui
copy con indicator_design.md
copy con state_transitions.md
copy con portal_to_rtt.md
cd..
md implementation
cd implementation
copy con ios.md
copy con android.md
copy con shared_logic.md
cd..
md release
cd release
copy con v1_scope.md
copy con v1_limitations.md
copy con roadmap_v2_inside.md
