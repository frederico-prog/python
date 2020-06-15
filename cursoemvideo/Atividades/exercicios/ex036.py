'''
Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
from time import sleep

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}

print('{}****** SISTEMA DE EMPRÉSTIMO ******{}'.format(cores['amarelo'], cores['limpa']))

nome = str(input('Informe o nome do cliente: ')).strip().upper()
salario = float(input('Informe o salário: R$ '))
casa = float(input('Informe o valor do imóvel: R$ '))
totalanual = int(input('Em quantos anos será pago o imóvel? '))

# Cacula valores básicos
meses = totalanual * 12                            # Verifica o total de meses em relação ao total de ano digitado
parcelasalario = salario * 30 / 100                # Calcula o valor referente à 30% do salário
parcela = casa / meses                             # Calcula o valor da parcela do imóvel

print('ANALISANDO....')
sleep(3)

if parcela > parcelasalario:
    print('{}REPROVADO!{} \nO empréstimo não poderá ser liberado para o cliente {}, o valor da parcela R$ {:.2f} é'
          'superior à 30% do salário: '.format(cores['vermelho'], cores['limpa'], nome, parcela))
    print('Valores negociados:')
    print('Cliente: {}\nTotal de meses: {}\nValor da parcela: R$ {:.2f}'.format(nome, meses, parcela))
else:
    print('{}APROVADO!{} \nApós a análise do sistema, o empréstimo poderá ser liberado para o cliente.'
          .format(cores['verde'], cores['limpa']))
    print('Valores negociados:')
    print('Cliente: {}\nTotal de meses: {}\nValor da parcela: R$ {:.2f}'.format(nome, meses, parcela))
print('Obrigado pela confiança. Volte sempre!')

print('********* FIM DA EXECUÇÃO DO PROGRAMA! *********')
