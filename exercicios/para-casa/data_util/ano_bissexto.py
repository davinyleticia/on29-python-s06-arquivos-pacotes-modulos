# Contém uma função eh_ano_bissexto(ano) que verifica se um ano é bissexto e retorna True ou False.

# Condições para ano  bisesxto:
# Ano divisível por 4 e;
# Ano divisível por 100 e por 400, ao mesmo tempo.

def eh_ano_bissexto(ano):
  if (ano % 4) == 0:
    if (ano % 100) == 0:
      if (ano % 400) == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False