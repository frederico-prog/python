# nomes = ['Guilherme', 'Marcelo', 'Frederico', 'Marta', 'Maria']


# for i in range(len(nomes)):
#     nome = str(input('Insira um nome: ')).upper().strip()
#     nomes.append(nome)
# print(nomes)

# i = 0
# while i <= 10:
#     print('i ainda é menor do que 10.', i)
#     i += 1

# lista_frutas = ['maçã', 'goiaba', 'abacaxi', 'uva', 'pera']
#
# print(len(lista_frutas))

# numero = 0
# while True:
#     print(numero)
#     if numero == 20:
#         break
#     numero += 1
# print('Saiu do programa')

'''
EXERCÌCIO
Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e colocar em uma lista de convidados.
Após isso irá imprimir todos os nomes da lista.
'''
print('-' * 20, 'LISTA DE CONVIDADOS', '-' * 20)

lista_convidados = []

qtde_convidados = int(input('Informe o total de convidados para a lista: '))

while len(lista_convidados) < qtde_convidados:
    convidado = str(input('Informe o nome do(a) convidado(a): ')).title().strip()
    lista_convidados.append(convidado)

print('-' * 20, 'CONVIDADOS CADASTRADOS', '-' * 20)

for convidado in lista_convidados:
    print('- ', convidado)

print('Serão convidados', len(lista_convidados), 'pessoas.\n')

print('OBRIGADO POR UTILIZAR O NOSSO SISTEMA')
