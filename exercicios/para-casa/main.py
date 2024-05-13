from datetime import date
from data_util.calculo_idade import calcular_idade
from data_util.ano_bissexto import eh_ano_bissexto



# pedir ao usuários seus dados de nascimento
dia = int(input('Informe seu dia de nascimento: '))
mes = int(input('Informe seu mês de nascimento: '))
ano = int(input('Informe seu ano de nascimento: '))

# armazenar a data de nascimento para calcular a idade e formatar
data_nascimento = date(ano, mes, dia)
idade = calcular_idade(data_nascimento)
print(f"Você nasceu em {data_nascimento.strftime('%d/%m/%Y')}\nA sua idade é: {idade} anos") # formatar a data de nascimento de acordo com d/m/a e mostrar a idade


ano_bissexto = eh_ano_bissexto(ano)

if ano_bissexto: 
    print(f"O {ano} é bissexto")
else:
    print(f"O {ano} não é bissexto")