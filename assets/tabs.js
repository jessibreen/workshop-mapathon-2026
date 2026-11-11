// The page shows one of three panels at a time: Before, At the mapathon, After.
// The menu mixes tab links (.tab) with jump links (.sub) to sections inside a panel.
// Any in-page link opens the panel that holds its target, then scrolls to it.
const panels = Array.from(document.querySelectorAll("main .panel"));
const tabLinks = Array.from(document.querySelectorAll(".toc a.tab"));
const menuLinks = Array.from(document.querySelectorAll(".toc a"));

if (panels.length) {
  const activate = (panel, id) => {
    panels.forEach(p => { p.hidden = p !== panel; });
    tabLinks.forEach(a => {
      if (a.hash === `#${panel.id}`) a.setAttribute("aria-current", "true");
      else a.removeAttribute("aria-current");
    });
    menuLinks.forEach(a => a.classList.toggle("here", a.classList.contains("sub") && a.hash === `#${id}`));
  };

  const go = (id, push) => {
    const target = id && document.getElementById(id);
    const panel = target && (panels.includes(target) ? target : target.closest(".panel"));
    if (!panel) return false;
    activate(panel, id);
    if (target === panel) {
      // Opening a tab: stay put, unless already scrolled past the menu; then go to the tab's top.
      const top = document.querySelector("main").getBoundingClientRect().top + window.scrollY - document.querySelector(".toc").offsetHeight;
      if (window.scrollY > top) window.scrollTo({ top });
    } else {
      target.scrollIntoView({ block: "start" });
    }
    if (push && location.hash !== `#${id}`) history.pushState(null, "", `#${id}`);
    return true;
  };

  document.addEventListener("click", event => {
    const link = event.target.closest('a[href^="#"]');
    if (link && go(link.hash.slice(1), true)) event.preventDefault();
  });

  // Sections scroll to just below the sticky menu, whatever its height (it wraps on phones).
  const toc = document.querySelector(".toc");
  const setMenuHeight = () => document.documentElement.style.setProperty("--menu-h", `${toc.offsetHeight}px`);
  setMenuHeight();
  window.addEventListener("resize", setMenuHeight);

  const sync = () => { if (!go(location.hash.slice(1), false)) activate(panels[0], ""); };
  document.documentElement.classList.add("tabs-enabled");
  window.addEventListener("popstate", sync);
  window.addEventListener("hashchange", sync);
  sync();
}
