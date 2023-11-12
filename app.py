from flask import Flask, request
from flask_cors import CORS

# Imports locais do meu projeto
from services.PerguntaUtils import PerguntaUtils
from model.Estrategia import EstrategiaPerguntas
from model.Jogo import Jogo

# INICIANDO FLASK
app = Flask(__name__)

# INICIANDO O QUIZ
jogo = Jogo()  

# HABILITANDO CORS
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/perguntas")
def perguntas():
    perguntas_dicionario = PerguntaUtils.carregar_dicionario_de_perguntas()
    return PerguntaUtils.serialize_json(perguntas_dicionario)

@app.route("/perguntas/<tema>")
def perguntas_tema_especifico(tema):
    perguntas_dicionario = PerguntaUtils.carregar_dicionario_de_perguntas()
    perguntas_tema = PerguntaUtils.filtrar_perguntas_por_tema(perguntas_dicionario, tema)   
    return PerguntaUtils.serialize_json(perguntas_tema)

@app.route("/gerar/perguntas/<tema>/<int:quantidade>")
def gerar_perguntas_tema_quantidade(tema, quantidade):
     perguntas = PerguntaUtils.carregar_dicionario_de_perguntas()
     estrategia = EstrategiaPerguntas(perguntas)
     perguntas_por_tema = estrategia.gerar_perguntas_por_tema(quantidade, tema)
     return PerguntaUtils.serialize_json(perguntas_por_tema)

@app.route("/gerar/perguntas/aleatorias/<int:quantidade>")
def gerar_perguntas_aleatorias_com_quantidade(quantidade):
     perguntas = PerguntaUtils.carregar_dicionario_de_perguntas()
     estrategia = EstrategiaPerguntas(perguntas)
     perguntas_aleatorias = estrategia.gerar_perguntas_aleatorias(quantidade)
     return PerguntaUtils.serialize_json(perguntas_aleatorias)

@app.route("/perguntas/aleatorias")
def gerar_perguntas_aleatorias():
     perguntas = PerguntaUtils.carregar_dicionario_de_perguntas()
     estrategia = EstrategiaPerguntas(perguntas)
     perguntas_aleatorias = estrategia.gerar_perguntas_aleatorias(10)
     return PerguntaUtils.serialize_json(perguntas_aleatorias)

@app.route("/perguntas/<int:id>")
def pesquisar_pergunta_por_id(id):
    pergunta = PerguntaUtils.pesquisar_por_id(id)
    return PerguntaUtils.serialize_json(pergunta)

@app.route("/verificar", methods=["POST"])
def verificar_resposta():  
    data = request.get_json()
    id_pergunta = data.get("id_pergunta")
    resposta = data.get("resposta")
    pontuacao = jogo.verificar_resposta(id_pergunta, resposta)
    return PerguntaUtils.serialize_json(pontuacao)

@app.route("/zerar_pontuacao")
def zerar_pontuacao():
    jogo.zerar_pontuacao()
    return PerguntaUtils.serialize_json(jogo.obter_pontuacao())

if __name__ == '__main__':
    app.debug = True
    app.run()