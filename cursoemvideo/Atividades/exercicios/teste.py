def jogada(msg):
    nivel = str(input(msg))
    total_de_pontos = 1000
    global number
    number = 42

    if nivel.isnumeric():
        valor = int(nivel)
    if valor == 1:
        total_tentativa = 20
        for rodada in range(0, total_tentativa):
            print(f'Tentativa {rodada+1} de {total_tentativa}.')

            chute = int(input('Digite o seu número: '))
            print(f'Você digitou {chute}.')

            acertou = number == chute
            maior = chute > number
            menor = chute < number

            if acertou:
                print('Você acertou!')
                break
            elif maior:
                print('Você errou! O seu chute é maior que o número secreto.')
                total_de_pontos = total_de_pontos - (chute - number)
            elif menor:
                print('Você errou! O seu chute é menor que o número secreto.')
                total_de_pontos = total_de_pontos - (number - chute)
    elif valor == 2:
        total_tentativa = 10
        for rodada in range(0, total_tentativa):
            print(f'Tentativa {rodada + 1} de {total_tentativa}.')

            chute = int(input('Digite o seu número: '))
            print(f'Você digitou {chute}.')

            acertou = number == chute
            maior = chute > number
            menor = chute < number

            if acertou:
                print('Você acertou!')
                break
            elif maior:
                print('Você errou! O seu chute é maior que o número secreto.')
                total_de_pontos = total_de_pontos - (chute - number)
            elif menor:
                print('Você errou! O seu chute é menor que o número secreto.')
                total_de_pontos = total_de_pontos - (number - chute)
    else:
        total_tentativa = 5
        for rodada in range(0, total_tentativa):
            print(f'Tentativa {rodada + 1} de {total_tentativa}.')

            chute = int(input('Digite o seu número: '))
            print(f'Você digitou {chute}.')

            acertou = number == chute
            maior = chute > number
            menor = chute < number

            if acertou:
                print('Você acertou!')
                break
            elif maior:
                print('Você errou! O seu chute é maior que o número secreto.')
                total_de_pontos = total_de_pontos - (chute - number)
            elif menor:
                print('Você errou! O seu chute é menor que o número secreto.')
                total_de_pontos = total_de_pontos - (number - chute)


nivel = jogada('Selecione o nível para o jogo: \n1- 20 Tentativas \n2- 10 Tentativas \n3- 5 Tentativas \n')

print('Fim de jogo!')
print(f'O seu total de pontos foi {total_de_pontos}.')
