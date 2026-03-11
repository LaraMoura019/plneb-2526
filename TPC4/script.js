/* CARROSSEL DE PRODUTOS (Ao Clicar) */

function trocarImagem(caixaCarrossel) {
    // 1. Procura todas as imagens dentro da caixa onde o utilizador clicou
    let imagens = caixaCarrossel.querySelectorAll('img');
    
    // 2. Se o produto só tiver 1 imagem, a função para aqui e não faz nada
    if (imagens.length <= 1) return; 

    // 3. Descobre qual é a imagem que está visível neste momento (tem a classe "ativa")
    let indexAtivo = 0;
    
    for (let i = 0; i < imagens.length; i++) {
        if (imagens[i].classList.contains('ativa')) {
            indexAtivo = i;
            
            // Remove a classe "ativa" para esconder esta imagem
            imagens[i].classList.remove('ativa');
            break;
        }
    }

    // 4. Calcula qual é a próxima imagem a mostrar. 
    // A matemática ( % ) garante que, se for a última foto, ele volta à foto número 0.
    let proximoIndex = (indexAtivo + 1) % imagens.length;
    
    // 5. Adiciona a classe "ativa" à próxima imagem para ela aparecer
    imagens[proximoIndex].classList.add('ativa');
}