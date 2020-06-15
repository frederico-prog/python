'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
'''
import emoji
print('-=-' * 15)
print('{:^40}'.format(' NÚMEROS PARES  '))
print('-=-' * 15)
'''for count in range(1, 51):
    if count % 2 == 0:
        print(count, end=' ')'''
for count in range(2, 51, 2):
    print(count, end=' ')
print(emoji.emojize('\n:frog: :frog: FIM DA EXECUÇÃO!!! :frog: :frog:', use_aliases=True))
