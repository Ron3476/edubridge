// main.js - EduBridge (Futuristic Edition)

// Confirm JS loaded with neon-style console
console.log('%c💠 EduBridge Loaded', 'color: #00d4ff; font-weight: bold; font-size: 1rem; text-shadow: 0 0 8px #00d4ff');

// DOM Helpers
const $ = selector => document.querySelector(selector);
const $$ = selector => document.querySelectorAll(selector);

// Utility: Fade out and remove alerts with neon glow effect
const fadeAlert = alert => {
    alert.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    alert.style.opacity = '0';
    alert.style.transform = 'translateY(-12px) scale(0.98)';
    setTimeout(() => alert.remove(), 600);
};

// DOMContentLoaded events
document.addEventListener('DOMContentLoaded', () => {

    // Auto-dismiss alerts
    $$('.alert').forEach(alert => {
        setTimeout(() => fadeAlert(alert), 4000);
    });

    // Smooth scroll for internal links
    $$('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', e => {
            e.preventDefault();
            const target = $(anchor.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                // Optional neon flash effect on target
                target.classList.add('scroll-highlight');
                setTimeout(() => target.classList.remove('scroll-highlight'), 800);
            }
        });
    });

    // Confirm toggle on study plan forms
    $$('form[action*="toggle"]').forEach(form => {
        form.addEventListener('submit', e => {
            if (!confirm('Toggle this task status?')) e.preventDefault();
        });
    });

    // Subtle card hover fallback for JS
    $$('.card').forEach(card => {
        card.addEventListener('mouseenter', () => card.classList.add('hovered'));
        card.addEventListener('mouseleave', () => card.classList.remove('hovered'));
    });

});
