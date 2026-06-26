const form = document.getElementById('post-form');

form.addEventListener('submit', function(event) {

    event.preventDefault();

    const usernameInput = document.getElementById('user');
    const emailInput = document.getElementById('email');
    const senhaInput = document.getElementById('password');

    const user = usernameInput.value;
    const email = emailInput.value;
    const senha = senhaInput.value;

    if (!email || !senha) { //verificação de campos vazios
               alert ("Os campos Email e Senha são obrigatórios!")
               return
            }

    console.log("user:", user);
    console.log("email:", email);
    console.log("senha:", senha);

        });




