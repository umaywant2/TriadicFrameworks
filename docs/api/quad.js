export async function onRequest() {
  return new Response(JSON.stringify({
    engine: "Quad Engine",
    version: "1.0.0"
  }), {
    headers: { "Content-Type": "application/json" }
  });
}
