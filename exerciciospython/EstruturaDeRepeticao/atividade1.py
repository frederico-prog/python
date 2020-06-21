'''
1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
'''
run = True

while run:

    num = int(input('Informe um número de 0 a 10. '))

    if num < 0 or num > 10:
        print(f'O número {num} digitado não está dentro da faixa de números solicitadas!')
        erro = True
    else:
        print(f'O número {num} está dentro da faixa solicitada corretamente.')
        erro = False

    run = True if erro == True else False
# run recebe True se erro for igual a True. Senão, run recebe False
