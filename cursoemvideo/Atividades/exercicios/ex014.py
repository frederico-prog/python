# Crie um algoritmo que converta a temperatura de celsius para fahrenheit
c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) + 5) + 32
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(c, f))
