from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('Rosa', 16, 'Scania', 30, 1000)
print('CAMINHÃO ROSA')
print('Cor: ', caminhao_rosa.cor)
print('Marca:', caminhao_rosa.marca)
print('Qtde de rodas:', caminhao_rosa.rodas)
print('Qtde de litros:', caminhao_rosa.tanque, 'litros')
print('Peso:', caminhao_rosa.peso, 'kilos')
caminhao_rosa.move_para_frente(20)
caminhao_rosa.abastecer(70)
print('\n')

carro_azul = Carro('Azul', 4, 'BMW', 15, 356)
print('CARRO AZUL')
print('Cor: ', carro_azul.cor)
print('Marca:', carro_azul.marca)
print('Qtde de rodas:', carro_azul.rodas)
print('Qtde de litros:', carro_azul.tanque, 'litros')
print('Peso:', carro_azul.peso, 'kilos')
carro_azul.abastecer(35)
