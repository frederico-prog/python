from cliente import Cliente


class Conta:

    def __init__(self):
        pass

    def verifica_saldo(self, valor):
        if valor == 100:
            return 0

    def realizar_deposito(self, conta, valor):
        saldo = self.verifica_saldo(valor)
        if saldo == 0:
            saldo += valor
            print('Depósito realizado com sucesso! Seu saldo atual é de R$ {} reais.'.format(saldo))
