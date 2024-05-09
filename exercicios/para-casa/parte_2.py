# 1. Solicite ao usuário que insira seus dados de nascimento no formato "dd/mm/aaaa" 
# e utilize a função do módulo calculo_idade.pypara calcular a idade da pessoa.

# 2. Verifique se o ano atual é bissexto ou não está usando a função do módulo ano_bissexto.py.

# 3. Solicite ao usuário que insira dados no formato "dd/mm/aaaa" 
# e use a função do módulo formatar_data.py para exibir dados no formato "aaaa-mm-dd".

from data_util import ano_bissexto, calculo_idade, formatar_data

def menu():
    print("Escolha a conversão que deseja realizar:")
    print("1. Calcular a sua idade")
    print("2. O ano atual é bissexto?")
    print("3. Mudar o formato da data")
    print("0. Sair")
    
def main():
    while True:
        menu()
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            ano_nascimento = float(input("Digite o ano do seu nascimento: "))
            ano_atual = float(input("Digite o ano atual: "))   
            idade = calculo_idade.calcular_idade(ano_nascimento, ano_atual)
            print(ano_nascimento, ano_atual, "A sua idade hoje é de ", idade, "anos.")

        elif opcao == '2':
            eh_ano_bissexto = float(input("Digite o ano atual: "))
            ano = ano_bissexto.eh_ano_bissexto(ano)
            print(ano, "O ano de ", ano, "é bisexto?")

        elif opcao == '3':
            formatar_data = float(input("Digite a data que você quer formatar: "))
            formato = formatar_data.formatar_data()
            print(formato, "A data formatada é", formato, ".")
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()