# Reconhecimento de Entidades Nomeadas (NER) em Português com BERTimbau

## Sobre o Projeto
Este projeto implementa um modelo de **Named Entity Recognition (NER)** treinado especificamente para a língua portuguesa. O objetivo do modelo é ler textos (como notícias) e extrair automaticamente entidades importantes, classificando-as em 5 categorias principais:
* **Pessoa** (`PER`)
* **Localização** (`LOC`)
* **Organização** (`ORG`)
* **Data** (`DATA`)
* **Profissão** (`PROF`)

O modelo foi treinado a partir do zero (fine-tuning) usando o **BERTimbau** (`neuralmind/bert-base-portuguese-cased`) e o dataset **Portuguese NER** (`lfcc/portuguese_ner`).

---

## Resultados
Após 3 épocas de treino, o modelo atingiu resultados seguintes:
* **F1-Score:** ~95.7%
* **Precision:** ~94.5%
* **Recall:** ~96.9%
* **Accuracy Global:** ~98.4%

---

## Tecnologias Utilizadas
* Python
* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) (Modelos, Tokenizers e Trainer)
* [Hugging Face Datasets](https://huggingface.co/docs/datasets/index) (Processamento de dados)
* `evaluate` e `seqeval` (Métricas de avaliação NER)
* PyTorch (Motor de Deep Learning)

---

## Desafios e Aprendizagens
A construção deste modelo envolveu resolver vários problemas técnicos reais :

### 1. Tutoriais em Inglês
**O Problema:** Inicialmente, o modelo estava a classificar entidades com etiquetas erradas (ex: "Donald Trump" como `location` e "EUA" como `creative-work`).

**Solução:** Estava a injetar dicionários (`id2label`) de um tutorial americano (WNUT). A solução foi extrair as etiquetas *diretamente* dos metadados do dataset em português (`dataset["train"].features["ner_tags"].feature.names`) para garantir o alinhamento perfeito.

### 2. O Limite de Leitura do BERT (512 Tokens)
**O Problema:** O treino parava com o erro: `The size of tensor a (565) must match the size of tensor b (512)`.

**Solução:** O modelo BERT tem um limite de memória de 512 tokens por frase. Adicionei os parâmetros `truncation=True` e `max_length=512` na função do Tokenizer para cortar as notícias muito longas, resolvendo o erro de matriz.

### 3. O Problema das Subpalavras (Subwords) e o Alinhamento
**O Problema:** O Tokenizer do BERT divide palavras desconhecidas em pedaços (ex: `Ormuz` vira `Or` + `##muz`), o que criava um desalinhamento entre o número de palavras e o número de etiquetas.

**Solução:** Implementação de uma função de alinhamento (`align_labels_with_tokens`) que usa o valor `-100` para mascarar os pedaços de palavras e tokens especiais (`[CLS]`, `[SEP]`), garantindo que o modelo só aprende com o início de cada palavra.

### 4. Extração Limpa (Pipeline Aggregation)
**O Problema:** Ao fazer a inferência, o modelo devolvia palavras cortadas com hashes (`##`).

**Solução:** Utilização do parâmetro `aggregation_strategy="simple"` na Pipeline do Hugging Face. Isto junta automaticamente os prefixos B (Início) e I (Dentro) e cola as subpalavras, devolvendo entidades compostas completas (ex: "Donald Trump" numa só string).

---

## Como usar o modelo (Inferência)
Depois de treinado, o modelo pode ser facilmente testado numa notícia usando a ferramenta `pipeline`.