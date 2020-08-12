'''
4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''
lista_consoante = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
lista_letra = lista_resultado = []

for letra in range(1, 11):
    consoante = str(input(f'Informe a primeira {letra} letra: ')).upper()[0]
    lista_letra.append(consoante)

lista_resultado = [x for x in lista_letra if x in lista_arquivo_1]
print(f'As consoante digitadas foram {lista_resultado}')
