# `.well-known` — Public Service Metadata Surface

The **`.well-known`** directory contains all machine‑readable service descriptors, capability manifests, authentication metadata, and agent‑skill definitions that external systems use to discover, authenticate, and interact with TriadicFrameworks.

This folder is the **public contract layer** of the TriadicFrameworks ecosystem.  
Everything here is designed for automated consumption by:

- Cloudflare Workers & Agent Skills  
- WebMCP and OpenLoop runtimes  
- OAuth 2.0 / OpenID Connect clients  
- Web bots and authenticated crawlers  
- External AI agents  
- Service registries and security scanners  

Human readers rarely need to modify these files directly; they define how TriadicFrameworks presents itself to the outside world.

---

## Purpose of the Folder

This directory provides:

- **Identity metadata** for agents, bots, and services  
- **Authentication endpoints** (OAuth, OpenID, token/refresh)  
- **Cryptographic material** (JWKS, HTTP signature keys)  
- **Capability catalogs** (API catalog, module configs)  
- **Agent Skill definitions** for Cloudflare’s Agent Skills RFC  
- **Machine-readable service cards** for MCP and WebMCP  
- **Security disclosures** (`security.txt`)  

Together, these files form the **service perimeter** of TriadicFrameworks.

---

## Folder Structure Overview

### 🔐 Authentication & Identity

- **Auth.md** — Human-readable overview of authentication flows.  
- **auth/refresh** — Refresh token endpoint configuration.  
- **auth/token** — Token issuance endpoint configuration.  
- **oauth-authorization-server** — OAuth 2.0 authorization server metadata.  
- **oauth-protected-resource** — Protected resource configuration.  
- **openid-configuration** — OpenID Connect discovery document.  
- **jwks.json** — JSON Web Key Set for signature verification.  
- **http-message-signatures-directory** — HTTP message signature keys and metadata.

### 🤖 Agent & Bot Metadata

- **agent.json** — Primary agent descriptor for TriadicFrameworks.  
- **agent-card.json** — Machine-readable agent identity card.  
- **web-bot-auth.json** — Bot authentication configuration.  
- **webmcp.json** — WebMCP server and skill configuration.

### 📚 API & Module Catalogs

- **api-catalog** — Service documentation links and API registry.  
- **modules/index.json** — Module registry index.  
- **modules/quad-engine.json** — Quad Engine module configuration.  
- **modules/rtt.json** — RTT module configuration.  
- **modules/triadic-gravity.json** — Triadic Gravity module configuration.

### 🧠 Agent Skills (Cloudflare)

Located under `agent-skills/`, each skill exposes a structured capability:

- **coherence-layers**  
- **link-headers**  
- **mcp**  
- **openloop**  
- **quad-engine**  
- **rtt-operators**  
- **tft3pack**  
- **triadic-gravity**  
- **triadic-modules**  
- **web-bot-auth**

Each skill folder contains:

- `SKILL.md` — Capability definition  
- Optional `index.md` — Human-readable overview  

These skills allow external agents to navigate, query, and operate TriadicFrameworks using standardized discovery mechanisms.

### 🛡 Security & Disclosure

- **security.txt** — Public security contact and disclosure policy.

---

## How This Folder Fits into the Canon

In TriadicFrameworks, `.well-known` is part of the **Infrastructure Layer**:

- It is **not** a conceptual module.  
- It is **not** part of the Book or the pedagogical canon.  
- It is **not** an operator grammar or regime layer.

Instead, it is the **machine interface** that allows the canon to be:

- discoverable  
- authenticatable  
- verifiable  
- interoperable  
- agent‑accessible  

This folder is essential for **AI agent integration**, **service federation**, and **secure external access**.

---

## Contribution Guidelines

When modifying files in this directory:

- Maintain **strict JSON validity** for all machine-readable files.  
- Follow **Cloudflare Agent Skills RFC** for skill definitions.  
- Keep **OAuth/OpenID fields compliant** with their respective specifications.  
- Update **api-catalog** when adding or relocating service documentation.  
- Ensure **JWKS** and signature directories remain consistent with active keys.  
- Avoid breaking **discovery endpoints** used by external agents.  
- Treat this folder as **public infrastructure**, not internal documentation.

---

## Status

The `.well-known` directory is actively maintained and updated as new services, modules, and agent capabilities are added to TriadicFrameworks.  
Recent updates include API catalog improvements, OAuth configuration refinements, and expanded Agent Skills (  [github.com](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/.well-known)).
