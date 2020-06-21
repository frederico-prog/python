class Conta:
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo

    def __str__(self):
        return f'ID: {self.ID}\nSaldo: R$ {self.saldo:.2f}'

    def __add__(self, outro):
        self.saldo += outro.saldo


Bradesco = Conta(456, 2000)
print(Bradesco)

Itau = Conta(555, 100000)
print(Itau)
Itau + Bradesco
print (Itau.saldo)



