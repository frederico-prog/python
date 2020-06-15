'''
CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES. SEU APLICATIVO DEVERÁ ANALISAR SE A
EXPRESSÃO PASSADA ESTÁ COM OS PARÊNTESES ABERTOS E FECHADOS NA ORDEM CORRETA.
'''
expr = str(input('Digite a sua expressão: '))
pilha = list()

for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está irregular!')
