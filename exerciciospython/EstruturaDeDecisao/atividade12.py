'''
12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    a- Salário Bruto até 900 (inclusive) - isento
    b- Salário Bruto até 1500 (inclusive) - desconto de 5%
    c- Salário Bruto até 2500 (inclusive) - desconto de 10%
    d- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''
valor = str(input('Informe o valor da hora trabalhada: ')).replace(',', '.')
valor2 = str(input('Informe o total de horas trabalhadas no mês: ')).replace(',', '.')

salario = float(valor)
horas = float(valor2)
salario_bruto = salario * horas

ir1 = 0.5
ir2 = 0.10
ir3 = 0.20

sindicato = 0.03
fgts = 0.11

if salario_bruto <= 900:
    desconto_sindicato = salario_bruto * sindicato
    desconto_fgts = salario_bruto * fgts
    salliquido = salario_bruto - desconto_sindicato
    total_desconto = desconto_sindicato + desconto_fgts
    print(f'Salário bruto ({salario:.2f} X {horas:.0f})\t\t\t:R$ {salario_bruto:.2f}')
    print(f'(-) IR 5%\t\t\t\t\t\t\t:ISENTO')
    print(f'FGTS 11%\t\t\t\t\t\t\t:R$ {desconto_fgts:.2f}')
    print(f'(-) Sindicato 3%\t\t\t\t\t:R$ {desconto_sindicato:.2f}')
    print(f'Total desconto:\t\t\t\t\t\t:R$ {total_desconto:.2f}')
    print(f'Salário líguido:\t\t\t\t\t:R$ {salliquido:.2f}')
elif 900 < salario_bruto <= 1500:
    desconto_sindicato = salario_bruto * sindicato
    desconto_ir = salario_bruto * ir1
    desconto_fgts = salario_bruto * fgts
    salliquido = salario_bruto - (desconto_sindicato - ir1)
    total_desconto = (desconto_sindicato + desconto_fgts + desconto_ir)
    print(f'Salário bruto ({salario:.2f} X {horas:.0f})\t\t\t:R$ {salario_bruto:.2f}')
    print(f'(-) IR 5%\t\t\t\t\t\t\t:R$ {desconto_ir:.2f}')
    print(f'FGTS 11%\t\t\t\t\t\t\t:R$ {desconto_fgts:.2f}')
    print(f'(-) Sindicato 3%\t\t\t\t\t:R$ {desconto_sindicato:.2f}')
    print(f'Total desconto:\t\t\t\t\t\t:R$ {total_desconto:.2f}')
    print(f'Salário líguido:\t\t\t\t\t:R$ {salliquido:.2f}')
elif 1500 < salario_bruto <= 2500:
    desconto_sindicato = salario_bruto * sindicato
    desconto_ir = salario_bruto * ir2
    desconto_fgts = salario_bruto * fgts
    salliquido = salario_bruto - (desconto_sindicato - ir2)
    total_desconto = (desconto_sindicato + desconto_fgts + desconto_ir)
    print(f'Salário bruto ({salario:.2f} X {horas:.0f})\t\t\t:R$ {salario_bruto:.2f}')
    print(f'(-) IR 5%\t\t\t\t\t\t\t:R$ {desconto_ir:.2f}')
    print(f'FGTS 11%\t\t\t\t\t\t\t:R$ {desconto_fgts:.2f}')
    print(f'(-) Sindicato 3%\t\t\t\t\t:R$ {desconto_sindicato:.2f}')
    print(f'Total desconto:\t\t\t\t\t\t:R$ {total_desconto:.2f}')
    print(f'Salário líguido:\t\t\t\t\t:R$ {salliquido:.2f}')
elif salario_bruto > 2500:
    desconto_sindicato = salario_bruto * sindicato
    desconto_ir = salario_bruto * ir3
    desconto_fgts = salario_bruto * fgts
    salliquido = salario_bruto - (desconto_sindicato - ir3)
    total_desconto = (desconto_sindicato + desconto_fgts + desconto_ir)
    print(f'Salário bruto ({salario:.2f} X {horas:.0f})\t\t\t:R$ {salario_bruto:.2f}')
    print(f'(-) IR 5%\t\t\t\t\t\t\t:R$ {desconto_ir:.2f}')
    print(f'FGTS 11%\t\t\t\t\t\t\t:R$ {desconto_fgts:.2f}')
    print(f'(-) Sindicato 3%\t\t\t\t\t:R$ {desconto_sindicato:.2f}')
    print(f'Total desconto:\t\t\t\t\t\t:R$ {total_desconto:.2f}')
    print(f'Salário líguido:\t\t\t\t\t:R$ {salliquido:.2f}')