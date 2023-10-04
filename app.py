from flask import Flask, render_template

# Imports locais do meu projeto
from model.JsonTools import LoadData
from model.Pergunta import Pergunta

app = Flask(__name__)

@app.route("/perguntas")
def perguntas():
    loader = LoadData()
    dados = loader.getJson('./assets/perguntas.json')
    perguntas = Pergunta.carregar_perguntas(dados)
    return render_template('perguntas.html', perguntas=perguntas)

if __name__ == '__main__':
    app.debug = True
    app.run()