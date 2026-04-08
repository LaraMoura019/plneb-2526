from flask import Flask, render_template, request
import json

app = Flask(__name__)

f_db = open ("./dicionario_medico.json","r", encoding="utf-8")
db =  json.load (f_db)

@app.get("/")
def home_page():
    return render_template("home.html")

@app.get("/conceitos")
def listar_conceitos():
    pagina=request.args.get('pagina',1,type=int)
    letra_filtro = request.args.get('letra', '')
    por_pagina=20

    inicio =(pagina-1)*por_pagina
    fim = por_pagina+inicio
    conceitos=list(db.keys())

    if letra_filtro:
        conceitos = [c for c in conceitos if c.upper().startswith(letra_filtro.upper())]

    conceitos_por_pagina=conceitos[inicio:fim]
    total_paginas = (len(conceitos) + por_pagina - 1) // por_pagina
    return render_template('conceitos.html', 
                           conceitos=conceitos_por_pagina, 
                           pagina_atual=pagina, 
                           total_paginas=total_paginas,
                           letra_ativa=letra_filtro)

@app.get("/conceitos/<designacao>") # <designacao> estamos a passar um parametro
def conceito(designacao):
    if designacao in db:
        descricao = db[designacao]
        return render_template("conceito.html", designacao=designacao, descricao=descricao)
    else:
        return render_template("error.html", erro="O conceito introduzido não existe")
    


@app.get("/api/conceitos")
def conceitos_api():
    return db

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('error.html'), 404

app.run(host="localhost", port=4002, debug=True)