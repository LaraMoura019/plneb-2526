import spacy 
import json

nlp = spacy.load("pt_core_news_lg")

ficheiro_texto = open("Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf-8")
texto = ficheiro_texto.read()
ficheiro_texto.close()

doc = nlp(texto)

DICIONARIO_APELIDOS = {
    "Hermione Granger": "Hermione",
    "Draco Malfoy": "Draco",
    "Malfoy": "Draco",
    "Dracos": "Draco",
    "Neville Longbottom": "Neville",
    "Longbottom": "Neville",
    "Simas Finnigan": "Simas",
    "Dino Thomas": "Dino",
    "Katie Bell de Grifinória": "Katie Bell",
    "Bell": "Katie Bell",
    "Adriano Pucey": "Pucey",
    "Olívio Wood": "Olívio",
    "Wood": "Olívio",
    "Parvati Patil": "Parvati",
    "Lilá Brown": "Lilá",
    "Sr. Ronald Weasley": "Rony", 
    "Fred Weasley": "Fred",
    "Jorge Weasley": "Jorge",
    "Jorge\nWeasley": "Jorge",
    "Percy Weasley": "Percy",
    "Gina Weasley": "Gina",
    "Rúbeo": "Hagrid",
    "Rúbeo Hagrid": "Hagrid",
    "Rúbeo\nHagrid": "Hagrid",
    "Guardião das Chaves": "Hagrid",
    "Minerva McGonagall": "Minerva",
    "Severo": "Snape",
    "Professor Snape": "Snape",
    "Professor Dumbledore": "Dumbledore",
    "Alvo Dumbledore": "Dumbledore",
    "Bruxo Chefe": "Dumbledore",
    "Cacique Supremo": "Dumbledore",
    "Madame Nor-r-ra": "Madame Norr-ra",
    "Mulher\nGorda": "Mulher Gorda",
    "Sr. Barão": "Barão Sangrento",
    "barão Sangrento": "Barão Sangrento",
    "Nick Quase": "Nick Quase Sem Cabeça",
    "Nicholas de Mimsy": "Nick Quase Sem Cabeça",
    "Madame\nMalkin": "Madame Malkin",
    "Diggle": "Dédalo Diggle",
    "Tio Válter": "Válter",
    "Válter Dursley": "Válter",
    "Tia Petúnia": "Petúnia",
    "Dudley": "Duda",
    "Dudinha": "Duda",
    "Duda\natropelara": "Duda",
    "Lorde Voldemort": "Voldemort",
    "Você-Sabe-Quem": "Voldemort",
    "Nicolau Flamel": "Flamel",
    "Nicolau\nFlamel": "Flamel",
    "Nicolau": "Flamel",
    "Tiago Potter": "Tiago",
    "Tiago Potter?": "Tiago"
}

IGNORAR = {
    "Grifinória", "Sonserina", "Lufa-Lufa", "Herbologia", "Prof", "Certo", 
    "Hum", "Suponho", "Entrementes", "Poderíamos", "Achei", "Pensou", 
    "Acabavam", "Tchau", "Puxou", "Genial", "Cautela", "casa dos Dursley", 
    "Deus", "cartola", "Bobagens", "Senhor", "Mestre", "Monitor", "Peça", 
    "Agouro", "Aborrecido", "Suspeitou", "Sr.", "Professora",
    "FORA", "Srta", "Presentes", "gargalhadinha tremida", "Hagrid traia Dumbledore", 
    "Aguardem", "Olhava", "putz", "Acha", "Desculpe", 
    "Valha-me Deus", "Sonhei", "Deitado", "Quero", "Endereçaram", "Viram", 
    "Queriam", "Entende", "Querido", "Alohomora", "Feitiça", "Morto-Vivo",
    "Gringotes", "bezoar", "Estalagmite", "tempestade", "Sr. H. Potter\nQuarto 17",
    "Ilustrações", "Mary GrandPré ©", "Sanguinidade",

}

def encontrar_amigos():
    dicionario_amigos = {}
    #percorre todas as frases do documento
    for sent in doc.sents:
        lista_pessoas = []
        #em cada frase do documento faz uma lista dos diferentes nomes que aparecem
        for entity in sent.ents:
            #Verifica se é uma pessoa
            if entity.label_ == "PER":
                nome_original = entity.text.strip()
                #limpa o nome com o dicionario
                nome_limpo = DICIONARIO_APELIDOS.get(nome_original, nome_original)
                
                #ignora palavras que foram consideradas pessoas mas nao sao
                if nome_limpo not in IGNORAR and len(nome_limpo) > 2:
                    if nome_limpo not in lista_pessoas:
                        lista_pessoas.append(nome_limpo)
        #se a frase tiver mais do que um nome 
        if len(lista_pessoas)>1:
            for pessoa in lista_pessoas:
                #se a pessoa nao existir no dicionario é adicionada
                if pessoa not in dicionario_amigos:
                    dicionario_amigos[pessoa]={}
                #caso exista é adicionado as pessoas que estao na mesma frase
                for pessoa_restante in lista_pessoas:
                    if pessoa_restante!=pessoa:
                        if pessoa_restante not in dicionario_amigos[pessoa] :
                            dicionario_amigos[pessoa][pessoa_restante]=1
                        else:
                            dicionario_amigos[pessoa][pessoa_restante]+=1
    
    dicionario_ordenado = {}
    # Ordena os amigos pelo valor (número de ocorrências) de forma decrescente
    for personagem, amigos in dicionario_amigos.items():
        amigos_sorted = dict(sorted(amigos.items(), key=lambda item: item[1], reverse=True))
        dicionario_ordenado[personagem] = amigos_sorted
    #ordena pelo numero de amigos maior
    dicionario_final = dict(sorted(dicionario_ordenado.items(), key= lambda item: len(item[1]), reverse =True))
    return dicionario_final
   
ficheiro = open("amigos.json","w", encoding="utf-8")
json.dump(encontrar_amigos(),ficheiro,indent=4,ensure_ascii=False)

ficheiro.close()