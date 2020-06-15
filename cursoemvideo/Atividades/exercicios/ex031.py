'''
Desenvolva um programa que pergunte a distância em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
até 200Km e R$0,45 para viagens mais longas.
'''
print('***** CALCULAR VALOR DA PASSAGEM *****')
distancia = float(input('Entre com a distância a ser percorrida: '))
if distancia <= 200.0:
    valor = distancia * 0.50
    print('Para a distância de {:.2f}, o valor da passagem é de R$ {:.2f}'.format(distancia, valor))
else:
    valor = distancia * 0.45
    print('Para a distância de {:.2f}, o valor da passagem é de R$ {:.2f}'.format(distancia, valor))
print('VOLTE SEMPRE!!!')

'''
distancia = float(input('Entre com a distância a ser percorrida: '))
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será de R$ {:.2f}'.format(valor))
print('VOLTE SEMPRE!!!')
'''
