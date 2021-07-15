import classes
from random import choice
from time import *
from os import *

def heroi():
    system('cls')
    heroi = str(input('Qual será o nome do seu herói?\n')).title()
    return heroi

def batalhar1():
    lista1 = [classes.orc_cacador, classes.orc_guerreiro, classes.orc_mago] 
    orc = choice(lista1)
    print(f'\n***Um {orc.nome} está te atacando!***\n')
    sleep(1)
    while classes.heroi.vida > 0 and orc.vida > 0:
        ataque = classes.heroi.atacar()
        orc.vida -= ataque
        if orc.vida < 0:
            orc.vida = 0
        print(f'Seu ataque desferiu {ataque} de dano. A vida do seu oponente é {orc.vida}.')
        classes.heroi.perder_vida(orc.ataque) 
        print(f'Você recebeu {orc.ataque} de dano. Sua vida é {classes.heroi.vida}\n')
        sleep(2)
    classes.heroi.exp += orc.experiencia
    print(f'Você ganhou {orc.experiencia} de experiência\n')
    input('\n\nAperte ENTER para continuar\n')
    orc.vida = 70
    classes.heroi.passar_level()
    

def batalhar2():
    lista2 = [classes.orc_cacador2, classes.orc_guerreiro2, classes.orc_mago2] 
    orc2 = choice(lista2)
    print(f'\nUm {orc2.nome} está te atacando!\n')
    sleep(1)
    while classes.heroi.vida > 0 and orc2.vida > 0:
        ataque = classes.heroi.atacar()
        orc2.vida -= ataque
        if orc2.vida < 0:
            orc2.vida = 0
        print(f'Seu ataque desferiu {classes.heroi.arma[1]} de dano. A vida do seu oponente é {orc2.vida}.')
        classes.heroi.perder_vida(orc2.ataque)
        print(f'Você recebeu {orc2.ataque} de dano. Sua vida é {classes.heroi.vida}\n')
        sleep(2)
    classes.heroi.exp += orc2.experiencia
    print(f'Você ganhou {orc2.experiencia} de experiência\n')
    orc2.vida = 140
    classes.heroi.passar_level()    

def batalharcampeao(): 
    orc = classes.campeao_orc
    print(f'\nVocê encontrou o {orc.nome}!\n')
    sleep(1)
    while classes.heroi.vida > 0 and orc.vida > 0:
        ataque = classes.heroi.atacar()
        orc.vida -= ataque
        if orc.vida < 0:
            orc.vida = 0
        print(f'Seu ataque desferiu {classes.heroi.arma[1]} de dano. A vida do seu oponente é {orc.vida}.')
        classes.heroi.perder_vida(orc.ataque)
        print(f'Você recebeu {orc.ataque} de dano. Sua vida é {classes.heroi.vida}\n')
        sleep(2)
    classes.heroi.exp += orc.experiencia
    print('Parabéns! Você derrotou o Orc Campeão!\n')
    print()
    print(f'Você ganhou {orc.experiencia} de experiência\n')
    input('\n\nAperte ENTER para continuar')
    classes.heroi.passar_level()
    system('cls')

def batalharrei(): 
    orc = classes.rei_orc
    print(f'\nVocê encontrou o {orc.nome}!\n')
    sleep(1)
    while classes.heroi.vida > 0 and orc.vida > 0:
        ataque = classes.heroi.atacar()
        orc.vida -= ataque
        if orc.vida < 0:
            orc.vida = 0
        print(f'Seu ataque desferiu {classes.heroi.arma[1]} de dano. A vida do seu oponente é {orc.vida}.')
        classes.heroi.perder_vida(orc.ataque)
        print(f'Você recebeu {orc.ataque} de dano. Sua vida é {classes.heroi.vida}\n')
        sleep(2)
    classes.heroi.exp += orc.experiencia
    rei = 'Você conseguiu! Você derrotou o Rei Orc!'
    for i in rei:
        sleep(0.02)
        print(i ,end='',flush=True)
    print()
    print(f'Você ganhou {orc.experiencia} de experiência\n')
    classes.heroi.passar_level()


def pegar_espada():
    classes.heroi.pegar_arma('Espada' , 15)
    espada = '\nA espada possui 15 de dano.\n'
    for i in espada:
        sleep(0.02)
        print(i ,end='',flush=True)
    sleep(1)

def treinar():
    treino = 'Você está treinando.'
    for i in treino:
        sleep(0.1)
        print(i ,end='',flush=True)
    print()
    print(f'Você ganhou 40 de experiência\n')
    classes.heroi.exp += 40
    classes.heroi.passar_level()

def matou_orc_campeao():
    fim1parte = 'Parabéns! Você matou o Orc campeão e o Rei está cada vez mais confiante em você. O seu caminho está sendo traçado! Na próxima versão de Blue Soul Tales você poderá derrotar o Rei Orc para se tornar o cavaleiro real mais forte de todos'
    for i in fim1parte:
        sleep(0.03)
        print(i ,end='',flush=True)
