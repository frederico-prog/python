'''
23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.
'''
valor = str(input('Numero original: ')).replace(',', '.')
num = float(valor)

if num == round(num):
    print("Inteiro")
else:
    print("Decimal")
    print("Arredondado pra baixo: ", round(num-0.5))
    print("Arredondado pra cima : ", round(num+0.5))
