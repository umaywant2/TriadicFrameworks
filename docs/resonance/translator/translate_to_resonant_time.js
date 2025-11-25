
// 🔁 Resonant-Time Translator
// Converts UTC timestamp to symbolic triad: E (Arrow), M (Clock), OC (Origin)

function translateToResonantTime(utcString) {
  const date = new Date(utcString);
  const hour = date.getUTCHours();
  const day = date.getUTCDate();
  const month = date.getUTCMonth() + 1;

  // Arrow (E): based on hour
  const E = `E${(hour % 12) + 1}`;

  // Clock (M): based on month
  const M = `M${month}`;

  // Origin (OC): based on day mod 5
  const OC = `OC${(day % 5) + 1}`;

  return `${E}-${M}-${OC}`;
}

// Example usage:
const utcNow = new Date().toISOString();
console.log("Resonant-Time:", translateToResonantTime(utcNow));
