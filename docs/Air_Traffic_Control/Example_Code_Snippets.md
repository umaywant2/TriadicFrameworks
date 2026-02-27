# 6. 🛠️ Example Code Snippets (Developer‑Ready)

## 6.1 RTT‑Inside Middleware Skeleton

```ts
export class RttMiddleware {
  private engine = new RttEngine();

  constructor(subscribe, publish) {
    subscribe((tracks) => {
      const augmented = tracks.map(t => {
        const neighbors = tracks.filter(n => n.trackId !== t.trackId);
        const rtt = this.engine.computeMetrics(t, neighbors);
        return { ...t, rtt };
      });
      publish(augmented);
    });
  }
}
```
