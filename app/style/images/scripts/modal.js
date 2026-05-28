const modal = document.getElementById('modal')
const closeModalButton = document.querySelector('dialog button')
const modalContent = document.getElementById('modal-content')

closeModalButton.addEventListener('click', function() {
    modal.close()
})

export function openStoryModal(titulo, autor, historia) {
    modalContent.innerHTML = `
    <div class="Modal-topo">
        <h2>${titulo}</h2>
        <p class="autor">
        por ${autor}
        </p>
        <div class="modal-conteudo">
        <p style="white-space: pre-wrap">${historia} </p></div>
    `

    modal.showModal();
}