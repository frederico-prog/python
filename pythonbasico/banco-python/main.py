'''
crie um software de gerenciamento bancário.
este software deve ser capaz de criar clientes e contas
cada cliente possui nome, cpf, idade
cada conta conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo
'''
from cliente import Cliente

cliente = Cliente('Frederico Gustavo Magalhães', '03324901650', 18)
cliente.abrir_conta(100)
print(cliente)