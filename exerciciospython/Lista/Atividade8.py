'''
8 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
'''
lista_resultado = []

for d in range(0, 2):
    lista_dado = []
    idade = int(input(f'Informe a idade da {d + 1}ª pessoa: '))
    altura_str = str(input(f'Informe a altura da {d + 1}ª pessoa: ')).replace(',', '.')
    altura = float(altura_str)

    lista_dado.append(idade)
    lista_dado.append(altura)

    # Inverte a lista com os dados inseridos
    lista_dado.reverse()

    # Inseri a lista de dados invertidos na lista de resultados juntamente com a pessoa D
    lista_resultado.append(d + 1)
    lista_resultado.append(lista_dado)

# Inverte os dados inseridos na lista de resultados antes da impressão
lista_resultado.reverse()
print(f'Lista invertida: {lista_resultado}')
