from flask import Response
import jsonpickle

# Meus imports
from model.JsonTools import LoadData

class PerguntaFactory:
    @staticmethod
    def criar_pergunta(pergunta_json):
        return Pergunta(
            pergunta_json["id"],
            pergunta_json["pergunta"],
            pergunta_json["opcoes"],
            pergunta_json["resposta_correta"],
            pergunta_json["tema"],
            pergunta_json["nivel_dificuldade"]
        )

class Pergunta:
    def __init__(self, id, pergunta, opcoes, resposta_correta, tema, nivel_dificuldade):
        self.id = id
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta_correta = resposta_correta
        self.tema = tema
        self.nivel_dificuldade = nivel_dificuldade

    @staticmethod
    def carregar_perguntas(dados_do_json):
        perguntas = []
        for pergunta_json in dados_do_json["perguntas"]:
            pergunta = PerguntaFactory.criar_pergunta(pergunta_json)
            perguntas.append(pergunta)
        return perguntas
    
    @staticmethod
    def filtrar_perguntas_por_tema(perguntas, tema):
        perguntas_tema = []
        for pergunta in perguntas:
            if pergunta.tema == tema.upper():
                perguntas_tema.append(pergunta)     
        return perguntas_tema
    
    @staticmethod
    def carregar_dicionario_de_perguntas():
        loader = LoadData()
        dados = loader.getJson('./assets/perguntas.json')
        perguntas = Pergunta.carregar_perguntas(dados)
        return perguntas
    
    @staticmethod
    def serialize_json(perguntas):
        response = jsonpickle.encode(perguntas, unpicklable=False)    
        return Response(response, mimetype="application/json")
