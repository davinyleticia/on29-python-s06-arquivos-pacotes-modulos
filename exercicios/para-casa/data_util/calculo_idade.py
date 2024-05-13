from datetime import date

def calcular_idade(data_nascimento):

    data_atual= date.today()
    print(f"Data de hoje: {data_atual.strftime('%d/%m/%Y')}")
    
#calcular a idade comparando somente o ano de nascimento
    idade = data_atual.year - data_nascimento.year
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1

#    print(f"Você tem {idade} anos.")
    return idade