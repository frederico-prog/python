class Meu_Objeto:
    def __init__(pessoa, nome, idade):
        pessoa.nome = nome
        pessoa.idade = idade
        print('Chamando o construtor')

    def imprime(pessoa):
        print(f'Olá meu nome é {pessoa.nome} e eu tenho {pessoa.idade} anos de idade.')



#Programa principal
nome = str(input('Digite o seu nome: ')).strip().upper()
idade = int(input('Digite a sua idade: '))
usuario = Meu_Objeto(nome, idade)
usuario.imprime()
