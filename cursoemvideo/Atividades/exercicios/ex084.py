'''
FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
A- QUANTAS PESSOAS FORAM CADASTRADAS.
B- UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
C- UMA LISTAGEM COM AS PESSOAS MAIS LEVES.
'''
pessoas = []
listapessoa = []
maior = menor = 0

while True:
    pessoas.append(str(input('Insira o nome do paciente: ')).strip().upper())
    pessoas.append(float(input('Insira o peso em KG do paciente: ')))
    if len(listapessoa) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    listapessoa.append(pessoas[:])
    pessoas.clear()

    resp = str(input('Deseja cadastrar um novo paciente? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print('-*-' * 30)
# print(f'Os dado cadastrados foram: {listapessoa}')
print(f'Total de pessoas cadastradas foram de {len(listapessoa)} pacientes.')
print(f'O maior peso foi de {maior}kg. Peso de ', end=' ')
for p in listapessoa:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor o peso foi de {menor}kg. Peso de ', end=' ')
for p in listapessoa:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
