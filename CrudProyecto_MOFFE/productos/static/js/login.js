document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const togglePass = document.getElementById('togglePass');
    const passInput = document.getElementById('userPassword');

    // Mostrar/Ocultar contraseña
    togglePass.addEventListener('click', () => {
        const type = passInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passInput.setAttribute('type', type);
        togglePass.textContent = type === 'password' ? '👁' : '🙈';
    });

    // Manejo del Login
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('userEmail').value;
        
        console.log("Iniciando sesión en Moffee con:", email);
        alert("¡Bienvenida de nuevo a Moffee!");
    });
});