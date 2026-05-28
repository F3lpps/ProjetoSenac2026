import { openStoryModal } from "./modal.js";

const form = document.getElementById('post-form');

form.addEventListener('submit', function(event) {

        event.preventDefault();

        const form_data = new FormData(event.target)

        const autorInput = document.getElementById('autor')
        const tituloInput = document.getElementById('titulo')
        const historiaInput = document.getElementById('historia')
        const historiasContainer = document.getElementById('historias')

        const autor = autorInput.value;
        const titulo = tituloInput.value;
        const historia = historiaInput.value;

        if (!autor || !historia) { //verificação de campos vazios
               alert ("Os campos Nome e História são obrigatórios!")
               return
        }

        const article = document.createElement('article');
        article.className = "artigo";

        article.innerHTML = `
        <div class="artigo-topo">
            <h2>${titulo || "História sem título"}</h2>

            <p class="autor">
                por ${autor}
            </p>
        </div>

        <div class="artigo-conteudo">
            ${historia.replace(/\n/g, "<br>")}
        </div>
    `;

    article.addEventListener('click', function() {
        openStoryModal(titulo, autor, historia);
    })

    document.getElementById('historias').appendChild(article);

    form.reset();
});