'''
15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    a- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    b- Triângulo Equilátero: três lados iguais;
    c- Triângulo Isósceles: quaisquer dois lados iguais;
    d- Triângulo Escaleno: três lados diferentes;
'''
from time import sleep

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m'
         }

print('{}****** SISTEMA DE TRIÂNGULO ******{}'.format(cores['amarelo'], cores['limpa']))

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

print('VERIFICANDO...')
sleep(3)

if ((r2 - r3) < r1 < (r2 + r3)) and ((r1 - r3) < r2 < (r1 + r3)) and ((r1 - r2) < r3 < (r1 + r2)):
    if r1 == r2 == r3:
        print('O tipo de trinângulo formado pelos segmentos {}, {} e {} é o EQUILÁTERO!'.format(r1, r2, r3))
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('O tipo de trinângulo formado pelos segmentos {}, {} e {} é o ISÓCELES!'.format(r1, r2, r3))
    else:
        print('O tipo de trinângulo formado pelos segmentos {}, {} e {} é o ESCALENO!'.format(r1, r2, r3))
else:
    print('Os segmentos digitados não formam um triângulo!')

print('********* FIM DA EXECUÇÃO DO PROGRAMA! *********')