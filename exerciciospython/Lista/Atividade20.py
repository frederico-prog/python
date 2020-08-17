'''
20 - As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado
durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto
será gasto com o pagamento deste abono. Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os
representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
    a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
    a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor
    mínimo;
    a.Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos,
    impostos ou outras particularidades.
Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de
salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono
concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
    a - O salário de cada funcionário, juntamente com o valor do abono;
    b - O número total de funcionário processados;
    c - O valor total a ser gasto com o pagamento do abono;
    d - O número de funcionário que receberá o valor mínimo de 100 reais;
    e - O maior valor pago como abono;
A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada
execução do programa.

Projeção de Gastos com Abono
============================

Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0

Salário    - Abono
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
'''
from time import sleep

abono = 0.20
piso = 100.00

lista_salario = []

salario = -1
total_cadastrado = aumento = custo = valor_minimo = valor_maximo = 0

print('Informe o valor do último salário do colaborador ou digite 0 para sair.')
while salario != 0:
    salario_str = str(input('Salário R$: ')).replace(',', '.')
    salario = float(salario_str)

    if salario == 0:
        print('Inserção de dados finalizada com sucesso.')
        break

    lista_salario.append(salario)
    total_cadastrado += 1
print('CALCULANDO O VALOR DO ABONO SALARIAL.....')
print('Salário\t\t\t-\t\t\tAbono')
sleep(1)
for valor in lista_salario:
    if valor < 1000:
        aumento = piso
        valor_minimo += 1
    else:
        aumento = valor * abono
    custo += aumento

    valor_maximo = aumento

    if aumento > valor_maximo:
        valor_maximo = aumento
    sleep(0.75)
    print(f'R$ {valor:.2f}\t\t-\t\tR$ {aumento:.2f}')
print('')
print(f'Foram processados {total_cadastrado} colaboradores')
print(f'Total gasto com abonos: R$ {custo:.2f}')
print(f'Valor mínimo pago a {valor_minimo} colaboradores')
print(f'Maior valor de abono pago: R$ {valor_maximo:.2f}')

print('CÁLCULO DO SALÁRIO FINALIZADO.')
