window.addEventListener('load', () => {

    const loader = document.getElementById('loader');

     // Espera 4 segundos
    setTimeout(() => {

        loader.style.opacity = '0';

        setTimeout(() => {
            loader.remove();
        }, 800);

        document.body.style.overflow = 'auto';

    }, 4000);
    
document.getElementById('contenido').style.display = 'block';

});

