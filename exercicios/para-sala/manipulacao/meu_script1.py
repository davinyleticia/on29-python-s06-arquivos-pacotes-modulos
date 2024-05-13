"""with open('dados.txt', 'r') as arquivo: # por alguma razão ele nao encontra meu arquivo txt
    conteudo= arquivo.read() # para ler tudo"""

with open('C:/Users/Pam/2024/Reprograma/Aula 6/on29-python-s06-arquivos-pacotes-modulos/exercicios/para-sala/manipulacao/dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
