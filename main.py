from Hist import part3
from objects import *
from Hist import *
from pygame import *
from os import *
from time import*
<<<<<<< Updated upstream
mixer.init()
mixer.music.load('C:\Github/blueMod1\projetos/blueSoulTales\data/TownTheme.mp3')
mixer.music.play(-1)
=======
# mixer.init()
# mixer.music.load('C:\Users\BrenBarrios\Desktop\Aulas\Projeto final Modulo 1 _ Blue Soul Kingdom _\BlueSoul\data\TownTheme.mp3')
# mixer.music.play(-1)
>>>>>>> Stashed changes
gameAgain = 'sim'
while gameAgain != 'NAO':
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Bem vindo(a) a Blue Soul')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    input('Aperte enter para continuar')
    system('cls')
    sleep(0.5)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    name = input('Qual nome do jogador ?:\n').title()
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    system('cls')
    sleep(0.5)
    player = Status(name)
    player.printStatus()
    # part1()
    player.printStatus()
    # part2()
    player.printStatus()
    condition = part3(player)
    if condition == 'Game Over':
        gameAgain = gameOver()
    else:
        pass
<<<<<<< Updated upstream
    

        




=======
>>>>>>> Stashed changes
