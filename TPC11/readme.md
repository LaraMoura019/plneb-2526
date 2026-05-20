# Motor de Busca TF-IDF e Similaridade do Cosseno

Este projeto foi desenvolvido no âmbito da disciplina de **Processamento de Linguagem Natural em Engenharia Biomédica** . 

Trata-se de uma implementação feita de raiz, sem o uso de bibliotecas de Machine Learning como o *scikit-learn* do algoritmo **TF-IDF (Term Frequency - Inverse Document Frequency)** acoplado a um motor de **Similaridade do Cosseno (Cosine Similarity)** para Recuperação de Informação.

## Funcionalidades

1. **Pré-processamento Textual:** Utiliza a biblioteca `spaCy` para tokenização, conversão para minúsculas e remoção de *stop words* e pontuação.
2. **Cálculo de Frequência de Termos (TF):** Calcula a proporção de cada termo num documento específico.
3. **Cálculo de Frequência Inversa em Documentos (IDF):** Penaliza palavras muito comuns e dá maior peso matemático a palavras raras na coleção.
4. **Matriz TF-IDF:** Constrói uma matriz global onde todas as linhas (documentos) têm o mesmo tamanho, mapeando para o vocabulário completo.
5. **Motor de Busca (Cosine Similarity):** Permite inserir uma *query* (pesquisa) e devolve os documentos ordenados por ordem de relevância através do cálculo do ângulo entre os vetores multidimensionais.

## Pré-requisitos e Instalação

Certifique-se de que tem o Python instalado. Depois, instale a biblioteca `spaCy` e o modelo de linguagem em inglês:

```bash
# Instalar o spaCy
pip install spacy

# Descarregar o modelo de processamento da língua inglesa
python -m spacy download en_core_web_sm
```

## Como Utilizar
Basta correr o script principal no terminal:

```Bash
python tf-idf.py
```

## Personalizar a Coleção e a Pesquisa
Para testar com outros textos, basta editar as seguintes variáveis no ficheiro tf-idf.py:

```Bash
# A base de dados de documentos
collection = [
    "The sky is blue",
    "The sun is bright",
    "The sun in the sky"
]

# A frase de pesquisa
query = "A bright sun in the sky"
```

## Exemplo de Output
O script processa a query e compara-a matematicamente com os documentos, devolvendo o score de similaridade (de 0 a 1.0):

### Query processada: ['bright', 'sun', 'sky']

### --- Resultados da Pesquisa ---
Score: 0.9450 | Documento: 'The sun is bright'

Score: 0.4627 | Documento: 'The sun in the sky'

Score: 0.1133 | Documento: 'The sky is blue'

## Resultado 
O documento com o "score" mais alto não é necessariamente o que partilha mais palavras com a query, mas sim o que partilha as palavras mais raras e relevantes (neste caso, a palavra "bright").