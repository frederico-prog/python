class Veiculo:


    def __init__(self, cor, rodas, marca, tanque, peso):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        self.peso = peso


    def abastecer(self, litros):
        abastecimento = self.tanque + litros

        if abastecimento > 110:
            return print('Tanque já está na sua capacidade total! Não precisa abastecer.')
        else:
            if abastecimento == 50:
                return print('Você abasteceu {} litros. Tanque completo!'.format(litros))
            elif abastecimento < 50:
                return print('Você abasteceu {} litros. Fim do abastecimento!'.format(litros))


    def move_para_frente(self, velocidade):
        self.velocidade = velocidade

        if self.velocidade == 0:
            print('Carro parado')
        elif self.velocidade == 10:
            print('Carro em primeira marcha')
        elif self.velocidade == 20:
            print('Carro em segunda marcha')