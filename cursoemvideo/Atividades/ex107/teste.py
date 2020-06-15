# RESOLUÇÃO EXERCÍCO 107
from PythonExercicios.ex107.moeda import *

p = float(input('Informe o preço: R$ '))
print(f'A metade de {p} é R$ {metade(p)}')
print(f'O dobro de {p} é R$ {dobro(p)}')
print(f'Aumentando em 10%, temos R$ {aumentar(p, 10)}')
print(f'Diminuindo em 10%, temos R$ {diminuir(p, 10)}')
