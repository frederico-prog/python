'''
2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
'''

num = str(input('Insira um número: ')).strip()
parsernum = float(str(num).replace(',', '.'))
print('O número formado foi:', parsernum)