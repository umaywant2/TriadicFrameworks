function collectStructure() {
  return {
    url: window.location.href,
    title: document.title,
    nav_count: document.querySelectorAll("nav, header, footer").length,
    main_count: document.querySelectorAll("main, [role='main']").length,
    form_count: document.querySelectorAll("form").length,
    button_count: document.querySelectorAll("button, [role='button']").length,
    dom_nodes: document.getElementsByTagName("*").length
  };
}

browser.runtime.sendMessage({
  type: "rtt-structure",
  structure: collectStructure()
});

