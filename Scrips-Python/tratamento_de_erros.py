"""
try:
    x = int(input('Digite um número: '))
except:
    print('Deu erro, insira apenas números.')
    x = 0
finally:
    print(f'O valor digitado foi o número {x}')
"""

class ValorRepetidoErro(Exception):
    def __init__(self, n):
        self.num = n
    
    def __str__(self):
        return (f'Vixe! Você já digitou o número {self.num} antes.')

def main():
    lista = []

    for i in range(8):
        while True:
            try:
                num = int(input('Digite um valor: '))
                break
            except ValueError:
                print('Digite apenas números')

        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetidoErro(num)


main()
                
    
