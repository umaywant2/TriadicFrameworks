/* ═══════════════════════════════════════════════════════════════
   TriadicFrameworks · Shared Core Runtime
   triadic-core.js · v1.0.0
   Author: Nawder · Protocol: Metadata Refresh v1
   ═══════════════════════════════════════════════════════════════ */

(function (TF) {
  'use strict';

  /* ── CONSTANTS ───────────────────────────────────────────── */
  var PROTOCOL_VERSION = 'metadata-refresh-v1';
  var TOKEN_SESSION_ID  = '__SESSION_ID__';
  var TOKEN_TIMESTAMP   = '__SESSION_TIMESTAMP__';

  /* ── SESSION ─────────────────────────────────────────────── */
  TF.session = {
    id:        null,
    timestamp: null,
    module:    null,
    user:      null,

    init: function () {
      var body   = document.body;
      this.module = body.dataset.module    || 'unknown';
      this.user   = body.dataset.user      || 'Nawder';
      this.timestamp = new Date().toISOString();
      this.id        = this.module + '-' + Date.now();
      return this;
    }
  };

  /* ── METADATA REFRESH PROTOCOL v1 ────────────────────────── */
  TF.metadataRefresh = {
    run: function (session) {
      var sid = session.id;
      var ts  = session.timestamp;

      /* --- meta[content] tokens --- */
      document.querySelectorAll('meta[content="' + TOKEN_SESSION_ID  + '"]').forEach(function (el) { el.setAttribute('content', sid); });
      document.querySelectorAll('meta[content="' + TOKEN_TIMESTAMP   + '"]').forEach(function (el) { el.setAttribute('content', ts);  });

      /* --- data-session-id attributes --- */
      document.querySelectorAll('[data-session-id="' + TOKEN_SESSION_ID + '"]').forEach(function (el) { el.dataset.sessionId = sid; });

      /* --- <time> elements --- */
      document.querySelectorAll('time[datetime="' + TOKEN_TIMESTAMP + '"]').forEach(function (el) {
        el.setAttribute('datetime', ts);
        el.textContent = ts;
      });

      /* --- footer session ID spans --- */
      document.querySelectorAll('.tf-footer__session-id').forEach(function (el) { el.textContent = sid; });

      /* --- copyright year --- */
      var yearEl = document.getElementById('tf-year');
      if (yearEl) yearEl.textContent = new Date().getFullYear();
    }
  };

  /* ── BADGE SYSTEM ────────────────────────────────────────── */
  TF.badges = {
    /* Promote a draft badge to live once content is ready */
    setStatus: function (status) {
      document.querySelectorAll('.tf-badge--status').forEach(function (el) {
        el.classList.remove('tf-badge--draft', 'tf-badge--live');
        el.classList.add('tf-badge--' + status);
        el.textContent = status.charAt(0).toUpperCase() + status.slice(1);
        el.setAttribute('aria-label', 'Status: ' + status);
      });
    }
  };

  /* ── MODULE REGISTRY ─────────────────────────────────────── */
  TF.registry = {
    modules: {
      son:        { label: 'SoN',        layer: 'Narrative Layer',   icon: '◈', color: '#7c6fef', href: '/modules/son/' },
      vocabulary: { label: 'Vocabulary', layer: 'Linguistic Layer',  icon: '◇', color: '#5fa8d3', href: '/modules/vocabulary/' },
      invariants: { label: 'Invariants', layer: 'Structural Layer',  icon: '◉', color: '#d36b5f', href: '/modules/invariants/' },
      hooks:      { label: 'Hooks',      layer: 'Engagement Layer',  icon: '◎', color: '#5fd38a', href: '/modules/hooks/' }
    },

    get: function (moduleId) {
      return this.modules[moduleId] || null;
    },

    applyModuleColor: function (moduleId) {
      var mod = this.get(moduleId);
      if (!mod) return;
      document.documentElement.style.setProperty('--tf-module-color', mod.color);
      /* Build a dimmed rgba from hex */
      var r = parseInt(mod.color.slice(1,3), 16);
      var g = parseInt(mod.color.slice(3,5), 16);
      var b = parseInt(mod.color.slice(5,7), 16);
      document.documentElement.style.setProperty('--tf-module-color-dim', 'rgba(' + r + ',' + g + ',' + b + ',0.15)');
    }
  };

  /* ── PLACEHOLDER AUDIT (dev helper) ─────────────────────── */
  TF.placeholderAudit = {
    /* Call in dev to log all unfilled placeholders to console */
    run: function () {
      var items = [];
      document.querySelectorAll('.tf-placeholder, [data-placeholder]').forEach(function (el, i) {
        items.push({ index: i, tag: el.tagName, id: el.id || '—', text: (el.textContent || '').trim().slice(0, 80) });
      });
      if (items.length) {
        console.group('[TriadicFrameworks] Unfilled placeholders (' + items.length + ')');
        items.forEach(function (p) { console.log(p.index, p.tag, '#' + p.id, p.text); });
        console.groupEnd();
      } else {
        console.log('[TriadicFrameworks] No unfilled placeholders found.');
      }
      return items;
    }
  };

  /* ── SMOOTH SECTION SCROLL ───────────────────────────────── */
  TF.nav = {
    init: function () {
      document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener('click', function (e) {
          var target = document.querySelector(link.getAttribute('href'));
          if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            target.focus({ preventScroll: true });
          }
        });
      });
    }
  };

  /* ── INIT ────────────────────────────────────────────────── */
  TF.init = function () {
    var session = TF.session.init();
    TF.metadataRefresh.run(session);
    TF.registry.applyModuleColor(session.module);
    TF.nav.init();

    /* Dev-mode placeholder audit */
    if (document.documentElement.dataset.tfDev === 'true') {
      TF.placeholderAudit.run();
    }

    document.dispatchEvent(new CustomEvent('tf:ready', { detail: { session: session, protocol: PROTOCOL_VERSION } }));
  };

  /* Boot on DOM ready */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', TF.init);
  } else {
    TF.init();
  }

}(window.TF = window.TF || {}));
