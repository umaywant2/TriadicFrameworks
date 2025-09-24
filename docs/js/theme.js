function toggleTheme() {
  document.body.classList.toggle('dark-mode');
  const isDark = document.body.classList.contains('dark-mode');
  // Notify listeners (hero-warp.js)
  document.dispatchEvent(new CustomEvent('theme:changed', { detail: { dark: isDark } }));
}
