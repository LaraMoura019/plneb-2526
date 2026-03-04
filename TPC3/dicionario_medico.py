import re
import json

#abrir o ficheiro 
ficheiro = open ("dicionario_medico.txt","r", encoding="utf-8")
texto = ficheiro.read()


#--------RETIRAR ESPAÇOS DE MUDANÇA DE PAGINA------

#texto = re.sub(r"\n\n\f","\n",texto)
#este metodo faz com que as os \f que nao estao na quebra de pagina tambem sejam identificados e 
#e fiquem dois conceitos juntos (retira um \n necessario entre dois conceitos diferentes)

#---dividir nos 3 casos possiveis---

#quebra de pagina entre termo-definição
texto = re.sub(r"\n\n([^\n]+)\n\n\f", r"\n\n\1\n",texto)
#uso dos () para guardar como um grupo de captura
#\1 escreve o que ficou guardado no grupo de captura

#quebra de pagina entre definição-definicao

#texto = re.sub(r"\n\n\f([^\n]+\n\n)", r" \1",texto) falha quando a definição tem mais que uma linha
#ou seja, falha quando a definição tem \n

texto = re.sub(r"\n\n\f((.|\n)*?)\n\n", r" \1\n\n", texto)
#para quando encontrar um \n\n
#forma alternativa
#texto = re.sub(r"\n\n\f([\s\S]*?)\n\n", r" \1\n\n", texto)

#quebra de pagina \n-termo
texto = re.sub(r"\f","",texto)


#-----CAPTURAR OS CONCEITOS
conceitos = re.split(r"\n\n",texto)
#print(conceitos)

#------ CRIAR O DICIONARIO
def limpa_descricao(descricao):
    resultado=re.sub(r"\n"," ",descricao)
    resultado= resultado.strip()
    return resultado

def criar_dicionario():
    dicionario={}
    for c in conceitos[1:]:
        elems = re.split(r"\n", c , maxsplit=1)
        if len(elems) > 1:
            designacao = elems[0]
            descricao = elems[1]
            dicionario[designacao] = limpa_descricao(descricao)
        else:
            continue
    return dicionario

def criar_json(dicionario,filename):
    f_out = open(filename,"w",encoding="utf-8")
    ficheiro_json =json.dump(dicionario,f_out,indent=4, ensure_ascii=False) 
    return ficheiro_json

criar_json(criar_dicionario(),"dicionario_medico.json")
print(criar_dicionario())
print(len(criar_dicionario()))





