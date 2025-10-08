# TFThooks Validators

The **validators** folder contains test harnesses and validation scripts for hooks.  
Every hook must pass validation before being added to the registry.

## Examples
- `hook_schema_validator.py` → ensures hook configs follow schema
- `runtime_safety_check.py` → checks hooks for safe execution
- `integration_test_runner.py` → runs integration tests

## Purpose
Validators are the **safety net** of TFThooks.  
They ensure every extension is stable, reproducible, and remix‑ready.
