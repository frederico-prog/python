'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
'''
print('***** VERIFICAR SE É POSSÍVEL CRIAR TRIÂNGULO A PARTIR DE 3 RETAS *****')
reta1 = float(input('Informe o primeiro segmento: '))
reta2 = float(input('Informe o segundo segmento: '))
reta3 = float(input('Informe o terceiro segmento: '))

if ((reta2 - reta3) < reta1 < (reta2 + reta3)) and ((reta1 - reta3) < reta2 < (reta1 + reta3))\
        and ((reta1 - reta2) < reta3 < (reta1 + reta2)):
    print('Os segmentos {:.2f}, {:.2f} e {:.2f} podem forma um trinâgulo!'.format(reta1, reta2, reta3))
else:
    print('Os segmentos {:.2f}, {:.2f} e {:.2f} não podem formar um trinâgulo!'.format(reta1, reta2, reta3))
