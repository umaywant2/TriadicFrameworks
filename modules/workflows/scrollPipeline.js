/**
 * Scroll Pipeline (JavaScript)
 * TriadicFrameworks • Workflows Subsystem
 *
 * Executes `.fff` scroll artifacts in browser environments.
 * Mirrors the Python pipeline API:
 *
 *     runScroll(scrollText)
 *
 * Returns:
 *     { output, warnings, metadata }
 */

import { parseScroll } from "./tft/scrolls/parse.js";
import { executeScroll } from "./tft/scrolls/pipeline.js";

export function runScroll(scrollText) {
    const parsed = parseScroll(scrollText);
    const result = executeScroll(parsed);

    return {
        output: result.output,
        warnings: result.warnings || [],
        metadata: result.metadata || {}
    };
}
