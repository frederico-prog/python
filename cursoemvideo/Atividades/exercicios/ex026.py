'''
Crie um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez.
'''
frase = str(input('Digite a sua frase: ')).strip()
contagem = frase.upper().count('A')
print('Analisando a frase "{}"...'.format(frase.upper()))
print('Na frase "{}", a letra "A" aparece {} veze(s).'.format(frase.upper(), contagem))
print('Na frase "{}", a letra "A" aparece na posição {} pela primeira vez.'.format(frase.upper(), frase.upper().
                                                                                   find('A') + 1))
print('Na frase "{}", a letra "A" aparece na posição {} pela última vez.'.format(frase.upper(), frase.upper().
                                                                                 rfind('A') + 1))
