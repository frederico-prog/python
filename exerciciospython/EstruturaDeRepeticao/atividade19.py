'''
19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
'''
print('-=-' * 20)
print('{:^60}'.format(' TRATANDO VÁRIOS VALORES 2 - v1.0 '))
print('-=-' * 20)

count = maior = menor = soma = 0
resp = 'S'
retorno = True

while resp in 'Ss':
    num = int(input('Informe o número: '))
    soma += num
    count += 1
    if num < 0 or num > 1000:
        print(f'Número digitado não está entre 0 e 1000')
        retorno = False
    else:
        if count == 1:
            maior = menor = soma = num
            retorno = True
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
            retorno = True

    resp = str(input('Deseja continuar? Digite S para continuar e N para parar: ')).upper().strip()[0]

if retorno is True:
    print(f'Foram digitado {count} números.')
    print(f'O maior número é o {maior} e o menor é {menor}.')
    print(f'A soma dos números digitados foi: {soma}')
else:
    print('Nenhum número válido diigitado.')
