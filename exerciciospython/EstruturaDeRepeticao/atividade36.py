'''
36 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a
tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35

Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''
print('TABUADA')
num = int(input('Digite o número: '))
comeca = int(input('Começar por: '))
termina = int(input('Termina em: '))

produto = 0

if termina < comeca:
    print(f'O valor digitado para terminar a tabuada não pode ser menor do que o valor digitado para começar'
          f'a tabuada.')
else:
    for n in range(comeca, termina + 1):
        produto = num * n
        print(f'{n} X {num} = {produto}')

