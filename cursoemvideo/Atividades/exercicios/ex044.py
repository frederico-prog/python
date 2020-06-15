'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
- À vista dinheiro/chegue: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- De 3x ou mais no cartão: 20% de juros
'''
# DICIONÁRIO DE CORES
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[7:34m',
         'verde': '\033[32m'
         }

print('{:=^40}'.format(' LOJAS FREDERICO MAGALHÃES '))
print('{:*^40}'.format('{} SISTEMA DE VENDAS {}').format(cores['amarelo'], cores['limpa']))

print('-=-' * 10)
print('{}            MENU            {}'.format(cores['azul'], cores['limpa']))
print('-=-' * 10)

menu = int(input('1- À vista \n2- Parcelado \n'))

if menu == 1:  # 1- À vista dinheiro/chegue/cartão
    menui = int(input('1- Dinheiro \n2- Chegue \n3- Cartão \n'))

    vcompra = float(input('Valor da compra: R$ '))     # valor da compra realizada pelo cliente
    desconto = vcompra - (vcompra * 10 / 100)          # desconto para pagamentos em chegue ou dinheiro
    cartao = vcompra - (vcompra * 5 / 100)             # desconto para pagamentos no carão de crédito

    if menui == 1:
        print('{}Pagamento com Dinheiro.{}'.format(cores['verde'], cores['limpa']))
        print('O valor da compra R$ {:.2f}. \nValor com desconto: R$ {:.2f}'.format(vcompra, desconto))
    elif menui == 2:
        print('{}Pagamento com Chegue.{}'.format(cores['verde'], cores['limpa']))
        print('O valor da compra R$ {:.2f}. \nValor com desconto: R$ {:.2f}'.format(vcompra, desconto))
    elif menui == 3:
        print('{}Pagamento com Cartão.{}'.format(cores['verde'], cores['limpa']))
        bandeira = str(input('Informe a bandeira do cartão: ')).strip().upper()
        print('Bandeira do cartão: {} \nO valor da compra R$ {:.2f}. \nValor com desconto: R$ {:.2f}'
              .format(bandeira, vcompra, cartao))
    else:
        print('A opção digitada não existe! Por gentileza, utilize uma das opções listadas acima.')
elif menu == 2:      # Parcelado
    menui = int(input('{}Forma de pagamento{}: \n1- Parcelado 2x vezes \n2- Parcelado 3x vezes ou mais \n'.format(
        cores['verde'], cores['limpa'])))

    if menui == 1:  # Parcelado 2x
        vcompra = float(input('Valor da compra: R$ '))
        parcela = vcompra / 2

        print('{}Pagamento em Cartão.{}'.format(cores['verde'], cores['limpa']))
        bandeira = str(input('Informe a bandeira do cartão: ')).strip().upper()
        print('{}Bandeira do cartão{}: {} \nO valor da compra R$ {:.2f}. \nValor da parcela 2x: R$ {:.2f}'.format(
            cores['verde'], cores['limpa'], bandeira, vcompra, parcela))
    elif menui == 2:  # Parceçado 3x
        vcompra = float(input('Valor da compra: R$ '))
        qtdparcelas = int(input('Informe a quantidade de parcelas: '))
        juros = vcompra + (vcompra * 20 / 100)
        vcompraparc = juros / qtdparcelas

        bandeira = str(input('Informe a bandeira do cartão: ')).strip().upper()
        print('{}Bandeira do cartão{}: {} \nO valor da compra R$ {:.2f}. \nValor da parcela {}x: R$ {:.2f}'.format(
            cores['verde'], cores['limpa'], bandeira, juros, qtdparcelas, vcompraparc))
    else:
        print('A opção digitada não existe! Por gentileza, utilize uma das opções listadas acima.')
else:
    print('A opção digitada não existe! Por gentileza, utilize uma das opções listadas acima.')

print('AGRADECEMOS A PREFERÊNCIA! VOLTE SEMPRE!')
