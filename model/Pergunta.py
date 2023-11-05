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