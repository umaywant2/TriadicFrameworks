export async function onRequest() {
  return new Response(JSON.stringify({
    modules: []
  }), {
    headers: { "Content-Type": "application/json" }
  });
}
