'''
39 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto
e o número do aluno mais baixo, junto com suas alturas.
'''
codigoMaisAlto = codigoMaisBaixo = maisAlto = maisBaixo = 0

for i in range(0, 10):
    codigo = int(input('Informe o numero do aluno: '))
    altura = int(input('Informe a altura do aluno: '))
    if ('maisAlto' not in vars()) or (altura > maisAlto):
        maisAlto = altura
        codigoMaisAlto = codigo
    if ('maisBaixo' not in vars()) or (altura < maisBaixo):
        maisBaixo = altura
        codigoMaisBaixo = codigo

print(f'O aluno mais alto eh o de codigo {codigoMaisAlto} com {maisAlto}')
print(f'O aluno mais baixo eh o de codigo {codigoMaisBaixo} com {maisBaixo}')
