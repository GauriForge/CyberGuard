/* ========================================
   CyberGuard - Main JavaScript
   ======================================== */


/* ---------- Page Loaded ---------- */

document.addEventListener("DOMContentLoaded", function () {

    console.log("CyberGuard loaded successfully.");

    initializeSearch();
    initializeNotifications();
    initializePasswordToggle();
    initializeFormValidation();
    initializeConfirmations();
    initializeMobileMenu();
    initializeFlashMessages();
    initializeCareerFilters();
    initializeInteractiveControls();

});


/* ---------- Search ---------- */

function initializeSearch() {

    const searchInputs = document.querySelectorAll(
        ".search-box input, [data-search-input]"
    );

    searchInputs.forEach(function (searchInput) {

        searchInput.addEventListener("input", function () {

            const searchText = searchInput.value
                .toLowerCase()
                .trim();

            const container = document.querySelector(
                searchInput.dataset.searchContainer ||
                "[data-search-container]"
            );

            if (!container) {
                return;
            }

            const items = container.querySelectorAll(
                "[data-search-item]"
            );

            items.forEach(function (item) {
                const itemText = item.textContent.toLowerCase();
                item.hidden = !itemText.includes(searchText);
            });

        });

    });

}


/* ---------- Notifications ---------- */

function initializeNotifications() {

    const notificationButtons = document.querySelectorAll(
        ".notification-button"
    );

    notificationButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const notificationUrl = button.dataset.notificationUrl;

            if (notificationUrl) {
                window.location.href = notificationUrl;
                return;
            }

            const notificationPanel = document.querySelector(
                "[data-notification-panel]"
            );

            if (notificationPanel) {
                notificationPanel.hidden = !notificationPanel.hidden;
            }

        });

    });

}


/* ---------- Password Visibility ---------- */

function initializePasswordToggle() {

    const toggleButtons = document.querySelectorAll(
        "[data-toggle-password]"
    );

    toggleButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const targetId = button.dataset.togglePassword;
            const passwordInput = document.getElementById(targetId);

            if (!passwordInput) {
                return;
            }

            const showPassword = passwordInput.type === "password";

            passwordInput.type = showPassword ? "text" : "password";

            button.textContent = showPassword ? "Hide" : "Show";
            button.setAttribute(
                "aria-label",
                showPassword ? "Hide password" : "Show password"
            );

        });

    });

}


/* ---------- Form Validation ---------- */

function initializeFormValidation() {

    const forms = document.querySelectorAll(
        "form[data-validate]"
    );

    forms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            if (!form.checkValidity()) {
                event.preventDefault();
                form.reportValidity();
            }

        });

    });

}


/* ---------- Confirmation Dialogs ---------- */

function initializeConfirmations() {

    const confirmationElements = document.querySelectorAll(
        "[data-confirm]"
    );

    confirmationElements.forEach(function (element) {

        element.addEventListener("click", function (event) {

            const message =
                element.dataset.confirm ||
                "Are you sure you want to continue?";

            if (!window.confirm(message)) {
                event.preventDefault();
            }

        });

    });

}


/* ---------- Mobile Menu ---------- */

function initializeMobileMenu() {

    const menuButton = document.querySelector(
        "[data-mobile-menu-toggle]"
    );

    const mobileMenu = document.querySelector(
        "[data-mobile-menu]"
    );

    if (!menuButton || !mobileMenu) {
        return;
    }

    menuButton.addEventListener("click", function () {

        const isExpanded =
            menuButton.getAttribute("aria-expanded") === "true";

        menuButton.setAttribute(
            "aria-expanded",
            String(!isExpanded)
        );

        mobileMenu.hidden = isExpanded;

    });

}


/* ---------- Flash Messages ---------- */

function initializeFlashMessages() {

    const closeButtons = document.querySelectorAll(
        "[data-dismiss-message]"
    );

    closeButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const message = button.closest(
                ".flash-message, .alert, [data-flash-message]"
            );

            if (message) {
                message.remove();
            }

        });

    });

}


/* ---------- Cybersecurity Career Filters ---------- */

function initializeCareerFilters() {

    const searchInput = document.querySelector(
        "#careerSearch, [data-career-search]"
    );

    const categoryFilter = document.querySelector(
        "#careerCategory, [data-career-category]"
    );

    const careerCards = document.querySelectorAll(
        ".career-card"
    );

    if (!careerCards.length) {
        return;
    }

    function filterCareers() {

        const searchText = searchInput
            ? searchInput.value.toLowerCase().trim()
            : "";

        const selectedCategory = categoryFilter
            ? categoryFilter.value.toLowerCase()
            : "";

        let visibleCount = 0;

        careerCards.forEach(function (card) {

            const cardText = card.textContent.toLowerCase();
            const cardCategory = (
                card.dataset.category ||
                card.querySelector(".career-category")?.textContent ||
                ""
            ).trim().toLowerCase();

            const matchesSearch = cardText.includes(searchText);

            const matchesCategory =
                !selectedCategory ||
                cardCategory === selectedCategory;

            const isVisible = matchesSearch && matchesCategory;

            card.hidden = !isVisible;

            if (isVisible) {
                visibleCount++;
            }

        });

        const emptyState = document.querySelector(
            ".career-empty-state"
        );

        if (emptyState) {
            emptyState.hidden = visibleCount !== 0;
        }

    }

    if (searchInput) {
        searchInput.addEventListener("input", filterCareers);
    }

    if (categoryFilter) {
        categoryFilter.addEventListener("change", filterCareers);
    }

    filterCareers();

}


/* ---------- Interactive Controls ---------- */

function initializeInteractiveControls() {

    /* Update visible value labels for range inputs. */

    const sliders = document.querySelectorAll(
        'input[type="range"][data-value-target]'
    );

    sliders.forEach(function (slider) {

        const target = document.getElementById(
            slider.dataset.valueTarget
        );

        function updateValue() {
            if (target) {
                target.textContent = slider.value;
            }
        }

        slider.addEventListener("input", updateValue);
        updateValue();

    });


    /* Prevent accidental double submission of forms. */

    const protectedForms = document.querySelectorAll(
        "form[data-prevent-double-submit]"
    );

    protectedForms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            if (form.dataset.submitting === "true") {
                event.preventDefault();
                return;
            }

            if (!form.checkValidity()) {
                return;
            }

            form.dataset.submitting = "true";

            const submitButton = form.querySelector(
                'button[type="submit"], input[type="submit"]'
            );

            if (submitButton) {
                submitButton.disabled = true;
            }

        });

    });

}