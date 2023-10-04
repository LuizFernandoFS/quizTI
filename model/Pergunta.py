class Pergunta:
    def __init__(self, pergunta, opcoes, resposta_correta, tema, nivel_dificuldade):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta_correta = resposta_correta
        self.tema = tema
        self.nivel_dificuldade = nivel_dificuldade

    @staticmethod
    def carregar_perguntas(dados_do_json):
        # Cria um ARRAY de perguntas
        perguntas = []
        for pergunta_json in dados_do_json["perguntas"]:
            # Popula o objeto com base no JSON
            pergunta = Pergunta(
                pergunta_json["pergunta"],
                pergunta_json["opcoes"],
                pergunta_json["resposta_correta"],
                pergunta_json["tema"],
                pergunta_json["nivel_dificuldade"]
            )
            # Adiciona PERGUNTA ao ARRAY de perguntas
            perguntas.append(pergunta)
        return perguntas