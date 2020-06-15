'''
w - write
r - read
a - append
b - utilizado para abrir arquivos em formatos difentes do txt
'''

arquivo = open('arquivo.txt', 'r')
# arquivo = open('arquivo.txt', 'w')
# arquivo = open('arquivo.txt', 'a')
# arquivo = open('imagem.png', 'rb')

for linha in arquivo:
    print(linha)

# for i in range(0, 1001):
#     arquivo.write(str(i) + '\n')
