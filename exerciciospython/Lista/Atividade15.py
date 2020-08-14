'''
15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de
dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    a - Mostre a quantidade de valores que foram lidos;
    b - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    d - Calcule e mostre a soma dos valores;
    e - Calcule e mostre a média dos valores;
    f - Calcule e mostre a quantidade de valores acima da média calculada;
    g - Calcule e mostre a quantidade de valores abaixo de sete;
    h - Encerre o programa com uma mensagem;
'''
resposta = soma = media = qtde = qtde7 = 0
lista_notas = []

print('Responda "-1" para sair do sistema.')

while resposta != -1:
    resposta_str = str(input('Informe a nota: '))
    resposta = float(resposta_str)

    if resposta == -1:
        break
    else:
        lista_notas.append(resposta)

soma = sum(lista_notas) # D
media = soma / len(lista_notas) # E
lista_notas.reverse() # C

print(f'QUANTIDADE DE NOTAS DIGITADAS: {len(lista_notas)}') # A
print(F'NOTAS DIGITADAS: {lista_notas}') # B
print(F'NOTAS DIGITADAS EM ORDEM INVERSA: {lista_notas}') # C
print(f'A SOMA DAS NOTAS FOI DE: {soma:.2f}') # D
print(F'A MÉDIA DAS SOMAS É DE: {media:.2f}') # E

for nota in lista_notas:
    if nota > media: # F
        qtde += 1
    if nota < 7: # G
        qtde7 += 1

print(f'QUANTIDADE DE NOTAS ACIMA DA MÉDIA CALCULADA: {qtde}') # F
print(f'QUANTIDADE DE NOTAS ABAIXO DE 7 PTOS: {qtde7}') # G

print('VOLTE SEMPRE!!!') # H
