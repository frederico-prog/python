'''
18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
arquivo = float(input("Informe do tamanho do arquivo em MegaByte: "))
link = float(input("Informe a velocidade do link em Mbps: "))
tempo = ((arquivo * 8) / link) / 60
print(f'O tempo aproximado de download é de {tempo:.2f} minutos')