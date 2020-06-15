import random


class Cliente:


    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def abrir_conta(self, valor_min):
        self.valor = valor_min
        lista_numero = random.sample(range(0, 10), 8)
        global conta, Conta
        conta = ''

        if self.idade < 18:
            print('O cliente {} é menor de idade e não pode abrir a conta'.format(self.nome))
        elif self.idade >= 18:
            if self.valor == 100:
                from conta import Conta
                for numero in lista_numero:
                    conta += str(numero)
            Conta.realizar_deposito(conta, self.valor)
            #print('Número da conta:', conta)
            print('Conta aberta com sucesso. Seu saldo inicial é de R$ {0:.2f} reais'.format(self.valor))

    def encerrar_conta(self, cpf):
        from conta import Conta
        if cpf == self.cpf:
            saldo = Conta.verifica_saldo()
            if saldo > 0:
                print('Para encerramento da conta, o saldo deve está zerado. Atualmente, você possui R$ {0:.2f}'
                      'reais de saldo'.format(saldo))
            elif saldo < 0:
                print('Para encerramento da conta, é necessário realizar o depósito de {0:.2f} reais.'.format(saldo))
            elif saldo == 0:
                print('A conta pode ser encerrada. Você possui R$ {0:.2f} reais de saldo na conta.'.format(saldo))
                print('Conta encerrada!')
        else:
            print('CPF informado inválido!')

    def __str__(self):
        return 'Cliente: ' + self.nome + '\nCPF: ' + self.cpf + '\nIdade: ' + str(self.idade) + '\nConta: ' + conta
