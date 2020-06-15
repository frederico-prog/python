'''
16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
valor = str(input('Informe o total da área a ser pintada: ')).replace(',', '.')
area = float(valor)

precoL = 80
capacidadeL = 18

latas = (area * 3) / capacidadeL
custo = round(latas) * precoL

print(f'Para pintar uma área de {area:.2f}m. Serão necessárias {latas:.0f} latas de tintas.')
print(f'O seu custo total é de R$ {custo:.2f}')
