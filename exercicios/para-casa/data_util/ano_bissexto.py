"""def eh_ano_bissexto(anobi):
    if anobi % 4 == 0:
        if anobi % 100 != 0:
            if anobi % 400 == 0:
                return True
            else:
                return False
        return True
    return True"""

def eh_ano_bissexto(anobi):
    if anobi % 4 == 0:
        if anobi % 100 != 0:
            return True
    if anobi % 400 != 0:
        return False