numero_secreto = 42
total_de_pontos = 1000

nivel = int(input('Selecione o nível para o jogo: \n1- 20 Tentativas \n2- 10 Tentativas \n3- 5 Tentativas \n'))

if nivel == 1:
    total_tentativa = 20
    for rodada in range(0, total_tentativa):
        print(f'Tentativa {rodada+1} de {total_tentativa}.')

        chute = int(input('Digite o seu número: '))
        print(f'Você digitou {chute}.')

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você acertou!')
            break
        elif maior:
            print('Você errou! O seu chute é maior que o número secreto.')
            total_de_pontos = total_de_pontos - (chute - numero_secreto)
        elif menor:
            print('Você errou! O seu chute é menor que o número secreto.')
            total_de_pontos = total_de_pontos - (numero_secreto - chute)
elif nivel == 2:
    total_tentativa = 10
    for rodada in range(0, total_tentativa):
        print(f'Tentativa {rodada + 1} de {total_tentativa}.')

        chute = int(input('Digite o seu número: '))
        print(f'Você digitou {chute}.')

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você acertou!')
            break
        elif maior:
            print('Você errou! O seu chute é maior que o número secreto.')
            total_de_pontos = total_de_pontos - (chute - numero_secreto)
        elif menor:
            print('Você errou! O seu chute é menor que o número secreto.')
            total_de_pontos = total_de_pontos - (numero_secreto - chute)
else:
    total_tentativa = 5
    for rodada in range(0, total_tentativa):
        print(f'Tentativa {rodada + 1} de {total_tentativa}.')

        chute = int(input('Digite o seu número: '))
        print(f'Você digitou {chute}.')

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você acertou!')
            break
        elif maior:
            print('Você errou! O seu chute é maior que o número secreto.')
            total_de_pontos = total_de_pontos - (chute - numero_secreto)
        elif menor:
            print('Você errou! O seu chute é menor que o número secreto.')
            total_de_pontos = total_de_pontos - (numero_secreto - chute)

print('Fim de jogo!')
print(f'O seu total de pontos foi {total_de_pontos}.')
