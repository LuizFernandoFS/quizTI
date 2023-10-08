from flask import Flask

# Imports locais do meu projeto
from model.Pergunta import Pergunta, EstrategiaPerguntas

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

@app.route("/gerar/perguntas/<tema>/<int:quantidade>")
def gerar_perguntas_tema_quantidade(tema, quantidade):
    perguntas = Pergunta.carregar_dicionario_de_perguntas()
    estrategia = EstrategiaPerguntas(perguntas)
    perguntas_por_tema = estrategia.gerar_perguntas_por_tema(quantidade, tema)
    return Pergunta.serialize_json(perguntas_por_tema)

@app.route("/gerar/perguntas/aleatorias/<int:quantidade>")
def gerar_perguntas_aleatorias(quantidade):
    perguntas = Pergunta.carregar_dicionario_de_perguntas()
    estrategia = EstrategiaPerguntas(perguntas)
    perguntas_aleatorias = estrategia.gerar_perguntas_aleatorias(quantidade)
    return Pergunta.serialize_json(perguntas_aleatorias)

if __name__ == '__main__':
    app.debug = True
    app.run()