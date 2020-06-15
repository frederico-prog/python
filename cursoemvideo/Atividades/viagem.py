# Variável para cotrolar meu while (caso queira rodar o programa novamente)
run = True
while run:
    print()
    print("==== CALCULADORA DE CUSTOS DE VIAGENS - VEÍCULO/AVIÃO ====")
    print()
    # Lista com os precos dos combustiveis (ordem: gasolina, etanol, gnv, diesel)
    lista_precos_combustiveis = [4.29, 2.15, 3.24, 3.35]

    # Outro while e variavel para controlar se digitar outra opcao alem de 1 ou 2
    opcao = True
    while opcao:
        tipo_viagem = int(input(" # Meio de Transporte (Digite: 1-Veículo, 2-Avião): "))
        if tipo_viagem == 1 or tipo_viagem == 2:
            opcao = False
        else:
            print("Opção: " + str(tipo_viagem) + " inválida - Opções válidas somente 1-Veículo, 2-Avião")
            print("Por favor, tente novamente!")
            opcao = True

    # Variaveis que o usuário vai dar entrada
    quantidade_trechos = int(input(" # Quantos trechos? (1 - Somente ida, 2 - Ida e Volta) "))
    quantidade_pessoas = int(input(" # Quantas pessoas? "))
    dias_viagem = int(input(" # Quantos dias no total (com ou sem hospedagem)? "))
    dias_hospedagem = int(input(" # Quantos dias de hospedagem? "))
    # Se nao vai se hospedar nao tem porque pedir o preco da hospedagem por dia
    if dias_hospedagem != 0:
        custo_diario_hospedagem = float(input(" # Quanto custa a diária de hospedagem? "))
    else:
        custo_diario_hospedagem = 0
    refeicoes_por_dia = int(input(" # Quantas refeições FORA por dia? "))
    orcamento_por_refeicao = float(input(" # Qual é o limite de gasto/refeição/pessoa/dia? "))

    # Calculos por categoria que é em comum para viagem com veiculo ou avião
    custos_hospedagem = dias_hospedagem * custo_diario_hospedagem
    custos_alimentacao = quantidade_pessoas * orcamento_por_refeicao * refeicoes_por_dia * dias_viagem

    # Se for viagem tipo 1 (veiculo)
    if tipo_viagem == 1:
        # coleta do usuário os dados/variaveis
        distancia_em_km = int(input(" # Quantos KM até seu destino? "))
        autonomia_veiculo = float(input(" # Quantos KM/L seu veículo faz? "))
        custo_pedagio_trecho = float(input(" # Quanto de pedágio até seu destino? "))
        outras_despesas = float(input(" # Qualquer outra despesa? "))

        # Lista com os custos dos combustiveis (ordem: gasolina, etanol, gnv, diesel)
        custos_combustiveis = []
        for preco in lista_precos_combustiveis:
            custos_combustiveis.append(distancia_em_km / autonomia_veiculo * preco * quantidade_trechos)

        custos_pedagio = custo_pedagio_trecho * quantidade_trechos

        # Lista com os custos da viagem por combustiveis (ordem: gasolina, etanol, gnv, diesel)
        custos_viagem_por_combustivel = []
        for custo_combustivel in custos_combustiveis:
            custos_viagem_por_combustivel.append(
                custo_combustivel + custos_pedagio + custos_hospedagem + custos_alimentacao + outras_despesas)

        # Arredondando para 2 casas decimais o custo total por combustivel
        custos_viagem_por_combustivel = ["%.2f" % round(elem, 2) for elem in custos_viagem_por_combustivel]

        # Mostrando na tela o preco de cada combustivel e demais categorias
        print()
        print("================ RESULTADO PARA VIAGEM DE VEÍCULO =============")
        print()
        print(
            "Custos GASOLINA - (TRANSPORTE + PEDÁGIOS): \tR$ " + str(
                "%.2f" % round(custos_combustiveis[0] + custos_pedagio, 2)))
        print(
            "Custos ETANOL - (TRANSPORTE + PEDÁGIOS): \tR$ " + str(
                "%.2f" % round(custos_combustiveis[1] + custos_pedagio, 2)))
        print("Custos GNV - (TRANSPORTE + PEDÁGIOS): \t\tR$ " + str(
            "%.2f" % round(custos_combustiveis[2] + custos_pedagio, 2)))
        print(
            "Custos DIESEL - (TRANSPORTE + PEDÁGIOS): \tR$ " + str(
                "%.2f" % round(custos_combustiveis[3] + custos_pedagio, 2)))

        print()
        print("Custos com HOSPEDAGEM: \t\tR$ " + str("%.2f" % round(custos_hospedagem, 2)))
        print("Custos com ALIMENTACAO: \tR$ " + str("%.2f" % round(custos_alimentacao, 2)))
        print("Custos com OUTRAS DESPESAS: \tR$ " + str("%.2f" % round(outras_despesas, 2)))

        print()
        print("Custo Total da sua viagem - GASOLINA: \tR$ " + str(custos_viagem_por_combustivel[0]))
        print("Custo Total da sua viagem - ETANOL: \tR$ " + str(custos_viagem_por_combustivel[1]))
        print("Custo Total da sua viagem - GNV: \tR$ " + str(custos_viagem_por_combustivel[2]))
        print("Custo Total da sua viagem - DIESEL: \tR$ " + str(custos_viagem_por_combustivel[3]))

    # se for tipo avião
    elif tipo_viagem == 2:
        # Coleta variaveis do usuario
        preco_passagem_pessoa = int(input(" # Qual o preço da passagem/pessoa/trecho? "))
        despesa_uber = float(input(" # Qual o valor de um trecho de Uber/Taxi até o aeroporto? "))
        dias_locacao_carro = int(input(" # Quantos dias de locação de carro? "))
        # Nao tem porque pedir preco por dia da locacao do carro se nao vai locar o carro
        if dias_locacao_carro != 0:
            locacao_carro_dia = float(input(" # Qual o preço da locação do carro/dia? "))
        else:
            locacao_carro_dia = 0
        outras_despesas = float(input(" # Qualquer outra despesa? "))

        custos_passagens = quantidade_pessoas * preco_passagem_pessoa * quantidade_trechos
        custos_uber_taxi = despesa_uber * quantidade_trechos
        custos_locacao_carro = locacao_carro_dia * dias_locacao_carro

        custo_aviao_total = custos_passagens + custos_uber_taxi + custos_locacao_carro + custos_alimentacao + custos_hospedagem

        # Mostrar na tela os resultados
        print()
        print("================ RESULTADO PARA VIAGEM DE AVIÃO =============")
        print()
        print("Custos PASSAGENS + UBER/TAXI: \tR$ " + str("%.2f" % round(custos_passagens + custos_uber_taxi, 2)))
        print("Custos com HOSPEDAGEM: \t\tR$ " + str("%.2f" % round(custos_hospedagem, 2)))
        print("Custos com ALIMENTACAO: \tR$ " + str("%.2f" % round(custos_alimentacao, 2)))
        print("Custos com OUTRAS DESPESAS: \tR$ " + str("%.2f" % round(outras_despesas, 2)))

        print()
        print("Custo Total da sua viagem: \tR$ " + str(custo_aviao_total))

    # aqui pedimos ao usuario se deseja rodar novamente o mesmo programa
    print()
    executar_novamente = input("Deseja executar novamente? (s = sim, qualquer tecla = não) ")
    run = True if executar_novamente.lower() == 's' else False

print()
print("Até a próxima viagem!")
