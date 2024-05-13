import csv

dados = [['Aline', 8, 30], ['Fabio', 5, 20]]

with open ('alunos.csv','w', newline='') as aluno_csv:
    escritor_csv= csv.writer(aluno_csv)
    escritor_csv.writerows(dados)   
    print(dados)

with open ('alunos.csv') as aluno_file:
    leitor_csv = csv.reader(aluno_file)
    notas = []

    for linha in leitor_csv:
        nota = int(linha[1])
        notas.append(nota)

print(sum(notas) / len(notas))
