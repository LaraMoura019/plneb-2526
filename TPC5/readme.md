# Atlas da Saúde Scraper

Este projeto é um script em **Python** desenvolvido para realizar o *Web Scraping* do portal [Atlas da Saúde](https://www.atlasdasaude.pt/doencasAaZ/). O objetivo é converter o índice alfabético de doenças do site num ficheiro **JSON** estruturado.

---

## Funcionalidades

*   Percorre automaticamente todas as páginas de `a` a `z`.
*   Identifica e separa o conteúdo (Causas, Sintomas, Tratamento) utilizando a hierarquia de tags `<h2>`.
*   **Limpeza Automática:** 
    *   Remove quebras de linha (`\n`) que fragmentam o texto.
    *   Remove espaços em branco inúteis nas extremidades (`strip`).
*   **Exportação Organizada:** Gera um ficheiro JSON , facilitando a leitura e integração.

---

## Tecnologias Utilizadas

| Biblioteca | Função |
| :--- | :--- |
| **Requests** | Realiza os pedidos HTTP para aceder ao site. |
| **BeautifulSoup4** | Faz o parsing do HTML e extrai os elementos desejados. |
| **JSON** | Formata e grava os dados no ficheiro final. |
| **String** | Fornece o alfabeto para a iteração automática. |

---

## Estrutura do JSON Gerado

O ficheiro `doencas_todas.json` organiza a informação da seguinte forma:

```json
{
    "Nome da Doença": [
        "Resumo curto da listagem principal.",
        {
            "Full_desc": "Texto introdutório da página principal.",
            "Causas": "Texto consolidado sobre causas...",
            "Sintomas": "Texto consolidado sobre sintomas...",
            "Tratamento": "Informação sobre tratamentos...",
            "Artigos relacionados": "Lista de temas sugeridos."
        }
    ]
}