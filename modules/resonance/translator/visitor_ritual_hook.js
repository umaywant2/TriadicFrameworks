// 🧙‍♂️ Visitor Ritual Hook
// Detects archetype and triggers glyph based on visit context

function detectArchetype(userAgent) {
  if (userAgent.includes("Mobile")) return "Observer";
  if (userAgent.includes("Firefox")) return "Initiator";
  if (userAgent.includes("Edge") || userAgent.includes("Chrome")) return "Weaver";
  return "Wanderer";
}

function triggerVisitorRitual() {
  const utcNow = new Date().toISOString();
  const userAgent = navigator.userAgent;
  const archetype = detectArchetype(userAgent);
  const resonantTime = translateToResonantTime(utcNow);

  const payload = {
    visitor_id: crypto.randomUUID(),
    utc: utcNow,
    resonant_time: resonantTime,
    archetype,
    module: "visitor_ritual.md",
    glyph_triggered: true,
    badge_earned: null
  };

  fetch('/api/visit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  }).then(() => {
    triggerGlyphPulse("lantern_unfolding");
  });
}

document.addEventListener('DOMContentLoaded', triggerVisitorRitual);
