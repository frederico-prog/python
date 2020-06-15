'''
CONVERTE LIBRAS EM KG
'''
print('-------- SISTEMA DE CONVERSÃO --------')
print('---------------  MENU ----------------')
menu = int(input('Selecione a opção desejada: \n1- Quilograma para Libra \n2- Libra para Quilograma \n3- Sair '))
if menu == 1:
    valor = str(input('Informe o peso em quilograma: Kg ')).strip().replace(',', '.')
    quilo = float(valor)
    libra = quilo * 2.2046
    print(f'O peso {quilo:.2f} kg convertido para libras é {libra:.3f} lb.')
elif menu == 2:
    valor = str(input('Informe o peso em libras: Lb ')).strip().replace(',', '.')
    libra = float(valor)
    quilo = libra / 2.2046
    print(f'O peso {libra:.3f} lb convertido para quilogramas é {quilo:.3f} kg.')
else:
    print('Programa encerrado com sucesso!')
