@echo off
echo Creating
echo . > module.json
echo . > operators.md
md regimes
cd regimes
echo . > us_federal.md
md us_state
cd us_state
echo . > texas.md
echo . > california.md
echo . > new_york.md
cd..
md international
cd international
echo . > eu.md
echo . > apac.md
echo . > latam.md
echo . > mena.md
cd..
echo . > crypto.md
cd..
md examples
cd examples
echo . > datacenter_tax_profile.md
echo . > cross_domain_tax_propagation.md
echo . > rtt_taxes_applied_to_infrastructure.md
cd..
md integration
cd integration
echo . > external_regime_integration.md
echo . > taxes_ie_gsm_cross_module_map.md
echo . > taxes_rrr_alignment.md
cd..
md maps
cd maps
echo . > cross_domain_propagation_map.md
echo . > temporal_resonance_map.md
echo . > incentive_regime_map.md
cd..