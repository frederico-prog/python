'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex.: APÓS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / O LOBO AMA O BOLO / ANOTARAM A DATA DA MARATONA
'''
print('-=-' * 12)
print('{:^35}'.format(' PALÍNDROMO '))
print('-=-' * 12)

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = '''''
inverso = junto[::-1]   # TÉCNICA DE FATIAMENTO DA FRASE
'''for letra in range(len(junto), -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} e {}.'.format(junto, inverso))
if inverso == junto:
    print('Esta frase é um PALÍNDROMO')
else:
    print('Esta frase não é um PALÍNDROMO')

print('***** FIM DA EXECUÇÃO *****')
