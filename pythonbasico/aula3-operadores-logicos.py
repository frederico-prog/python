'''
Comparações: == != > < >= <=
Comparções: and or
'''

# var_verdade = True
# var_falso = False
# #
# # print(var_falso, var_veradeiro)
#
# if var_verdade == True:
#     print('Var_verdade é verdadeiro!')
#
# a = 2
# b = 20
#
# if a > b:
#     print(a, 'é maior do que', b)
# else:
#     print(a, 'não é maior do que', b)

# print('Menu:\n1 = Escreve Frederico\n2 = Escreve João\n3 = Escreve Maria\n')
#
# opcao = int(input('Escolha uma opção:'))
#
# if opcao == 1:
#     print('Frederico')
# elif opcao == 2:
#     print('João')
# elif opcao == 3:
#     print('Maria')
# else:
#     print('Opção errada, tente novamente!')

# idade = 50
#
# if not idade == 50:
#     print('Você não tem 50 anos.')
# else:
#     print('Você tem 50 anos.')


'''
EXERCÍCIO:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decida se ela está apta a ser do Exercíto.
Para entrar no exercíto é preciso ter mais de 18 anos, pesar mais ou igual a 60 kilos e medir mais ou igual a 1,70 metros.
'''

print('-' * 20, ' CÁLCULO ALISTAMENTO MILITAR ', '-' * 20)

nome = str(input('Digite o nome: ')).title().strip()
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

if idade >= 18 and peso >= 60.0 and altura >= 1.70:
    print('O candidato {} está apto para se alistar: ', nome)
else:
    print('O candidato {} ainda não está apto a se alistar.'.format(nome))