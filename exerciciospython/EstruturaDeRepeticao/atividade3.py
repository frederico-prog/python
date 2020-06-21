'''
3 - Faça um programa que leia e valide as seguintes informações:
    a- Nome: maior que 3 caracteres;
    b- Idade: entre 0 e 150.
    c- Salário: maior que zero.
    d- Sexo: 'f' ou 'm'.
    e- Estado Civil: 's', 'c', 'v', 'd'.
'''
nome = input("Digite o seu nome: ").upper().strip()
while len(nome) <= 3:
    nome = input("Digite o seu nome[MAIOR QUE 3 CARACTERES]: ")
idade = int(input("Digite a sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Digite a sua idade[ENTRE 0 E 150]: "))
salario = float(input("Digite o seu salário: "))
while salario <= 0:
    salario = float(input("Digite o seu salário[MAIOR QUE 0]: "))
sexo = input("Digite o seu sexo [f, m]: ").upper().strip()
while sexo not in 'MF':
    sexo = input("Digite o seu sexo[f OU m]: ")
estado_civil = input("Digite o seu estado cívil [s, c, v, d]: ").upper().strip()
while estado_civil not in 'SCVD':
    estado_civil = input("Digite o seu estado civil[s, c, v, d]: ")
