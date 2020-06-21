class Animal:
    def __init__(anim, cor, genero, andar):
        anim.cor = cor
        anim.genero = genero
        anim.num_de_patas = andar


    def falar(anim):
        print('Olá sou um cachorro e sei falar!')


    def andar(anim):
        if anim.num_de_patas == 4:
            print(f'Estou andando sobre {anim.num_de_patas} patas')
        print(f'Estou andando sobre {anim.num_de_patas} pés')
                


    def amamentar(anim):
        if anim.genero.lower()[0] == 'm':
            print('Machos não amamentam')
            return
        print('Amamentando o meu filhote')


#Rex = Animal('marron', 'femea', 4)
#Rex.falar()
#Rex.andar()
#Rex.amamentar()



class Pessoa(Animal):
    def __init__(anim, cor, genero, andar, cabelo):
        super(Pessoa, anim).__init__(cor, genero, andar)
        anim.cabelo = 'Preto'

    def falar(anim):
        super(Pessoa, anim).falar()
        print('Olá sou uma pessoa e sei falar!')


Hugo = Pessoa('preto', 'maculino', 2, 'preto')
Hugo.falar()
