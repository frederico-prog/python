'''
11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    a- salários até R$ 280,00 (incluindo) : aumento de 20%
    b- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    c- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    d- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        a- o salário antes do reajuste;
        b- o percentual de aumento aplicado;
        c- o valor do aumento;
        d- o novo salário, após o aumento.
'''
valor = str(input('Informe o salário do funcionário: ')).replace(',', '.')
salario = float(valor)

p1 = 0.20
p2 = 0.15
p3 = 0.10
p4 = 0.05

porcentagem1 = p1 * 100
porcentagem2 = p2 * 100
porcentagem3 = p3 * 100
porcentagem4 = p4 * 100

if salario <= 280:
    aumento = salario * p1
    salreajuste = salario + aumento
    print(f'Salário anterior: R$ {salario:.2f}\nPercentual apliacado: {porcentagem1:.0f}%\nValor do aumento: R$'
          f'{aumento:.2f}\nNovo salário: R$ {salreajuste:.2f}')
elif 280 < salario <= 700:
    aumento = salario * p2
    salreajuste = salario + aumento
    print(f'Salário anterior: R$ {salario:.2f}\nPercentual apliacado: {porcentagem2:.0f}%\nValor do aumento: R$'
          f'{aumento:.2f}\nNovo salário: R$ {salreajuste:.2f}')
elif 700 < salario <= 1500:
    aumento = salario * p3
    salreajuste = salario + aumento
    print(f'Salário anterior: R$ {salario:.2f}\nPercentual apliacado: {porcentagem3:.0f}%\nValor do aumento: R$'
          f'{aumento:.2f}\nNovo salário: R$ {salreajuste:.2f}')
elif salario > 1500:
    aumento = salario * p4
    salreajuste = salario + aumento
    print(f'Salário anterior: R$ {salario:.2f}\nPercentual apliacado: {porcentagem4:.0f}%\nValor do aumento: R$'
          f'{aumento:.2f}\nNovo salário: R$ {salreajuste:.2f}')