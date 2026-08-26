/* ═══════════════════════════════════════════════════════════════
   TriadicFrameworks · Module JS: SoN (Structural operating Node)
   assets/js/modules/son.js · v1.0.0
   Requires: triadic-core.js (TF global)
   ═══════════════════════════════════════════════════════════════ */

(function (TF) {
  'use strict';

  /* ── WAIT FOR CORE READY ─────────────────────────────────── */
  document.addEventListener('tf:ready', function (e) {
    SoN.init(e.detail.session);
  });

  var SoN = {

    /* ── INIT ──────────────────────────────────────────────── */
    init: function (session) {
      this.session = session;
      this.bindTriadicMap();
      this.bindLayerList();
      /* PLACEHOLDER: additional SoN-specific inits */
    },

    /* ── TRIADIC MAP INTERACTION ───────────────────────────── */
    bindTriadicMap: function () {
      var poles = document.querySelectorAll('.tf-triadic-map__pole');
      poles.forEach(function (pole) {
        pole.setAttribute('tabindex', '0');
        pole.setAttribute('role', 'button');

        pole.addEventListener('click',  function () { SoN.selectPole(this); });
        pole.addEventListener('keydown', function (e) {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            SoN.selectPole(this);
          }
        });
      });
    },

    selectPole: function (poleEl) {
      var type = poleEl.dataset.pole;
      /* PLACEHOLDER: emit pole-selected event, update related sections */
      document.dispatchEvent(new CustomEvent('son:pole-selected', { detail: { pole: type } }));
    },

    /* ── NARRATIVE LAYER LIST ─────────────────────────────── */
    bindLayerList: function () {
      var items = document.querySelectorAll('.tf-layer-list__item');
      items.forEach(function (item) {
        item.setAttribute('tabindex', '0');
        /* PLACEHOLDER: expand/collapse layer detail panels */
      });
    }

    /* PLACEHOLDER: additional SoN module methods */
  };

  /* Expose to TF namespace */
  TF.modules = TF.modules || {};
  TF.modules.son = SoN;

}(window.TF = window.TF || {}));
