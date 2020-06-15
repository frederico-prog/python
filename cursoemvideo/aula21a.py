'''
FUNÇOES - PARTE II
- Interactive help
- Docstrings
- Argumentos opcionais
- Escopo de variáveis
- Retorno de resultados
'''

# Interactive help
# help(input)
# print(input.__doc__)

# Docstrings
# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela
#     :param i: início da contagem
#     :param f: fim fa contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='...')
#         c += p
#     print('FIM!')
#
#
# contador(2, 10, 2)
# help(contador)

# Argumentos opcionais
# def somar(a=0, b=0, c=0):
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     """
#     s = a + b + c
#     print(f'A soma vale {s}.')
#
#
# somar(3, 2, 5)
# somar(8, 4)
# somar()
# somar(b=4, c=2)
# somar(c=3, a=2)


# Escopo de variáveis
# def teste():
#     x = 8      # escopo local
#     print(f'Na função teste, N vale {n}')
#     print(f'Na função teste, X vale {x}')


# Programa principal
# n = 2    # escopo global
# print(f'No programa principal, N vale {n}')
# teste()

# def teste(b):
#     a = 8         # escopo local
#     b += 4        # escopo local
#     c = 2         # escopo local
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
#
# # Programa principal
# a = 5            # escopo global
# teste(a)
# print(f'A fora vale {a}')


# def teste(b):
#     global a      # escopo global da variáel dentro da função
#     a = 8         # escopo local
#     b += 4        # escopo local
#     c = 2         # escopo local
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
#
# # Programa principal
# a = 5            # escopo global
# teste(a)
# print(f'A fora vale {a}')


# Retorno de resultados
# def somar(a=0, b=0, c=0):
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     """
#     s = a + b + c
#     return s              # Retorna o valor da variável "S"
#
#
# r1 = somar(3, 2, 5)
# #print(somar(3, 2, 5))
# r2 = somar(2, 2)
# r3 = somar(6)
# print(f'Os resultados foram: {r1}, {r2} e {3}')

# def fatorial(num=1):

#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
#
# # n = int(input('Digite um número: '))
# # print(f'O fatorial de {n} é igual a {fatorial(n)}')
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os fatoriais são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar')

