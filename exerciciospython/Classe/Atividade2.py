'''
2 - Classe Quadrado: Crie uma classe que modele um quadrado:
    a - Atributos: Tamanho do lado
    b - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''


class Quadrado:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        print(f'TAMANHO: {self.tamanho}')
        print('Quadrado criado!')

    def mudarValor(self, tamanho):
        self.tamanho = tamanho

    def retornaLado(self):
        print(f'NOVO TAMANHO: {self.tamanho}')

    def calcularArea(self):
        area = self.tamanho * self.tamanho
        print(f'A área do quadrado é: {area}')


# TESTE DA CLASSE

if __name__ == '__main__':
    quad1 = Quadrado(4)
    quad1.mudarValor(6)
    quad1.retornaLado()
    quad1.calcularArea()
