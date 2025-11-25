import CorridorClient from "../clients/js/corridorClient.js";
import { normalize, computeRci, assignGlyph } from "../rfc_qeb_0002/validator.js";
import fs from "fs";

const client = new CorridorClient("http://localhost:5000/v1");

async function processCorridor(corridorId, parentScroll) {
  // Step 1: Fetch metadata
  const metadata = await client.getCorridorMetadata(corridorId);

  // Step 2: Validate RCI/glyph
  const Cf = normalize(metadata.rail_signatures.frequency);
  const Cfl = normalize(metadata.rail_signatures.fluids);
  const Cfo = normalize(metadata.rail_signatures.forces);
  const RCI = computeRci(Cf, Cfl, Cfo, 3);
  const glyph = assignGlyph(RCI, Cf, Cfl, Cfo);

  const status =
    Math.round(RCI * 1000) / 1000 !== metadata.resonance_clarity_index ||
    glyph !== metadata.glyph
      ? "validation_failed"
      : "validation_passed";

  // Step 3: Append to remix lineage
  const lineageEvent = {
    event: {
      corridor_id: corridorId,
      parent_scroll: parentScroll,
      child_scroll: `${parentScroll}-child`,
      previous_glyph: metadata.glyph,
      new_glyph: glyph,
      previous_rci: metadata.resonance_clarity_index,
      new_rci: RCI,
      status: status,
    },
  };

  fs.writeFileSync(
    `registry/events/${corridorId}_event.yml`,
    JSON.stringify(lineageEvent, null, 2)
  );

  return lineageEvent;
}
