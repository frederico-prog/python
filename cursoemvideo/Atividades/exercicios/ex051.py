'''
Desenvolva um programa que leia o primeiro termo e a razão de PA(Progressão aritimética). No final, mostre os 10
primeiros termos desta progressão.
'''
print('-=-' * 12)
print('{:^35}'.format(' PROGESSÃO ARITIMÉTICA(PA) - v1.0 '))
print('-=-' * 12)

primeiro = int(input('Informe o primeiro elemento: '))
razao = int(input('Informe a razão: '))
elemento = int(input('Quantidade de elementos para exibir: '))

ultimo = primeiro + (elemento - 1) * razao          # FÓRMULA APLICADA a(n) = a(1) + (n-1).r
ultimo = ultimo + 1

for count in range(primeiro, ultimo, razao):
    print(count, end=' » ')

print('\n***** FIM DA EXECUÇÃO *******')
