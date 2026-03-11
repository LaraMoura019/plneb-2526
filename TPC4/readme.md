# Projeto de Estudo: DARMA - Website de Mobiliário

Este projeto foi desenvolvido do zero como um exercício prático intensivo para consolidar os meus conhecimentos em **HTML**. O objetivo foi criar um website com aspeto profissional e interativo para a empresa dos meus pais, garantindo um código limpo e sem depender de *frameworks* externas.

## O que aprendi e apliquei neste projeto

### HTML5 (Estrutura e Semântica)
* **HTML Semântico:** Utilização correta de tags estruturais (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) para criar um documento legível para navegadores e motores de busca.
* **Navegação Complexa:** Criação de menus e submenus estruturados através do aninhamento correto de listas não ordenadas (`<ul>` e `<li>`).
* **Caminhos e Ligações:** Gestão da navegação entre múltiplas páginas (`home_page.html`, `sofas.html`, etc.) e organização de caminhos relativos para importar imagens e folhas de estilo.

### CSS3 

* **CSS Grid:** Criação de uma galeria de produtos responsiva utilizando `display: grid`, com regras automáticas (`auto-fit`, `minmax()`) para que o layout se adapte a qualquer ecrã sem quebrar.
* **Proporções de Imagem:** Uso da propriedade `aspect-ratio` e `object-fit: cover` para garantir que dezenas de fotografias diferentes fiquem com caixas de tamanho perfeitamente simétrico.
* **Transições e Pseudo-classes:** Utilização de `:hover` combinado com `transition` para criar interações (sombras a crescer, elementos a "levitar", etiquetas a aparecer suavemente).

### JavaScript (Manipulação do DOM)
* **Interatividade via Cliques:** Criação de um sistema de carrossel de imagens manual (`onclick`) diretamente nos cartões de produto.
* **Seleção de Elementos:** Utilização do `querySelectorAll` para encontrar imagens específicas dentro de uma `<div>`.
* **Lógica de Classes:** Manipulação visual dos elementos ligando e desligando classes CSS através do JavaScript (`classList.add` e `classList.remove`).

## Como executar este projeto
1. Fazer o download ou clone deste repositório.
2. Abrir a pasta no **Visual Studio Code**.
3. Recomenda-se a utilização da extensão **Live Server**. Clique com o botão direito no ficheiro `home_page.html` e selecione "Open with Live Server".
