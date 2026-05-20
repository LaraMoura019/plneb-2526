import spacy 
import math

nlp = spacy.load("en_core_web_sm") 
collection = ["The sky is blue",
            "The sun is bright",
            "The sun in the sky"
            ]

query = "A bright sun in the sky"

def pre_processamento(collection):
    new_collection = []
    for doc in collection:
        s_doc = nlp(doc)
        #remover stop_words, remover pontuação, tokenizar , colocar em minusculas
        filtered_tokens= [token.text.lower() for token in s_doc if not token.is_stop and not token.is_punct]
        new_collection.append(filtered_tokens)
    return new_collection
#print(pre_processamento(collection))


def tf(d): #recebe um documento
    res = {}
    N=len(d)
    for token in d:
        if token in res:
            res[token]+=1
        else:
            res[token]=1
    for key, value in res.items():
        value = value/N

    # res = {k: v/N k,v in res.items()}
    return res
    #{"termo":freq}

#idf(t,D)=log(N/df)
def idf(collection):
    N=len(collection)
    res = {}
    unique_terms = set([term for d in collection for term in d])
    for term in unique_terms:
        counter = 0
        for doc in collection:
            if term in doc:
                counter += 1
        rarity=math.log(N/counter,10)
        res[term]=rarity

    return res
# {termo:rarity}

#td_idf(t,d,D)=tf(t,d)*idf(t,D)
def tf_idf(collection):
    idf_values = idf(collection)
    values= idf_values.keys()
    res = []
    
    for d in collection:
        doc_tf_idf= []
        tf_values = tf(d)
        for term in values:
            if term in tf_values:
                tf_idf = tf_values[term]* idf_values[term]
                doc_tf_idf.append(tf_idf)
            else:
                doc_tf_idf.append(0)
        res.append(doc_tf_idf)
    return res

colecao_processada = pre_processamento(collection)
idf_values = idf(colecao_processada)
matriz_documentos = tf_idf(colecao_processada)

#----query
def vetor_query(query):
    query_pre_processada= pre_processamento([query])[0]
    query_tf=tf(query_pre_processada)
    vocabulario = idf_values.keys()

    vetor_query = []

    for term in vocabulario:
        if term in query_tf:
            # Usa o TF da query, mas o IDF da coleção original!
            score = query_tf[term] * idf_values[term]
            vetor_query.append(score)
        else:
            vetor_query.append(0)

    return vetor_query

def cosine_similarity(vetor_a, vetor_b):
    dot_product = sum(a * b for a, b in zip(vetor_a, vetor_b))
    magnitude_a = math.sqrt(sum(a**2 for a in vetor_a))
    magnitude_b = math.sqrt(sum(b**2 for b in vetor_b))
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)

def calcular_similariedade(query,matriz_documentos):

    resultados = []

    for i, doc_vector in enumerate(matriz_documentos):
        # Calcular a similaridade entre a pesquisa e este documento específico
        score = cosine_similarity(vetor_query(query), doc_vector)

        # Guardar a pontuação juntamente com a frase original
        resultados.append((score, collection[i]))

    # Ordenar os resultados do mais relevante (maior score) para o menos relevante
    resultados.sort(reverse=True, key=lambda x: x[0])
    return resultados

resultados=calcular_similariedade(query,matriz_documentos)
print("\n--- Resultados da Pesquisa ---")
print(query)
for score, doc in resultados:
    print(f"Score: {score:.4f} | Documento: '{doc}'")


