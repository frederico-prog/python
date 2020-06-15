'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela
abaixo:
- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal
- Entre 25 até 30: Sobrepeso
- Entre 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''
from time import sleep

# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m'
         }

print('{}****** SISTEMA DE CÁLCULO DO IMC ******{}'.format(cores['amarelo'], cores['limpa']))

paciente = str(input('Digite o nome do paciente: ')).strip().upper()
altura = float(input('Digite a altura em metros(m): '))
peso = float(input('Digite o peso em quilos(Kg): '))

imc = peso / (altura ** 2)

print('AVALIANDO O PESO E ALTURA DO PACIENTE {}'.format(paciente))
sleep(3)

if imc < 18.5:
    print('O paciente {} está abaixo do peso. \nO seu IMC é {:.1f}.'.format(paciente, imc))
elif 18.5 <= imc < 25.0:
    print('O paciente {} está no peso ideal. \nO seu IMC é {:.1f}.'.format(paciente, imc))
elif 25.0 <= imc < 30.0:
    print('O paciente {} apresenta caso de Sobrepeso. \nO seu IMC é {:.1f}.'.format(paciente, imc))
elif 30.0 <= imc < 40.0:
    print('O paciente {} apresenta caso de Obesidade. \nO seu IMC é {:.1f}.'.format(paciente, imc))
else:
    print('O paciente {} apresenta caso de Obesidade Mórbida. \nO seu IMC é {:.1f}.'.format(paciente, imc))

print('********* FIM DA EXECUÇÃO DO PROGRAMA! *********')
