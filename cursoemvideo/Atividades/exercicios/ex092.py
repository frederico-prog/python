'''
CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E CADASTRE-OS(COM IDADE) EM UM DICIONÁRIO SE POR
ACASO A CTPS FOR DIFERENTE DE ZERO, O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E ACRESCENTE,
ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.
'''
from datetime import date
cadprofissional = dict()
profissional = list()
while True:
    cadprofissional['nome'] = str(input('Nome do contribuinte: ')).upper()
    cadprofissional['sexo'] = str(input('Informe o sexo: \n"M" - Masculino ou "F" - Feminino ')).strip().upper()[0]
    anonasc = int(input(f'Ano de nascimento do contribuinte {cadprofissional["nome"].upper()}: '))
    while anonasc < 1900:
        anonasc = int(input(f'Ano de nascimento do contribuinte {cadprofissional["nome"]}: '))
    if anonasc > 1900:
        cadprofissional['ano'] = anonasc
    anoatual = date.today().year
    cadprofissional['idade'] = anoatual - cadprofissional['ano']
    resp = int(input('O contribuinte possui carteira de trabalho? \nDigite 0 para "NÃO" ou 1 para "SIM".'))
    if resp == 0:
        cadprofissional['ctps'] = 'NÃO POSSUI'
        cadprofissional['aposentadoria'] = 'AINDA NÃO É CONTRIBUINTE'
        cadprofissional['trestante'] = 'AINDA NÃO POSSUI TEMPO MÍNIMO'
    elif resp == 1:
        ctrabalho = int(input('Informe o número da CTPS do funcionário: '))
        if ctrabalho < 8:
            print('Número da carteira de trabalho incorreta.')
        else:
            cadprofissional['ctps'] = ctrabalho
            cadprofissional['anocontratacao'] = int(input('Informe o ano de contratação do contribuinte: '))
            cadprofissional['salario'] = float(input('Informe o salário do contribuinte: R$ '))
            cadprofissional['tempocontribuicao'] = anoatual - cadprofissional['anocontratacao']   # VERIFICA O TEMPO DE CONTRIBUIÇÃO
            if cadprofissional['tempocontribuicao'] >= 15 or cadprofissional['tempocontribuicao'] < 30:
                cadprofissional['aposentadoria'] = 'CONTRIBUINTE TEM O DIREITO A 60% DE APOSENTADORIA'
                cadprofissional['trestante'] = cadprofissional['tempocontribuicao']
            elif cadprofissional['tempocontribuicao'] > 30 or cadprofissional['tempocontribuicao'] < 45:
                cadprofissional['aposentadoria'] = 'CONTRIBUINTE TEM O DIREITO A 80% DE APOSENTADORIA'
                cadprofissional['trestante'] = cadprofissional['tempocontribuicao']
            elif cadprofissional['tempocontribuicao'] < 45:
                cadprofissional['aposentadoria'] = 'CONTRIBUINTE TEM O DIREITO A 100% DE APOSENTADORIA'
                cadprofissional['trestante'] = cadprofissional['tempocontribuicao']
            else:
                cadprofissional['aposentadoria'] = 'NÃO ATINGIU O TEMPO MÍNIMO'
                cadprofissional['trestante'] = 15 - cadprofissional['tempocontribuicao']
    else:
        print('Opção inválida!')
    profissional.append(cadprofissional.copy())
    resp1 = str(input('Deseja cadastrar um novo comntribuinte? "C" para continuar e "S" para sair. ')).strip().upper()[0]
    while resp1 not in 'CS':
        resp1 = str(input('Deseja cadastrar um novo comntribuinte? "C" para continuar e "S" para sair. ')).strip().upper()[0]
    if resp1 == 'S':
        break
print('-=' * 40)
print(f'{"Nome":^10}{"Sexo":^5}{"Idade":^10}{"CTPS":^15}{"Tempo restante":^20}{"Aposentadoria":^35}')
print('-' * 100)
for k, v in enumerate(profissional):
    print(f'{v["nome"]:^10}{v["sexo"]:^5}{v["idade"]:^10}{v["ctps"]:^15}{v["trestante"]:^20}{v["aposentadoria"]:^35}')


'''
from datetime import datetime
dado = dict()
dado['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dado['idade'] = datetime.now().year - nasc
dado['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dado['ctps'] != 0:
    dado['contratacao'] = int(input('Ano de contratação: '))
    dado['salario'] = float(input('Salário: R$ '))
    dado['aposentadoria'] = dado['idade'] + ((dado['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dado.items():
    print(f'  - {k} tem o valor {v}')
'''