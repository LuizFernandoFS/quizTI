from flask import Flask, jsonify
import jsonpickle

# Imports locais do meu projeto
from model.Pergunta import Pergunta

app = Flask(__name__)

@app.route("/perguntas")
def perguntas():
    perguntas_dicionario = Pergunta.carregar_dicionario_de_perguntas()
    return Pergunta.serialize_json(perguntas_dicionario)

@app.route("/perguntas/<tema>")
def perguntas_tema_especifico(tema):
    perguntas_dicionario = Pergunta.carregar_dicionario_de_perguntas()
    perguntas_tema = Pergunta.filtrar_perguntas_por_tema(perguntas_dicionario, tema)   
    return Pergunta.serialize_json(perguntas_tema)

if __name__ == '__main__':
    app.debug = True
    app.run()