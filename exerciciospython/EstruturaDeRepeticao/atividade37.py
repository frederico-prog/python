'''
37 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua
altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao
encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e
do mais magro, além da média das alturas e dos pesos dos clientes
'''
cod_clientes = []
altura_clientes = []
peso_clientes = []
ncliente = 1
codigo = True

while codigo != 0:
    print(f'\nCliente n° {ncliente}')
    codigo = int(input('Digite o código: '))
    if codigo == 0:
        print('Fim do programa!')
        break
    else:
        alturastr = str(input('Digite a altura: ')).replace(',', '.')
        altura = float(alturastr)
        pesostr = str(input('Digite o peso: ')).replace(',', '.')
        peso = float(pesostr)
        cod_clientes.append(codigo)
        altura_clientes.append(altura)
        peso_clientes.append(peso)
        ncliente += 1

codmagro = peso_clientes.index(min(peso_clientes))
codgordo = peso_clientes.index(max(peso_clientes))
codalto = altura_clientes.index(max(altura_clientes))
codbaixo = altura_clientes.index(min(altura_clientes))
mediaaltura = sum(altura_clientes) / len(altura_clientes)
mediapeso = sum(peso_clientes) / len(peso_clientes)
print('\n' * 5)
print(f'Código do mais magro: {cod_clientes[codmagro]}')
print(f'Código do mais gordo: {cod_clientes[codgordo]}')
print(f'Código do mais alto: {cod_clientes[codalto]}')
print(f'Código do mais baixo: {cod_clientes[codbaixo]}')
print(f'Média de altura: {mediaaltura:.2f}m')
print(f'Média de peso: {mediapeso:.2f}Kg')
