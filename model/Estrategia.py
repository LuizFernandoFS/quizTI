# Utilizando STRATEGY para gerar perguntas randômicas ou com determinados temas
class EstrategiaPerguntas:
    def __init__(self, perguntas):
        self.perguntas = perguntas

    def gerar_perguntas_aleatorias(self, num_perguntas):
        if num_perguntas >= len(self.perguntas):
            return self.perguntas
        return random.sample(self.perguntas, num_perguntas)

    def gerar_perguntas_por_tema(self, num_perguntas, tema):
        perguntas_do_tema = Pergunta.filtrar_perguntas_por_tema(self.perguntas, tema)
        if num_perguntas >= len(perguntas_do_tema):
            return perguntas_do_tema
        return random.sample(perguntas_do_tema, num_perguntas)