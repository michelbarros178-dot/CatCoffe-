document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registerForm');

    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            
            // Capturamos con tus IDs reales del HTML
            const datosRegistro = {
                nombre: document.getElementById('regName').value,
                email: document.getElementById('regEmail').value,
                telefono: document.getElementById('regPhone').value,
                password: document.getElementById('regPassword').value
            };

            // Validación local rápida
            if (datosRegistro.nombre.trim().length < 3) {
                e.preventDefault(); // Frena el envío SOLO si hay error
                alert("Por favor, ingresa un nombre válido.");
                return;
            }

            // NO ponemos e.preventDefault() al final.
            // NO ponemos window.location.href.
            // Dejamos que el formulario viaje libremente a Python.
            alert(`¡Procesando registro para ${datosRegistro.nombre}! Espera un momento...`);
        });
    }
});