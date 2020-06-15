# RESOLUÇÃO EXERCÍCO 112
from PythonExercicios.ex112.utilidadescev import moeda
from PythonExercicios.ex112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: ')
ta = int(input('Taxa de aumento: '))
tr = int(input('Taxa de redução: '))
moeda.resumo(p, ta, tr)
