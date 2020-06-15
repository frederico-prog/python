'''
MÓDULOS E PACOTES - AULA 22

MODULARIZAÇÃO

 - SURGIU NO INÍCIO DA DÉCADA DE 60
 - SISTEMAS FICANDO CADA VEZ MAIORES
 - FOCO: DIVIDIR UM PROGRAMA GRANDE
 - FOCO: AUMENTAR A LEGIBILIDADE
 - FOCO: FACILITAR A MANUTENÇÃO

VANTAGENS

 - ORGANIZAÇÃO DO CÓGIDO
 - FACILIDADE NA MANUTENÇÃO
 - OCULTAÇÃO DE CÓDIGO DETALHADO
 - REUTILIZAÇÃO EM OUTROS PROJETOS
'''
# from uteis import fatorial, dobro, triplo - NÃO É RECOMENDADO UTILIZAR A IMPORTAÇÃO DESTA MANEIRA
from uteis import numeros


num = int(input('Digite um valor: '))
#fat = uteis.fatorial(num)
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
#print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
#print(f'O triplo de {num} é {uteis.triplo(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
