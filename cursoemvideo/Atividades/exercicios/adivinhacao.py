number = 42
total_tentativa = 3

for rodada in range(1, total_tentativa):
	print(f'Tentativa {rodada} de {total_tentativa}.')

	chute = int(input('Digite o seu número: '))
	print = (f'Você digitou {chute}.')

	acertou = number == chute
	maior = chute > number
	menor = chute < number

	if acertou:
		print('Você acertou!')
	elif maior:
		print('Você errou! O seu chute é maior que o número secreto.')
	elif menor:
		print('Você errou! O seu chute é menor que o número secreto.')

print('Fim de jogo!')
