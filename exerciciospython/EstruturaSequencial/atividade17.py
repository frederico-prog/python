'''
17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    a - comprar apenas latas de 18 litros;
    b - comprar apenas galões de 3,6 litros;
    c - misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os
    valores para cima, isto é, considere latas cheias.
'''
import math

print('Calculo para verificar quantas latas/galões de tintas serão necessarias e o valor delas')

METROS = float(input("Entre com o tamanho em metros quadrados da área a ser pintada: "))

METROSLATAS = METROS / 6

if (METROSLATAS <= 0):
    METROSLATAS = 1

QTDLATAS18 = math.floor(METROSLATAS / 18 + (18 * 0.10))
QTDGALOES36 = math.floor(METROSLATAS / 3.6 + (3.6 * 0.10))
QTDLATAS = METROSLATAS / 18
RESTO = METROSLATAS % 18

if (RESTO > 0 and RESTO <= 3.6):
    QTDGALOES = 1
elif (RESTO == 0):
    QTDGALOES = 0
else:
    QTDGALOES = math.floor(RESTO / 3.6 + (3.6 * 0.10))

if (QTDLATAS18 <= 0 or QTDGALOES36 <= 0 or QTDGALOES < 0):
    QTDGALOES36 = 1
    QTDLATAS18 = 1
    QTDGALOES = 1

PRECOLATAS18 = QTDLATAS18 * 80
PRECOGALOES36 = QTDGALOES36 * 25
PRECOLATAS = QTDLATAS * 80
PRECOGALOES = QTDGALOES * 25

PRECOTIMO = PRECOLATAS + PRECOGALOES

print(f'\nQuantidade de latas: {QTDLATAS18} latas. Preço latas: R$ {PRECOLATAS18:.2f}.\nQuantidades galões: {QTDGALOES36}'
      f' galões. Preço galões: {PRECOGALOES36:.2f}.\nSolução Otima, latas: {QTDLATAS} e galões: {QTDGALOES} Valor: R$ {PRECOTIMO:.2f}')

