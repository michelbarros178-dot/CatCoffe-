// --- CONTROL DE SCROLL CON LOADER ---
if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}

document.addEventListener('DOMContentLoaded', () => {

    // --- 1. VARIABLES ---
    const counters = document.querySelectorAll('.counter');
    const statsSection = document.querySelector('.stats-bar');
    let started = false;

    // --- 2. CONTADORES PRO (SUAVES Y LENTOS) ---
    const startCount = (el) => {
        const target = parseInt(el.getAttribute('data-target'));
        const suffix = el.getAttribute('data-suffix') || '';

        let startTime = null;
        const duration = 3000; // ⏱️ 3 segundos (puedes subir a 4000 si quieres más lento)

        const animate = (timestamp) => {
            if (!startTime) startTime = timestamp;

            const progress = timestamp - startTime;
            const percentage = Math.min(progress / duration, 1);

            // 🔥 easing suave (pro)
            const easeOut = 1 - Math.pow(1 - percentage, 3);

            const current = Math.floor(easeOut * target);

            // 🔥 formato con separador de miles
            el.innerText = current.toLocaleString() + suffix;

            if (percentage < 1) {
                requestAnimationFrame(animate);
            } else {
                el.innerText = target.toLocaleString() + suffix;
            }
        };

        requestAnimationFrame(animate);
    };

    // --- 3. REVEAL ON SCROLL ---
    const revealSections = () => {
        const reveals = document.querySelectorAll('.reveal');

        reveals.forEach(section => {
            const windowHeight = window.innerHeight;
            const elementTop = section.getBoundingClientRect().top;
            const elementVisible = 150;

            if (elementTop < windowHeight - elementVisible) {
                section.classList.add('active');
            }
        });
    };

    // --- 4. INTERSECTION OBSERVER (CONTADORES) ---
    if (statsSection) {
        const statsObserver = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !started) {
                counters.forEach(counter => startCount(counter));
                started = true;
            }
        }, { threshold: 0.5 });

        statsObserver.observe(statsSection);
    }

    // --- 5. HEADER SCROLL ---
    const headerScroll = () => {
        const header = document.querySelector('.header');
        if (!header) return;

        if (window.scrollY > 50) {
            header.style.background = 'rgba(20, 17, 14, 0.95)';
            header.style.padding = '5px 0';
            header.style.boxShadow = '0 5px 20px rgba(0,0,0,0.3)';
        } else {
            header.style.background = 'transparent';
            header.style.padding = '20px 0';
            header.style.boxShadow = 'none';
        }
    };

    // --- 6. EVENTOS ---
    window.addEventListener('scroll', () => {
        revealSections();
        headerScroll();
    });

    revealSections();
    headerScroll();

    // --- 7. FILTRO DE PRODUCTOS ---
    const botonesFiltro = document.querySelectorAll('.btn-cat');
    const cards = document.querySelectorAll('.product-card');

    botonesFiltro.forEach(boton => {
        boton.addEventListener('click', () => {
            const categoria = boton.getAttribute('data-cat');

            botonesFiltro.forEach(btn => btn.classList.remove('active'));
            boton.classList.add('active');

            cards.forEach((card, index) => {
                if (card.classList.contains(categoria)) {

                    card.classList.remove('oculto');

                    setTimeout(() => {
                        card.classList.add('mostrar');
                    }, index * 120);

                } else {
                    card.classList.remove('mostrar');
                    card.classList.add('oculto');
                }
            });
        });
    });

});

// --- LIBERAR SCROLL (BACKUP) ---
window.addEventListener("load", () => {
    document.body.style.overflow = "auto";
});