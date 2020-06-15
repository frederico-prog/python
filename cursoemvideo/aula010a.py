'''
tempo = int(input('Quantos anos o seu carro tem? '))
if  tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
# Forma simplificada do IF ELSE
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('------ FIM ------')
'''
'''
nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Gustavo'
    print('Que nome lindo você tem!')
else:
    print('O seu nome é tão normal!')
print('Bom dia,{}!'.format(nome))
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m <= 6.0:
    print('A sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
#print('PARABÉNS' if m <= 6 else 'ESTUDE MAIS') -- IF simplificado