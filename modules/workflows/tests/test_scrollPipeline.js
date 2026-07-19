/* 🧪 Minimal Test Harness (Jest) */

import { runScroll } from "../scrollPipeline.js";

test("runs a basic scroll", () => {
    const scroll = `
        emitter: test
        frequency: 144
    `;

    const out = runScroll(scroll);
    expect(out).toHaveProperty("output");
});
