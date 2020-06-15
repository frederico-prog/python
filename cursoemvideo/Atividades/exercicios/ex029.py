'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
import random
print('***** RADAR ELETRÔNICO *****')
from datetime import datetime, timedelta, date
#velocidade = float(input('Entre com a velocidade do veículo: '))
velocidade = random.uniform(30.0, 199.00)
maxima = 80.0
if velocidade <= maxima:
    print('Velocidade registrada: {:.2f}'.format(velocidade))
    print('O seu veículo não ultrapassou a velocidade máxima permitida. PARABÉNS!')
else:
    print('Velocidade registrada: {:.2f}'.format(velocidade))
    print('O seu veículo ultrapassou a velocidade máxima permitida! VOCÊ SERÁ MULTADO!')
    multa = (velocidade - maxima) * 7
    data = (date.today() + timedelta(days=30))
    print('O valor da sua multa é de R$ {:.2f}. Esta mula deverá ser paga até o dia {}.'.format(multa, data.strftime('%d/%m/%Y')))
print('Tenha um bom dia! Dirija com segurança! \nFoi um prazer te atender. Volte Sempre!')
