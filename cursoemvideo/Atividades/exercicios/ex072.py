'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE.
SEU PROGRAMA DEVERÁ RECEBER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO
'''
import emoji
print('-=-' * 20)
print('{:^60}'.format(' CONTADOR NUMÉRICO '))
print('-=-' * 20)

numeracao = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE',
             'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    num = int(input('Informe um número de 0 a 20: '))
    if num >= 0 or num >= 20:
        print(emoji.emojize(f'O número digitado foi {num} e ele é escrito desta maneira: {numeracao[num]} :clap:',
                            use_aliases=True))
    else:
        print(emoji.emojize('Número digitado está fora dos números solicitados: Tente novamente! :see_no_evil:',
              use_aliases=True))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('VOLTE SEMPRE!!!')
