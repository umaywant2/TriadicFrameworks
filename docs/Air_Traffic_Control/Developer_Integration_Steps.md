# 3. 🔧 Developer Integration Steps

## 3.1 Subscribe to the Track Bus

Our ATC system already publishes fused tracks via:

- ASTERIX categories  
- Protobuf messages  
- JSON over WebSocket  
- Proprietary middleware  

RTT‑Inside middleware needs **read‑only** access.

### Example (TypeScript‑style pseudocode)

```ts
subscribeTracks((tracks: Track[]) => {
  rttMiddleware.process(tracks);
});
```
