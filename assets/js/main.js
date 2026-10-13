/* ==========================================================================
   Portafolio digital - Miguel Troncoso - Módulo 8
   Interacciones: navegación, progreso de scroll, animaciones y "volver arriba".
   ========================================================================== */
(function () {
  "use strict";

  const header = document.getElementById("site-header");
  const progress = document.getElementById("scroll-progress");
  const navToggle = document.getElementById("nav-toggle");
  const nav = document.getElementById("primary-nav");
  const toTop = document.getElementById("to-top");
  const navLinks = Array.from(document.querySelectorAll('.primary-nav a[href^="#"]'));
  const sections = Array.from(document.querySelectorAll("main section[id]"));

  /* ---------- Menú móvil ---------- */
  if (navToggle && nav) {
    navToggle.addEventListener("click", () => {
      const open = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
      document.body.classList.toggle("nav-open", !open);
    });

    nav.addEventListener("click", (event) => {
      if (event.target.closest("a")) {
        navToggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
        document.body.classList.remove("nav-open");
      }
    });
  }

  /* ---------- Scroll: sombra, progreso, botón subir y link activo ---------- */
  const onScroll = () => {
    const scrolled = window.scrollY;

    if (header) header.classList.toggle("is-scrolled", scrolled > 8);

    if (progress) {
      const height = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = (height > 0 ? (scrolled / height) * 100 : 0) + "%";
    }

    if (toTop) toTop.classList.toggle("is-visible", scrolled > 600);

    let current = "";
    for (const section of sections) {
      if (scrolled >= section.offsetTop - 140) current = section.id;
    }
    navLinks.forEach((link) => {
      const isActive = link.getAttribute("href") === "#" + current;
      link.classList.toggle("is-active", isActive && !link.classList.contains("nav-cta"));
    });
  };

  let ticking = false;
  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          onScroll();
          ticking = false;
        });
        ticking = true;
      }
    },
    { passive: true }
  );
  onScroll();

  if (toTop) {
    toTop.addEventListener("click", () =>
      window.scrollTo({ top: 0, behavior: "smooth" })
    );
  }

  /* ---------- Animación de aparición ---------- */
  const reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    reveals.forEach((el, index) => {
      el.style.transitionDelay = Math.min(index % 4, 3) * 70 + "ms";
      observer.observe(el);
    });
  } else {
    reveals.forEach((el) => el.classList.add("is-visible"));
  }

  /* ---------- Año dinámico en el footer ---------- */
  const year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());
})();
