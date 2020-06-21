'''
2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.
'''
run = True

print('O usuário e a senha não podem ser iguais.')

while run:
    nome = str(input('Login: ')).strip()
    senha = str(input('Senha: ')).strip()

    if nome == senha:
        print('Erro! Favor verificar o usuário e a senha.')
        erro = True
    else:
        print(f'Usuário {nome.title()} criado com sucesso.')
        erro = False

    run = True if erro == True else False

print(' ')
print('SISTEMA DE CADASTRO DE SENHA PYTHON')
