'''
10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
turno = str(input('Digite M para Matutino ou V para Vespertino ou N para Noturno: ')).upper().strip()

if turno[0] == 'M':
    print('Bom dia!')
elif turno[0] == 'V':
    print('Boa tarde!')
elif turno[0] == 'N':
    print('Boa noite!')
else:
    print(f'Valor digitado "{turno[0]}" inválido.')
