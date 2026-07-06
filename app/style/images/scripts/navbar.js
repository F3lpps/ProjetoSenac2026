document.addEventListener('DOMContentLoaded', function(){
    const token = localStorage.getItem('Token');

    const links = document.querySelectorAll('.link-cabecalho');

    links.forEach(link => {
        if (link.getAttribute('href') === './login.html') {

            if (token) {
                link.setAttribute('href', './forms.html');
            }
        }
    })
})