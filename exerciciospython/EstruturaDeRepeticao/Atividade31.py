'''
31 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
'''
print('Lojas Tabajara')

sair = 1

while sair != 0:
    soma = 0
    a = 1
    valor = eval(input('Digite o valor do produto ou 0 para finalizar: '))
    while valor > 0:
        soma = soma + valor
        print(f'Produto {a} R$ {valor:.2f}')
        a = a + 1
        valor = eval(input('Digite o valor do produto ou 0 para finalizar: '))

    if soma > 0:
        print(f'Total R$: {soma:.2f}')
        formaPagamento = int(input('Digite (1)-Cartao / (2)-Dinheiro: '))
        if formaPagamento == 2:
            quantDinheiro = eval(input('Informe o valor pago: '))
            troco = quantDinheiro - soma
        else:
            troco = 0
        print(f'Troco de R$ {troco:.2f}')
    sair = int(input('Digite 0 para sair ou 1 para continuar: '))
