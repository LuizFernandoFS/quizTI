import random
from flask import Response
import jsonpickle

# Meus imports
from model.JsonTools import LoadData

# FACTORY para criar perguntas
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

# Utilizando STRATEGY para gerar perguntas randômicas ou com determinados temas
class EstrategiaPerguntas:
    def __init__(self, perguntas):
        self.perguntas = perguntas

    def selecionar_perguntas(self, num_perguntas, tema=None):
        if tema is None:
            return self.gerar_perguntas_aleatorias(num_perguntas)
        else:
            return self.gerar_perguntas_por_tema(num_perguntas, tema)

    def gerar_perguntas_aleatorias(self, num_perguntas):
        if num_perguntas >= len(self.perguntas):
            return self.perguntas
        return random.sample(self.perguntas, num_perguntas)

    def gerar_perguntas_por_tema(self, num_perguntas, tema):
        perguntas_do_tema = Pergunta.filtrar_perguntas_por_tema(self.perguntas, tema)
        if num_perguntas >= len(perguntas_do_tema):
            return perguntas_do_tema
        return random.sample(perguntas_do_tema, num_perguntas)
