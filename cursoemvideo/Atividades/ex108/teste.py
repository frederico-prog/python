# RESOLUÇÃO EXERCÍCO 108
import moeda

p = float(input('Informe o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo em 10%, temos {moeda.moeda(moeda.diminuir(p, 10))}')
