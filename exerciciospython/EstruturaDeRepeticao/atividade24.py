'''
24 - Faça um programa que calcule o mostre a média aritmética de N notas.
'''
media = soma = count = 0

while True:
    num = str(input('Informe o número: ')).replace(',', '.').strip()
    valor = float(num)
    soma += valor
    count += 1
    media = soma / count

    resp = ' '
    sair = False
    while resp not in 'SN':
        resp = str(input('Você deseja continuar? [S/N]')).upper().split()[0]
        if resp == 'N':
            sair = True
    if sair:
        break
print(' ')
print(f'Total de números digitado: {count}')
print(f'A soma foi {soma} e a média foi {media}')
