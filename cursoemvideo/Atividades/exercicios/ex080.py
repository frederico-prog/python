'''
CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA
DE INSERÇÃO(SEM USAR O SORT()). NO FINAL, MOSTRE A LISTA ORDENADA NA TELA.
'''
lista = []

for c in range(0, 5):
    num = int(input(f'Insira o {c + 1}º número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-*-' * 25)
print(f'Os valores digitados em ordem foram {lista}.')