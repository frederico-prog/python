'''
FUNÇÕES - PARTE I
'''
# def lin():
#     print('-' * 30)


'''
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


# PROGRAMA PRINCIPAL
mensagem('   SISTEMA DE ALUNOS   ')
mensagem('   SISTEMA DE INFORMAÇÃO   ')
'''

'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    print('-' * 25)


# PROGRAMA PRINCIPAL
soma(b=4, a=5)
soma(4, 5)
soma(8, 9)
soma(2, 1)
'''

'''
#EMPACOTAR
def contator(* num):
    print('-' * 30)
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


contator(2, 1, 7)
contator(8, 0)
contator(4, 4, 7, 6, 2)
'''

'''
# PASSAGEM DE LISTA COMO PARÂMETRO
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


valores = [7, 2, 5, 0, 4] # Declaração de uma lista
print(valores)
dobra(valores)
'''

# DESEMPACOTAR
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


# PROGRAMA PRINCIPAL
soma(5, 2)
soma(2, 9, 4)
