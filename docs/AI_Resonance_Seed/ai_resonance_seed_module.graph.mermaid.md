graph TD

    %% Orientation
    README["README.md"]
    PRIMER["primer.md"]
    HOWTO["how_to_read.md"]

    %% Substrate + Primitives
    SUBSTRATE["minimal_substrate.md"]
    INVARIANTS["invariants.yaml"]
    PRIMITIVES["resonance_time_primitives.yaml"]

    %% Schemas + Emitters
    SCHEMAS["schemas/"]
    EMITTERS["emitters/"]

    %% Validator + Lineage + Dashboards + Migration
    VALIDATOR["validator.md"]
    LINEAGE["lineage.md"]
    DASHBOARDS["dashboards/"]
    MIGRATION["migration.md"]

    %% Edges (Dependency Flow)
    README --> PRIMER
    PRIMER --> HOWTO
    HOWTO --> SUBSTRATE
    SUBSTRATE --> INVARIANTS
    INVARIANTS --> PRIMITIVES
    PRIMITIVES --> SCHEMAS
    SCHEMAS --> EMITTERS
    EMITTERS --> VALIDATOR
    VALIDATOR --> LINEAGE
    LINEAGE --> DASHBOARDS
    DASHBOARDS --> MIGRATION
