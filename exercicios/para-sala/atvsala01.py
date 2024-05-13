'''**Exercício 1: Crie um Pacote de Matemática**

Crie um pacote Python chamado "matematica" que inclua módulos para realizar operações matemáticas básicas,
como adição, subtração, multiplicação e divisão. 
Crie um programa principal que importe esses módulos e realize operações matemáticas com eles.'''

import math

def soma(a,b):
    return a + b

def sub( a,b):
    return a - b

def produto(a,b):
    return a * b
def div(a,b):
    if b != 0:
        return a / b
    else:
        print("Indeterminação")