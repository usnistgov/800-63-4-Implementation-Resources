// Custom JS can be added here. Datatables configuration, mermaid configuration
// or other custom settings that do not make sense to put in the template

// Lift the fixed sidebar above the footer when the footer is in view.
// The sidebar is position: fixed with bottom: 0, so without this it would
// visually extend over the top edge of the footer at the bottom of long pages.
(function () {
  function adjustSidebarBottom() {
    var footer = document.querySelector('.nist-footer');
    var sidebar = document.querySelector('.wy-nav-side');
    if (!footer || !sidebar) return;
    var rect = footer.getBoundingClientRect();
    var overlap = Math.max(0, window.innerHeight - rect.top);
    sidebar.style.bottom = overlap + 'px';
  }
  window.addEventListener('scroll', adjustSidebarBottom, { passive: true });
  window.addEventListener('resize', adjustSidebarBottom);
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', adjustSidebarBottom);
  } else {
    adjustSidebarBottom();
  }
})();
