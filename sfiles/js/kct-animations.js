/*
 * Site-wide scroll reveals (AOS + css/kct-animations.css).
 *
 * Everything on the site is brought onto one motion language (the "kct-*"
 * animations): hand-authored data-aos attributes, the theme's old WOW
 * animations and the elements listed in RULES below all end up using the
 * same four reveals, so every page feels consistent.
 */
(function () {
    "use strict";

    if (!window.AOS) { return; }

    var reducedMotion = window.matchMedia &&
        window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    var UP = "kct-up";
    var FROM_LEFT = "kct-from-left";
    var FROM_RIGHT = "kct-from-right";
    var SCALE = "kct-scale";

    var STAGGER = 100;      // ms between siblings (AOS supports 50ms steps)
    var MAX_STAGGER_STEPS = 5;

    // Carousels manage their own transforms, so nothing inside them is animated.
    var NO_ANIMATION_INSIDE = ".owl-carousel, .swiper-wrapper, .kct-hero";
    // Site chrome that is not auto-tagged by RULES.
    var SKIP_RULES_INSIDE = NO_ANIMATION_INSIDE + ", header, footer, " +
        ".mobile-nav__wrapper, .search-popup, .popup-overlay, [data-aos]";

    // [selector, animation, stagger siblings?]
    var RULES = [
        // Page headers / section titles
        [".page-header__title", UP],
        [".cleenhearts-breadcrumb", UP],
        [".sec-title", UP],
        [".sec-title__tagline", UP],
        [".section-title", UP],
        [".section-subtitle", UP],

        // About
        [".about-one__text", UP],
        [".card-item", SCALE, true],
        [".trustee-message-header", UP],
        [".trustee-message-paragraph", UP],
        [".trustee-message-quote", UP],
        [".logo-title", UP],
        [".trustee", SCALE, true],
        [".kct-staff-heading", UP],
        [".kct-staff-card", UP, true],
        [".aboutPara", UP],
        [".vmcard", UP, true],
        [".trustWrapp", UP],
        [".affItem", SCALE, true],

        // Careers
        [".career-container-hiring h2", UP],
        [".career-container-hiring img", SCALE],

        // Gallery
        [".gallery-one__card", SCALE, true],

        // News
        [".video-wrapper", FROM_LEFT],
        [".video-content", FROM_RIGHT],

        // Events / projects / schemes / reports / terms
        [".event-details__time", UP],
        [".event-details__title", UP],
        [".event-details__text", UP],
        [".event-details__inner__list", UP],
        [".reaction-section", UP],
        [".pdf-viewer-wrapper", UP],
        [".download-pdf", UP],

        // Success stories
        [".story_card:not(.reverse) .story_card-img", FROM_LEFT],
        [".story_card:not(.reverse) .story_card-text-box", FROM_RIGHT],
        [".story_card.reverse .story_card-img", FROM_RIGHT],
        [".story_card.reverse .story_card-text-box", FROM_LEFT],

        // Donate
        [".kct-donate-impact__title", UP],
        [".kct-donate-impact__subtitle", UP],
        [".kct-impact-table__row", UP, true],
        [".kct-donate-trust__title", UP],
        [".kct-trust-badge", SCALE, true],
        [".kct-donate-stats__item", UP, true],
        [".kct-donate-form-card", UP],
        [".kct-fcra", UP]
    ];

    var AOS_ATTRS = ["data-aos", "data-aos-delay", "data-aos-once", "data-aos-duration",
        "data-aos-easing", "data-aos-offset", "data-aos-anchor-placement"];

    var animated = [];

    function each(selector, fn) {
        var nodes = document.querySelectorAll(selector);
        for (var i = 0; i < nodes.length; i++) { fn(nodes[i]); }
    }

    function clearAos(el) {
        AOS_ATTRS.forEach(function (attr) { el.removeAttribute(attr); });
    }

    function siblingDelay(el) {
        if (!el.parentElement) { return 0; }
        var index = Array.prototype.indexOf.call(el.parentElement.children, el);
        return (index % MAX_STAGGER_STEPS) * STAGGER;
    }

    function apply(el, animation, delay) {
        clearAos(el);
        el.setAttribute("data-aos", animation);
        el.setAttribute("data-aos-once", "true");
        if (delay) { el.setAttribute("data-aos-delay", delay); }
        animated.push(el);
    }

    // Map a legacy animation name (AOS built-ins or animate.css) to ours.
    function refine(name) {
        name = (name || "").toLowerCase();
        if (/flip|zoom/.test(name)) { return SCALE; }
        // AOS "fade-right" / animate.css "fadeInLeft" both enter from the left.
        if (name === "fade-right" || name.indexOf("fadeinleft") !== -1) { return FROM_LEFT; }
        if (name === "fade-left" || name.indexOf("fadeinright") !== -1) { return FROM_RIGHT; }
        return UP;
    }

    if (!reducedMotion) {
        // 1. Theme "wow" (animate.css) elements -> our reveals. This runs
        //    before WOW starts, so removing the class takes them out of WOW.
        each(".wow", function (el) {
            var legacy = el.className;
            var wowDelay = parseInt(el.getAttribute("data-wow-delay"), 10) || 0;
            el.className = legacy.split(/\s+/).filter(function (cls) {
                return !/^(wow|animated|animate__\w+|fadeIn\w*|slideIn\w*|zoomIn\w*)$/.test(cls);
            }).join(" ");
            el.style.visibility = "";

            if (el.closest(NO_ANIMATION_INSIDE) || el.querySelector("[data-aos]") ||
                el.parentElement.closest("[data-aos]")) { return; }
            var delay = Math.min(Math.round(wowDelay / 200) * STAGGER, 400);
            apply(el, refine(legacy), delay);
        });

        // 2. Hand-authored data-aos elements -> our reveals, with a gentle
        //    stagger when several siblings animate together.
        each("[data-aos]:not([data-aos^='kct-'])", function (el) {
            if (el.closest(NO_ANIMATION_INSIDE)) { clearAos(el); return; }
            var hasAnimatedSibling = el.parentElement &&
                el.parentElement.querySelectorAll(":scope > [data-aos]").length > 1;
            apply(el, refine(el.getAttribute("data-aos")),
                hasAnimatedSibling ? siblingDelay(el) : 0);
        });

        // 3. Everything else listed in RULES.
        RULES.forEach(function (rule) {
            each(rule[0], function (el) {
                if (el.closest(SKIP_RULES_INSIDE) || el.querySelector("[data-aos]")) { return; }
                apply(el, rule[1], rule[2] ? siblingDelay(el) : 0);
            });
        });
    }

    // Once an element has finished revealing, drop the AOS attributes so its
    // own hover transforms / transitions behave exactly as designed.
    animated.forEach(function (el) {
        el.addEventListener("transitionend", function onEnd(e) {
            if (e.target !== el || e.propertyName !== "transform") { return; }
            if (!el.classList.contains("aos-animate")) { return; }
            el.removeEventListener("transitionend", onEnd);
            clearAos(el);
        });
    });

    AOS.init({
        disable: reducedMotion,
        once: true,
        offset: 80
    });
})();
