import jsonpickle
from flask import Response

# Meus imports
from model.Pergunta import Pergunta, PerguntaFactory
from model.JsonTools import LoadData

class PerguntaUtils:
    
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
        perguntas = PerguntaUtils.carregar_perguntas(dados)
        return perguntas
    
    @staticmethod
    def serialize_json(perguntas):
        response = jsonpickle.encode(perguntas, unpicklable=False)    
        return Response(response, mimetype="application/json")
    
    @staticmethod
    def pesquisar_por_id(id):
        perguntas = PerguntaUtils.carregar_dicionario_de_perguntas()
        for pergunta in perguntas:
            if pergunta.id == id:
                return pergunta
        return None