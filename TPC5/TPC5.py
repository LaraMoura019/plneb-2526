import requests 
from bs4 import BeautifulSoup
import json
import string

url="https://www.atlasdasaude.pt/doencasAaZ/"
url_full_desc="https://www.atlasdasaude.pt"

def extrair_full_desc(url_desc):
    html = requests.get(url_desc).text
    soup = BeautifulSoup(html, "html.parser")
    
    div_desc = soup.find("div", class_="field field-name-body field-type-text-with-summary field-label-hidden")
    if not div_desc: 
        return {}
    
    conteudo = {}

    #full_desc = div_desc.find("div", class_="field-item even")
    titulo_atual = "Full_desc"
    conteudo[titulo_atual]=""

    for elemento in div_desc.find_all(['div','h2', 'p', 'ul', 'ol']):
        
        if elemento.name == 'h2':
            # Sempre que encontramos um h2, ele passa a ser o novo título ativo
            titulo_atual = elemento.text.replace('\n', ' ').strip()
            conteudo[titulo_atual] = ""
            
        else:
            texto = elemento.text.replace('\n', ' ').strip()
            if texto:
                conteudo[titulo_atual] += texto +" "
                
    print(conteudo)
    return conteudo


def extrair_pagina(url):
    html = requests.get(url).text
    soup=BeautifulSoup(html,"html.parser")
    div_doenca = soup.find_all("div",class_="views-row")
    res={}
    for div in div_doenca:
        descricao=[]
        designacao = div.div.h3.a.text
        small_desc = div.find("div",class_="views-field-body").div.text
        url_desc = div.div.h3.a['href']
        full_desc=extrair_full_desc(url_full_desc+url_desc)
        descricao.append(small_desc.strip())
        descricao.append(full_desc)
        res[designacao]=descricao 
    return res

res={}
for letra in string.ascii_lowercase:
    res=res | extrair_pagina(url+letra)


f_out=open("doencas_todas.json","w",encoding="utf-8")
json.dump(res,f_out, indent=4,ensure_ascii=False)
f_out.close()