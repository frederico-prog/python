'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS). DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA
PALAVRA, QUAIS SÃO AS SUAS VOGAIS.
'''
import emoji
print('-=-' * 20)
print('{:^60}'.format(' VERIFICAÇÃO DE VOGAIS '))
print('-=-' * 20)

palavra = ('ARROZ', 'FEIJAO', 'MACARRAO', 'BATATA', 'LIMAO', 'LARANJA', 'CARNE', 'AZEITE', 'ALFACE', 'CEBOLA',
           'CEBOLINHA', 'FUBA', 'TRIGO', 'LEITE', 'BISCOITO')
for c in palavra:
    print(f'\nNa palavra {c.upper()} temos: ', end=' ')
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
print(emoji.emojize(f'\nVOLTE SEMPRE!! :eyes: :eyes: :eyes:', use_aliases=True))
