# Using the Schemas

Schemas define the structure, constraints, and relationships of data used throughout the Resonance Substrate Model. This document explains how to load, validate, and work with these schemas in external tools or applications.

---

## 1. Purpose of the Schemas
Schemas ensure:
- consistent field definitions  
- reproducible simulation configurations  
- standardized experiment metadata  
- compatibility across layers and modules  

---

## 2. Loading Schemas
Schemas are typically stored as JSON or YAML files and can be loaded using standard parsing libraries.

Example workflow:
1. load schema file  
2. validate configuration against schema  
3. construct substrate objects from validated data  

---

## 3. Validation
Validation ensures:
- required fields are present  
- field types match expectations  
- operator parameters fall within allowed ranges  

Validation errors should be treated as configuration issues rather than runtime failures.

---

## 4. Extending Schemas
Schemas can be extended to support:
- new operators  
- custom experiment types  
- additional metadata fields  
- domain-specific configurations  

Extensions should maintain backward compatibility whenever possible.

