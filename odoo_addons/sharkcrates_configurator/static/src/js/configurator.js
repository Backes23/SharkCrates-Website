/**
 * We don't have DriveWorks' documented completion event/payload API, so this
 * only detects completion the same way their own CSS does: the WordPress
 * site's CSS toggles a "message-shown" class on `.dw-message-form-complete`
 * once the embed finishes. We watch for that class and report it to Odoo.
 * If DriveWorks exposes a real JS callback or postMessage payload (e.g. the
 * chosen dimensions/price), swap this out for that instead.
 */
(function () {
    "use strict";

    function watchMessage(selector, onShown) {
        var el = document.querySelector(selector);
        if (!el) {
            return;
        }
        var observer = new MutationObserver(function () {
            if (el.classList.contains("message-shown")) {
                onShown(el);
                observer.disconnect();
            }
        });
        observer.observe(el, {attributes: true, attributeFilter: ["class"]});
    }

    document.addEventListener("DOMContentLoaded", function () {
        watchMessage(".dw-message-form-complete", function (el) {
            fetch("/configurator/submitted", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    message: el.getAttribute("data-message"),
                    url: window.location.href,
                    timestamp: new Date().toISOString(),
                }),
            });
        });
    });
})();
