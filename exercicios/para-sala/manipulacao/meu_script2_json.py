import json

with open("c:/Users/Pam/2024/Reprograma/Aula 6/on29-python-s06-arquivos-pacotes-modulos/exercicios/para-sala/manipulacao/dados.json", 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)