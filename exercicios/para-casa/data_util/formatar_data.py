# Contém uma função formatar_data(data) que recebe um dado no formato "dd/mm/aaaa" e um formato como "aaaa-mm-dd".
# O módulo datetime é uma biblioteca incorporada ao Python que fornece classes e métodos para manipular datas e horas. 
# Ele é usado para criar objetos de data e hora, realizar operações matemáticas e lógicas com datas, 
# formatar e exibir datas, entre outras funcionalidades.

# A formatação de datas no Python é realizada através do método strftime() (string format time) 
# presente no módulo datetime.
# Esse método permite formatar um objeto de data e hora em uma string com o formato desejado.
# Para começar, é necessário importar o módulo datetime.


import datetime

# Para data no formato "aaaa-mm-dd"
def formatar_data():
    formato = "%Y-%m-%d"
    formatar_data = formatar_data.strftime(formato)
    return formatar_data


# Para data no formato "dd/mm/aaaa"
# def formatar_data1():
#     formato1 = "%d/%m/%Y"
#     formatar_data1 = formatar_data1.strftime(formato1)