area = float(input('Por favor, indique a area que tenciona pintar: ')) # Pedir a area ao utilizador


lata_grande = 18.0 # Litros
lata_pequena = 3.6 # Litros
preco_lata_grande = 80.0 # Euros
preco_lata_pequena = 25.0 # Euros
area_litro_tinta = 6.0 # Metros.sq por litro

tinta_necessaria = float(area)/area_litro_tinta # Litros de tinta necessarios para a pintura

if tinta_necessaria == 1:
    print('Vai precisar de um litro de tinta')
elif (tinta_necessaria != 1) and (tinta_necessaria > 0):
    print(f'Vai precisar de {tinta_necessaria} litros de tinta')
else:
    print('Dados errados')

latas_grandes_needed = tinta_necessaria/lata_grande # Devolve a qtdade de latas grandes necessarias para pintar a area prentendida

paint_left = tinta_necessaria%lata_grande # Devolve a qtd de tinta que fica em excesso das latas grandes

# Com base nesse excesso, vemos se o que e usado da ultima lata justifica a sua compra
# Temos o valor excessivo a partir de (3.6*4) porque e o valor em que as latas pequenas ficam mais caras que uma grande
if (lata_grande - paint_left)<(3.6*4):
    latas_pequenas_needed = (lata_grande-paint_left)/lata_pequena

# Devolve o preco da mistura

if latas_pequenas_needed != 0:
    preco_final = (preco_lata_grande*(int(latas_grandes_needed)-1))+((int(latas_pequenas_needed))*preco_lata_pequena)
else:
    preco_final = preco_lata_grande*int(latas_grandes_needed)


preco_lata_gr = latas_grandes_needed * preco_lata_grande
preco_lata_pq = preco_lata_pequena * (tinta_necessaria / lata_pequena)
print(f'Preco final {preco_final}')
print(f'Preco em latas grandes {preco_lata_gr}')
print(f'Preco em latas pequenas {preco_lata_pq}')
