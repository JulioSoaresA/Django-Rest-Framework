import re

CELULAR_REGEX = r'^\([1-9]{2}\) [9][6-9][0-9]{3}-[0-9]{4}$'

def cpf_invalido(cpf):
    numeros = [int(digito) for digito in cpf if digito.isdigit()]
    
    if len(numeros) != 11:
        return True
    
    # Cálculo do primeiro dígito verificador
    soma_produtos = sum(a * b for a, b in zip(numeros[0:9], range(10, 1, -1)))
    digito_esperado = (soma_produtos * 10 % 11) % 10
    if digito_esperado == 10 or digito_esperado == 11:
        digito_esperado = 0
    
    if numeros[9] != digito_esperado:
        return True
    
    # Cálculo do segundo dígito verificador
    soma_produtos = sum(a * b for a, b in zip(numeros[0:10], range(11, 1, -1)))
    digito_esperado = (soma_produtos * 10 % 11) % 10
    if digito_esperado == 10 or digito_esperado == 11:
        digito_esperado = 0
    
    if numeros[10] != digito_esperado:
        return True

def nome_invalido(nome):
    return not nome.isalpha()   

def celular_invalido(celular):
    # Verifica se o número tem o tamanho correto
    if len(celular) != 15:
        return True
    
    # Verifica se o número segue o formato específico
    if not re.match(CELULAR_REGEX, celular):
        return True
