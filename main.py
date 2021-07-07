from Hist import part3
from objects import *
from Hist import *
from pygame import *
from os import *
from time import*
# mixer.init()
# mixer.music.load('data/TownTheme.mp3')
# mixer.music.play(-1)
gameAgain = 'sim'
while gameAgain == 'sim' :
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Bem vindo(a) a Blue Soul')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    input('\n\nAperte ENTER para continuar')
    system('cls')
    sleep(0.5)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    name = input('Qual nome do jogador ?:\n').title()
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    system('cls')
    sleep(0.5)
    player = Status(name)
    player.printStatus()
    part1()
    player.printStatus()
    part2()
    player.printStatus()
    part3(player)
    
    
    

        




