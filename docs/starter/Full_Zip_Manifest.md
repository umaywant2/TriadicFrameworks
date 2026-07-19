# **RTT Starter Kit — Full .zip Manifest**

- [`RTT_Starter_Full.zip`](RTT_Starter_Full.zip)— Agentic RTT Starter Kit

```
rtt-starter-kit/
│
├── README.md
├── Full_Zip_Manifest.md
│
├── rtt/
│   ├── cheat-sheet.md
│   ├── index.md
│   ├── instructor-overview.md
│   ├── quick-reference.md
│   ├── _sidebar.md
│   │
│   ├── 1/
│   │   ├── README.md
│   │   └── rtt1.md
│   ├── 2/
│   │   ├── README.md
│   │   └── rtt2.md
│   └── 3/
│       ├── README.md
│       └── rtt3.md
│
├── modules/
│   ├── starter/
│   │   ├── README.md
│   │   ├── module.json
│   │   └── example-operator.md
│   │
│   └── templates/
│       ├── module.blank.json
│       ├── module.example.json
│       └── module.rtt-ready.json
│
├── schema/
│   └── module.schema.json
│
├── tools/
│   ├── validate.py
│   ├── validate.js
│   └── README.md
│
└── docs/
    ├── index.md
    ├── HOWTO.md
    ├── We_Didnt_Start_RTT__remix.md
    ├── Cold_as_Ice__RTT_parody.md
    ├── THE_FRAMEBREAKER—RTT_Metal_Parody_Original.md
    └── github-setup.md
```

---

# **Section‑by‑Section Breakdown**

## **Root**
- `README.md` — overview of the Starter Kit

---

## **/rtt/**
Student editions of RTT/1, RTT/2, RTT/3.

Each folder contains:
- `README.md` — short intro  
- `rttX.md` — the student‑edition content  

---

## **/modules/**
Where students build their modules.

### **/modules/starter/**
A fully working example module:
- `README.md`  
- `module.json`  
- `example-operator.md`  

### **/modules/templates/**
Three canonical templates:
- `module.blank.json`  
- `module.example.json`  
- `module.rtt-ready.json`  

---

## **/schema/**
- `module.schema.json` — the canonical schema

---

## **/tools/**
Validator scripts + instructions:
- `validate.py`  
- `validate.js`  
- `README.md`  

---

## **/docs/**
Student‑facing documentation:
- `index.md` — landing page  
- `HOWTO.md` — 1‑page module creation guide  
- `github-setup.md` — publishing instructions  

---

# **Packaging Notes**
The `.zip` should contain **exactly** the structure above — no hidden files, no OS metadata, no editor folders.

Ideal packaging command (conceptually):

```
zip -r rtt-starter-kit.zip rtt-starter-kit/
```

This ensures deterministic structure for students and agents.
