'''
4 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
lista_nota = []
media = 0
for nota in range(1, 5):
    nota_str = str(input(f'Informe a {nota}: ')).replace(',', '.')
    nota = float(nota_str)
    lista_nota.append(nota)
media = sum(lista_nota) / len(lista_nota)
print(f'A média das notas digitadas foi: {media}.')