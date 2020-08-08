'''
44 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
utilizados são: 1 , 2, 3, 4  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
· O total de votos para cada candidato;
· O total de votos nulos;
· O total de votos em branco;
· A percentagem de votos nulos sobre o total de votos;
· A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''
count_voto_a = count_voto_b = count_voto_c = count_voto_d = count_voto_nulo = count_voto_branco = total_votos = 0
votos_nulos = votos_brancos = votos_validos = 0
voto = -1

while voto != 0:
    voto = int(input('Escolha o seu candidato:\n1- A\n2- B\n3- C\n4- D\n5- NULO\n6- BRANCO\n0- Sair\n'))

    if 1 <= voto <= 6:
        if voto == 1:
            count_voto_a += 1
        elif voto == 2:
            count_voto_b += 1
        elif voto == 3:
            count_voto_c += 1
        elif voto == 4:
            count_voto_d += 1
        elif voto == 5:
            count_voto_nulo += 1
        elif voto == 6:
            count_voto_branco += 1
        total_votos += 1
    else:
        print('OPÇÃO INVÁLIDA!')

if total_votos == 0:
    votos_nulos = 0
else:
    votos_nulos = (count_voto_nulo / total_votos) * 100

if total_votos == 0:
    votos_brancos = 0
else:
    votos_brancos = (count_voto_branco / total_votos) * 100

votos_validos = total_votos - (count_voto_nulo + count_voto_branco)

print('Resultado')
print(f'Total de votos: {total_votos}.')
print(f'Total de votos válidos: {votos_validos}.')
print(f'Total de votos do candidato A: {count_voto_a}.')
print(f'Total de votos do candidato B: {count_voto_b}.')
print(f'Total de votos do candidato C: {count_voto_c}.')
print(f'Total de votos do candidato D: {count_voto_d}.')
print(f'Percentual de votos nulos: {votos_nulos:.2f}%.')
print(f'Percentual de votos nulos: {votos_brancos:.2f}%.')
