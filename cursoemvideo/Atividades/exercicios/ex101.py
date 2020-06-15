'''
CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO DE UMA PESSOA, RETORNANDO UM VALOR
LITERAL INDICANDO SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES.
'''


def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        resp = f'Com {idade} anos: VOTO NEGADO!'
    elif idade <= 16 or idade < 18 or idade > 65:
        resp = f'Com {idade} anos: VOTO OPCIONAL'
    else:
        resp = f'Com {idade} anos: VOTO OBRIGATÓRIO'
    return resp


# PROGRAMA PRINCIPAL
ano = int(input('Informe o ano de nascimento: '))
print(voto(ano))


