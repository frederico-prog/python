'''
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0, com
pausa de 1 segundo entre eles.
'''
from time import sleep
import emoji

print('-=-' * 15)
print('{:^40}'.format(' CONTAGEM REGRESSIVA  '))
print('-=-' * 15)

num = 10

print('Inciando a contagem!!!')
sleep(1)
for count in range(num, -1, -1):
    print(count)
    sleep(1)
sleep(0.5)
print(emoji.emojize(':boom: :boom: :boom: :boom: BOOMMM!!!! BOOMMM!!!! :boom: :boom: :boom: :boom:', use_aliases=True))
