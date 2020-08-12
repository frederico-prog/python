'''
2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
lista_num = []
for num in range(1, 11):
    valor_str = str(input(f'Informe o {num}: ')).replace(',', '.')
    valor = float(valor_str)
    lista_num.append(valor)
lista_num.reverse()
print(lista_num)
