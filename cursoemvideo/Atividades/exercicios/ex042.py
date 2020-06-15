'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados são iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados são diferentes.
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
