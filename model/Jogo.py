class Jogo:
    def __init__(self):
        self.pontuacao = 0

    def aumentar_pontuacao(self):
        self.pontuacao += 1

    def obter_pontuacao(self):
        return self.pontuacao

jogo = Jogo()  # Crie uma instância da classe Jogo

# Adicione um endpoint para aumentar a pontuação
@app.route("/aumentar_pontuacao", methods=["POST"])
def aumentar_pontuacao():
    jogo.aumentar_pontuacao()
    return "Pontuação aumentada com sucesso!"

# Adicione um endpoint para obter a pontuação atual
@app.route("/obter_pontuacao")
def obter_pontuacao():
    pontuacao = jogo.obter_pontuacao()
    return f"Pontuação atual: {pontuacao}"
