'''
TRATAMENTOS DE ERRO E EXCEÇÕES
 - ERRO DE SINTAXE
 - ERRO DE SEMÂNTICA
'''
# n = int(input('Número: '))
# print(f'Você digitou o número {n}')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema cos os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'A divisão de {a} / {b} é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
