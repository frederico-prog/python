'''
4 - Classe Pessoa: Crie uma classe que modele uma pessoa:
    a - Atributos: nome, idade, peso e altura
    b - Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''


class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        print(f'NOME: {self.nome}\nIDADE: {self.idade}\nPESO:{self.peso}\nALTURA: {self.altura}')
        print('PESSOA CRIADA!')

    def envelhecer(self, idade):
        anosAntes = self.idade
        self.idade += idade
        if anosAntes < 25:
            if self.idade < 25:
                self.crescer(idade * 0.5)
            else:
                self.crescer((25 - anosAntes) * 0.5)
        print(f'PESSOA ENVELHECEU TANTO {self.crescer} ANOS!')

    def engordar(self, peso):
        self.peso += peso
        print(f'NOVO PESO: {self.peso}')

    def emagrecer(self, peso):
        if peso > self.peso:
            self.peso = 0
        else:
            self.peso -= peso
        print(f'NOVO PESO: {self.peso}')

    def crescer(self, altura):
        self.altura += altura
        print(f'NOVA ALTURA: {self.altura}')


# TESTE DA CLASSE

if __name__ == '__main__':
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    pesoStr = str(input('Peso: ')).replace(',', '.')
    peso = float(pesoStr)
    alturaStr = str(input('Altura: ')).replace(',', '.')
    altura = float(alturaStr)

    pessoa = Pessoa(nome, idade, peso, altura)
    pessoa.engordar(peso)
    pessoa.crescer(altura)
    pessoa.emagrecer(peso)
    pessoa.envelhecer(idade)
