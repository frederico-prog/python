'''
3 - Classe Retangulo: Crie uma classe que modele um retangulo:
    a - Atributos: LadoA, LadoB (ou base e altura, ou Base e Altura, a escolher)
    b - Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve
criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''


class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        print(f'BASE: {self.base}\nALTURA: {self.altura}')
        print('RETÂNGULO CRIADO')

    def mudarLado(self):
        self.base = altura
        self.altura = base

    def retornarLado(self):
        print(f'BASE: {self.base}\nALTURA: {self.altura}')

    def calculaArea(self):
        area = self.base * self.altura
        print(f'A ÁREA DO RETÂNGULO É: {area}')

    def calculaPerimetro(self):
        perimetro = 2 * self.base + 2 * self.altura
        print(f'O PERÍMETRO DO RETÂNGULO É: {perimetro}')


# TESTE DA CLASSE

if __name__ == '__main__':
    print('CALCULAR ÁREA DO RETÂNGULO')
    base = float(input('Informe a base do retângulo: '))
    altura = float(input('Informe a altura do retângulo: '))

    retangulo = Retangulo(base, altura)
    retangulo.mudarLado()
    retangulo.retornarLado()
    retangulo.calculaArea()
    retangulo.calculaPerimetro()
