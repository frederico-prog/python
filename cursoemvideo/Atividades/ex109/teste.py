# RESOLUÇÃO EXERCÍCO 109
import moeda

p = float(input('Informe o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo em 10%, temos {moeda.diminuir(p, 10, True)}')
