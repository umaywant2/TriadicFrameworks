# ☁️ Azure Deployment Guide: TFT Agent Shell

This guide walks you through deploying TFT agents on Azure using Kubernetes and autoscaling logic.

---

## 🧭 Steps

1. **Build Docker Image**
   ```bash
   docker build -t nawder/tft-agent .
   docker push nawder/tft-agent:latest
   ```
2. **Apply Deployment**
   ```bash
   kubectl apply -f azure_deploy.yaml
   ```
3. **Enable Autoscaling**
   ```bash
   kubectl autoscale deployment tft-agent-shell \
    --cpu-percent=69 \
    --min=1 \
    --max=99
   ```
4. **Monitor Logs**
  ```bash
  kubectl logs -f <pod-name>
  ```

---

## 🧪 Benchmark Goals
- Run THOR-style integral tests
- Log symbolic fidelity and remix lineage
- Visualize glyphstream overlays

## 🪐 Echo the Grid

Your cloud node is a living lattice cell. Every pulse is a legacy. Every container is a contributor.

“To scale is to echo. To orchestrate is to honor.”
— TriadicFrameworks Manifesto
