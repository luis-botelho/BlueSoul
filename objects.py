from os import *
from time import *
from random import *
class Status():
    def __init__(self, name, life = 100, stamina = 100, experience = 0, time = 1, weapon = ['Soco',0], gold = 0):
        self.life = life 
        self.stamina = stamina 
        self.experience = experience
        self.time = time 
        self.name = name   
        self.weapon = weapon
        self.gold = gold 
    def printStatus(self):
        system('cls')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'                                {self.name}                                  ')
        print(f'                      \U0001F499 Vida: {self.life}',end="              ")
        print(f'\U0001F525 Energia: {self.stamina}')#\U00026A1
        print(f'                      \U0001F3AF Nivel: {self.experience}',end='             ')
        print(f'\U0001F315 Horário: {self.time}')
        print(f'                               \U0001F5E1 Arma atual: {self.weapon[0]}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    def pickup(self,item):
        if item == 'Espada':
            self.weapon[0] = item
            self.weapon[1] = 3
        elif item == 'Ouro':
            self.Ouro = randint(5,20)

