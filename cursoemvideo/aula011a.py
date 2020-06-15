'''
PRIMEIRO VALOR: Para style
SEGUNDO VALOR: Para text
TERCEIRO VALOR: Para back
EX.: \033[0; 33; 44m

STYLE
0 - NONE
1 - BOLD
4 - UNDERLINE
7 - NEGATIVE

CORES
30 - BRANCO
31 - VERMELHO
32
33
34 -
35 - ROXO
36 - MAGENTA
37 - CINZA

BACK
40 - BRANCO
41 - VERMELHO
42 - VERDE
43 - AMARELO
44
45
46
47
'''
print('\033[7;30mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Frederico'
cores = {'limpa': '\033[m',    # DICIONÁRIO DE CORES
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
