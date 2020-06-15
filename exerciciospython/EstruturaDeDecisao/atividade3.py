'''
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido.
'''
palavra = str(input('Insira a letra para identificar se é Masculino ou Feminino ')).strip().upper()

if palavra[0] == 'M':
    print('Masculino!!')
elif palavra[0] == 'F':
    print('Feminino!!')
else:
    print('Sexo inexistente!!')
