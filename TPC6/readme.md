# Harry Friends

Este projeto tem como objetivo principal analisar o texto do livro *"Harry Potter e A Pedra Filosofal"* e extrair as amizades entre as personagens. 

A extração baseia-se na premissa de **coocorrência**: se duas personagens são mencionadas na mesma frase, consideramos que interagiram ou são "amigas". O resultado final é exportado para um ficheiro JSON devidamente ordenado.

##  spaCy no Projeto 

O **spaCy** é uma biblioteca avançada e industrial de Processamento de Linguagem Natural (NLP) para Python. Neste projeto, ele atua como o "cérebro" que lê e interpreta a gramática do livro. Em vez de usarmos simples expressões regulares (Regex) ou procurarmos por palavras com letra maiúscula, o spaCy compreende o contexto das frases.

Para este trabalho, foi utilizado o modelo **`pt_core_news_lg`** , que assume duas responsabilidades fundamentais:

1. **Segmentação de Frases (`doc.sents`):** O modelo divide o texto do livro inteiro em frases lógicas.
2. **Reconhecimento de Entidades Nomeadas (`entity.label_ == "PER"`):** O spaCy analisa cada termo e classifica-o conseguindo distinguir, pelo contexto, se uma palavra é um Local (`LOC`), uma Organização (`ORG`) ou uma Pessoa (`PER`). O nosso código extrai de forma apenas as entidades classificadas como `"PER"`.

## O Desafio e a Solução (Limpeza de Dados)

Apesar de o spaCy ser muito poderoso, a extração automática gera sempre algum "ruído" num texto literário longo. Inicialmente, o modelo identificava feitiços e variações do mesmo nome (ex: "Draco", "Malfoy", "Draco Malfoy") como pessoas completamente diferentes, gerando um ficheiro JSON com cerca de **1500 linhas**.

Para resolver isto, foram implementados dois mecanismos de normalização no código:
1. **Dicionário de Apelidos (`DICIONARIO_APELIDOS`):** Agrupa todas as variações e títulos de uma personagem sob um único nome principal (ex: "Professor Dumbledore" e "Alvo Dumbledore" tornam-se apenas "Dumbledore").
2. **Lista de Exclusão (`IGNORAR`):** Remove falsos positivos detetados pelo modelo (ex: feitiços como "Alohomora", casas de Hogwarts como "Grifinória" ou palavras comuns de início de frase que foram identificadas incorretamente como personagens).

**Resultado:** O ficheiro final foi reduzido para **cerca de 700 linhas** de dados, mais precisos e estruturados, removendo as duplicações e o lixo.

## Tecnologias Utilizadas

* **Python 3**
* **spaCy:** Motor principal de NLP para processamento do texto.
* **JSON:** Biblioteca nativa do Python para estruturação e exportação do mapeamento gerado.

## Como Funciona o Código

1. **Leitura do Texto:** O script lê o ficheiro `.txt` do livro na íntegra.
2. **Processamento (spaCy):** O documento é entregue ao motor do spaCy e dividido em frases.
3. **Extração e Limpeza:** Em cada frase, o código procura as entidades do tipo Pessoa (`"PER"`). O nome detetado passa pelos nossos dicionários de limpeza; se for válido e tiver mais de 2 caracteres, é adicionado a uma lista temporária.
4. **Cálculo de Coocorrência:** Se a frase contiver mais do que um nome (múltiplas entidades), o script regista uma interação entre eles de forma bidirecional num dicionário.
5. **Ordenação:**  Os amigos de cada personagem são ordenados do maior para o menor número de interações.
   * As personagens principais são ordenadas com base na quantidade total de amigos diferentes que possuem.
6. **Exportação:** Os dados são guardados e formatados no ficheiro `amigos.json` com indentação para fácil leitura.

## Como Executar

**1. Instalar as dependências:**
Abre o terminal e instala o spaCy e o respetivo modelo NLP em português:
```bash
pip install spacy
python -m spacy download pt_core_news_lg
``` 
**2. Preparar os ficheiros:**
Garante que o ficheiro de texto do livro se encontra na mesma diretoria do script Python, com o nome exato de "Harry Potter e A Pedra Filosofal.txt".

**3. Correr o script:**
Executa o ficheiro Python. O processamento do texto demorará alguns segundos a minutos dependendo da máquina. No final, o ficheiro amigos.json será gerado automaticamente na mesma pasta.