metros = input("Digite a quantidade de metros quadrados a serem pintados: ")
litros = float(metros)/3

precoL = 80.0
capacidadeL = 18

latas = litros / capacidadeL
total = latas * precoL

print(f'Você usara {latas} latas de tinta')
print(f'O preco total é de: R$ {total}')
