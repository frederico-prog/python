'''
CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM ESTÁ ACESSÍVEL PELO COMPUTADOR USADO.
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0:31mO Site não está disponível.\033[m')
else:
    print('O site está disponível.')
    print(site.read())            # Obtem o código HTML do site
