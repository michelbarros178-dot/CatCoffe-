
/* =========================================
   🐾 HUELLAS SOLO EN PRODUCTOS
   ========================================= */

const productosSection = document.getElementById("productos");

let lastStepY = 0;
let step = 0;
let canCreate = true;

window.addEventListener("scroll", () => {
    if (!productosSection) return;

    const rect = productosSection.getBoundingClientRect();

    // 🔥 detectar si la sección está visible
    const visible = rect.top < window.innerHeight && rect.bottom > 0;

    if (!visible) return;

    if (!canCreate) return;

    const currentY = window.scrollY;

    if (Math.abs(currentY - lastStepY) > 100) {
        createStep(currentY);
        lastStepY = currentY;

        canCreate = false;
        setTimeout(() => canCreate = true, 200);
    }
});

function createStep(scrollY) {
    const paw = document.createElement("div");
    paw.classList.add("paw");

    const isLeft = step % 2 === 0;
    step++;

    const curve = Math.sin(step * 0.5) * 20;
    const rotation = -20 + (Math.random() * 10 - 5);

    if (isLeft) {
        paw.style.left = (40 + curve) + "px";
        paw.style.transform = `rotate(${rotation}deg)`;
    } else {
        paw.style.right = (40 - curve) + "px";
        paw.style.transform = `scaleX(-1) rotate(${rotation}deg)`;
    }

    // 📍 SOLO dentro de la sección
    const sectionTop = productosSection.offsetTop;
    const relativeY = scrollY - sectionTop;

    paw.style.top = (sectionTop + relativeY + window.innerHeight - 160) + "px";

    document.body.appendChild(paw);

    setTimeout(() => paw.remove(), 2500);
}
