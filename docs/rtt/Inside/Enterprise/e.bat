@echo off
echo Creating...
echo . > module.json
echo . > README.md
md identity_substrate
cd identity_substrate
echo . > README.md
md 0_local
cd 0_local
echo . > README.md
cd..
md 1_active_directory
cd 1_active_directory
echo . > README.md
cd..
md 2_ldap
cd 2_ldap
echo . > README.md
cd..
md 3_dns_srv
cd 3_dns_srv
echo . > README.md
cd..
md 4_kerberos
cd 4_kerberos
echo . > README.md
cd..
md 5_service_discovery
cd 5_service_discovery
echo . > README.md
cd..
md 6_modern_identity
cd 6_modern_identity
echo . > README.md
cd..
md 7_cloud_directory
cd 7_cloud_directory
echo . > README.md
cd..
md 8_zero_trust
cd 8_zero_trust
echo . > README.md
cd..
cd..
md substrate_extensions
cd substrate_extensions
echo . > README.md
md clarity
cd clarity
echo . > README.md
cd..
md regime
cd regime
echo . > README.md
cd..
md triad_roles
cd triad_roles
echo . > README.md
cd..
md coherence_envelopes
cd coherence_envelopes
echo . > README.md
cd..
md examples
cd examples
echo . > README.md
md minimal_enterprise
cd minimal_enterprise
echo . > README.md
cd..
md identity_flow
cd identity_flow
echo . > README.md
cd..
md substrate_negotiation
cd substrate_negotiation
echo . > README.md
cd..
cd..