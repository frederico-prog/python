'''
38 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    a - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    b - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    c - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que
o usuário digite o salário inicial do funcionário.
'''
anoInicial = int(input('Digite o ano da contratação: '))
salario = eval(input('Digite o valor do salário: '))
anoFinal = int(input('Digite o último ano do contrato: '))
print('')
ajuste = 0.15
anoInicial += 1
a = 1

while anoInicial <= anoFinal:
    if anoInicial <= 1995 or a == 1:
        ajuste = ajuste
    else:
        ajuste *= 2
    salario = salario + (salario * ajuste)
    print(f'{anoInicial} - ajuste de: {(ajuste * 100):.2f} ')
    print(f'Salário ajustado: {salario:.2f} \n')
    anoInicial = anoInicial + 1
