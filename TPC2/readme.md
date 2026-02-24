# Ficha de Exercícios - Expressões Regulares em Python

Este repositório contém a resolução de uma ficha prática composta por 10 exercícios focados na manipulação e pesquisa de *strings* utilizando Expressões Regulares através da biblioteca `re` em Python.

## Objetivos de Aprendizagem
Durante a resolução destes exercícios, foram explorados e aplicados os seguintes conceitos:
* **Funções principais da biblioteca `re`:** `match()`, `search()`, `findall()`, `sub()` e `split()`.
* **Âncoras:** Início (`^`) e fim (`$`) de *string*.
* **Classes de Caracteres:** Dígitos (`\d`), caracteres de palavra (`\w`), espaços em branco (`\s`) e conjuntos (`[a-z]`, `[.!?]`).
* **Quantificadores:** Zero ou mais (`*`), um ou mais (`+`), opcional (`?`).
* **Fronteiras de Palavra:** Limites lógicos de palavras usando `\b`.
* **Agrupamento e Flags:** Grupos não-capturáveis `(?:...)` e a flag `re.IGNORECASE`.

---

## Extras e Decisões de Implementação
Para além do que foi estritamente pedido no enunciado, o código desenvolvido inclui várias otimizações e abordagens alternativas:

* **Ex. 1.5 e Ex. 9:** 
    * No Exercício 1.5, a divisão da string não foi feita apenas pela vírgula, mas sim pela expressão `,\s*`. Isto garantiu que os espaços indesejados no início de cada palavra fossem automaticamente limpos da lista final.
  * No Exercício 9, implementou-se a expressão universal `\s+` em vez de apenas espaços literais (` +`). Isto garante que a função trata corretamente tabulações (`\t`) e quebras de linha (`\n`), tendo sido criada uma frase de teste específica (`frase2`) para comprovar a eficácia.
* **Ex. 2:** A expressão regular foi flexibilizada com `\s*` antes e depois da pontuação (`r"por favor\s*[.!?]\s*$"`). Isto permite que o código valide a frase mesmo que existam espaços antes do ponto de interrogação ou no fim da string.
* **Ex. 6:** Aplicação do grupo `(?:...)`. Isto garantiu que os pronomes fossem agrupados para efeitos do operador `|` (OU), permitindo que as fronteiras de palavra (`\b`) no início e no fim se aplicassem corretamente a todas as opções.
* **Ex. 8:** Evitou-se o uso do `\b` de forma propositada ao capturar números negativos. Como o sinal `-` e o espaço são ambos considerados "não-palavras", o uso de fronteiras impediria a captura correta de números como `-6`.
* **Ex. 1.3, Ex. 5 e Ex. 10:** Vários exercícios apresentam mais do que uma solução documentada:
  * Uso de (`(?i:...)`) como da flag explícita `re.IGNORECASE` (Ex. 1.3).
  * Inclusão de versões otimizadas utilizando **List Comprehensions** em alternativa aos tradicionais ciclos `for` (Ex. 5 e Ex. 10). Adicionalmente, no Ex. 5, demonstrou-se a integração entre a biblioteca `re` e a função nativa `sum()` para um código mais limpo e conciso numa só linha.
---
## Resumo dos Exercícios

* **Alíneas 1.1 a 1.5:** Exercícios introdutórios para explorar as diferenças entre funções de regex (`match`, `search`, `findall`, `sub` e `split`) usando a palavra "hello" e separação por vírgulas.
* **Exercício 2:** Função `palavra_magica` - Validação de frases que terminam obrigatoriamente com "por favor" seguido de pontuação válida.
* **Exercício 3:** Função `narcisismo` - Contagem de pronomes ("eu") ignorando *case sensitive* e evitando falsos positivos em palavras compostas.
* **Exercício 4:** Função `troca_de_curso` - Substituição sensível a maiúsculas da sigla "LEI".
* **Exercício 5:** Função `soma_string` - Extração de números separados por vírgulas numa *string*, conversão para inteiros e cálculo da sua soma.
* **Exercício 6:** Função `pronomes` - Extração de vários pronomes pessoais usando lógica de agrupamento e fronteiras.
* **Exercício 7:** Função `variavel_valida` - Validação rigorosa de nomes de variáveis (letras iniciais e apenas caracteres alfanuméricos/underscores depois).
* **Exercício 8:** Função `inteiros` - Extração de números inteiros positivos e negativos de uma frase.
* **Exercício 9:** Função `underscores` - Limpeza avançada de formatação de espaços.
* **Exercício 10:** Função `codigos_postais` - Divisão e estruturação de uma lista de códigos postais num formato de pares.
---
## Como Executar
Para testar o código, basta ter o Python instalado. Não são necessárias bibliotecas externas, pois o módulo `re` é nativo da linguagem.

```bash
# Executar o ficheiro python
python nome_do_ficheiro.py
