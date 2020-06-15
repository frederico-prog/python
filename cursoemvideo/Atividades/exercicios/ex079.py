'''
CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS UM LISTA. CASO O NÚMERO JÁ EXISTA
LÁ DENTRO, ELE NÃO SERÁ ADICIONADO. NO FINAL, SERÃO EXIBIDIDOS TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE.
'''
lista = []
while True:
    num = int(input('Insira um número: '))
    if num not in lista:
        lista.append(num)
        print('Número inserido.')
    else:
        print('Número digitado já existe na lista e não será inserido.')
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Os números digitados foram: {lista}')
lista.sort()
print('A ordem crescente dos números foi: ')
print('VOLTE SEMPRE!!!')
