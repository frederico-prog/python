# print('Hello World!\tSegundo print! - Utilizando a tabulação')
# print('Hello World!\nSegundo print! - Utilizando a quebra de linha')

# nome = 'Frederico'
# idade = 41
# altura = 1.78
#
#
# print(nome, 'tem', idade, 'anos e possui', altura, 'de altura')

# nome = input('Escreva o seu nome: ').title()
# idade = input('Sua idade: ')
# altura = input('Sua altura: ')
#
#
# print(nome, 'tem', idade, 'anos e possui', altura, 'de altura')
# print(type(nome), type(altura), type(idade))

# numero1 = 10
# numero2 = 2
# numero3 = 5.5
# resultado = numero1 **(1/2)
# print(resultado)

'''
EXERCÍCIO:
Faça um formulário que pergunte o nome, cpf, endereço, idade altura e telefone e imprima em um formulário
organizado.
'''

print('-' * 20, 'CADASTRO DE USUÁRIOS', '-' * 20)

nome = str(input('Nome: ')).title().strip()
cpf = str(input('CPF: ')).strip()
idade = int(input('Idade: '))
endereco = str(input('Endereço: ')).title().strip()
telefone = str(input('Telefone: ')).strip()
altura = str(input('Altura: ')).strip()

print('-' * 20, 'USUÁRIO CADASTRADO', '-' * 20)
print('Nome: {}\nCPF: {}\nIdade: {} anos\nEndereço: {}\nTelefone: {}\nAltura: {}'.format(nome, idade, cpf, endereco, telefone, altura))