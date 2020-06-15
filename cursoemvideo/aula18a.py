'''
Variáveis compostas
- Tuplas - não são imutáveis ()
- Listas [Parte 2] - podem ser mutáveis []
'''

'''
dado = list()
dado.append('Pedro')
dado.append(25)
print(dado[0])
print(dado[1])

pessoas = list()
pessoas.append(dado[:])

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])    # Saida: Pedro
print(pessoas[1][1])    # Saída: 19
print(pessoas[2][0])    # Saída: João
print(pessoas[1])       # Saída: ['Maria', 19]
'''
'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])
print(galera[0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])    # Cria a cópia da lista DADO [:]
    dado.clear()
print(f'Lista GALERA é composta por {galera}')
# print(f'Lista DADO é composta por {dado}')

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
