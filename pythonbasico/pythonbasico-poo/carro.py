from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, rodas, marca, tanque, peso):
        Veiculo.__init__(self, cor, rodas, marca, tanque, peso)


    def abastecer(self, litros):
        abastecimento = self.tanque + litros

        if abastecimento > 50:
            return print('Tanque já está na sua capacidade total! Não precisa abastecer.')
        else:
            if abastecimento == 50:
                return print('Você abasteceu {} litros. Tanque completo!'.format(litros))
            elif abastecimento < 50:
                return print('Você abasteceu {} litros. Fim do abastecimento!'.format(litros))