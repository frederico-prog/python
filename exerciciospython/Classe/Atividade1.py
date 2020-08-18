'''
1 - Classe Bola: Crie uma classe que modele uma bola:
    a - Atributos: Cor, circunferência, material
    b - Métodos: trocaCor e mostraCor
'''


class Bola:

    def __init__(self, cor, circunferencia, material):
        self.circunferencia = circunferencia
        self.cor = cor
        self.material = material
        print(f'COR: {self.cor}\nCIRCUNFERÊNCIA: {self.circunferencia}\nMATERIAL: {self.material}')
        print('Bola criada!')

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(f'NOVA COR: {self.cor}')


# TESTE DA CLASSE

if __name__ == '__main__':
    bola = Bola('azul', 20.5, 'plástico')
    bola.trocaCor('branca')
    bola.mostraCor()

