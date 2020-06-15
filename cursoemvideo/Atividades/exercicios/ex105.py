'''
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E VAI RETORNAR UM DICIONÁRIO COM AS
SEGUINTES INFORMAÇÕES:
- QUANTIDADE DE NOTAS
- A MAIOR NOTA
- A MENOR NOTA
- A MÉDIA DA TURMA
- A SITUAÇÃO (OPCIONAL)
ADICONAR TAMBÉM AS DOCSTRINGS DA FUNÇÃO
'''


def notas(*n, sit=False):
    """
    -> função para analisar notas e situações escolares
    :param n: uma ou mais notas dos alunos (aceita várias notas)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    sala = dict()
    sala['total'] = len(n)
    sala['maior'] = max(n)
    sala['menor'] = min(n)
    sala['media'] = sum(n)/len(n)
    if sit:
        if sala['media'] >= 7:
            sala['situacao'] = 'BOA'
        elif sala['media'] >= 5:
            sala['situacao'] = 'RAZOÁVEL'
        else:
            sala['situacao'] = 'RUIM'
    return sala


# PROGRAMA PRINCIPAL
resp = notas(5.5, 2.5, 8.5, 1.0, sit=True)
print(resp)
help(notas)
