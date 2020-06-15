# Faça um algoritmo que calcule o valor do pagamento de uma compra à vista e à prazo. À vista recebe 5% de desconto e
# a prazo tem um acréscimo de 8%.
print('******** DESAFIO - AULA 07 - CALCULADORA 7 *********')
produto = float(input('Informe o valor da compra: R$ '))
avista = produto - (produto * 5 / 100)
aprazo = produto - (produto * 8 / 100)
print('A compra feita no valor de R${:.2f}, sairá a R${:.2f} à vista ou R${:.2f} à prazo.'.format(produto, avista,
                                                                                                   aprazo))
