from services.PerguntaUtils import PerguntaUtils

#SINGLETON

class Jogo:

    def __init__(self):
        self.pontuacao = 0

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Jogo, cls).__new__(cls)
            cls._instance.pontuacao = 0
        return cls._instance

    def aumentar_pontuacao(self, pontos):
        self.pontuacao += pontos

    def obter_pontuacao(self):
        return self.pontuacao

    def verificar_resposta(self, id_pergunta, resposta):
        pergunta = PerguntaUtils.pesquisar_por_id(id_pergunta)
        if pergunta.resposta_correta == resposta: 
            self.aumentar_pontuacao(10)
        return self.obter_pontuacao()
            