import json

# Carregando dados do JSON
class LoadData:
    @staticmethod
    def getJson(filename):
        dados_json = {}
        with open(filename, "r") as arquivo_json:
            dados_json = json.load(arquivo_json)
        return dados_json