from os import *
from time import *
from random import *
from Orcs import * 
class Status():
    def __init__(self, name, life = 100, stamina = 100, experience = 0, time = 1, weapon = 3, gold = 0):
        self.life = life 
        self.stamina = stamina 
        self.experience = experience
        self.time = time 
        self.name = name   
        self.weapon = weapon
        self.gold = gold 

    def ataqueHeroi(self):
        return self.weapon

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
    
    def batalha(self):
        while inimigo.vida > 0 and self.life > 0: 
            ataqueheroi = randint(heroi.weapon - 1, heroi.weapon +1)           
            inimigo.vida-=ataqueheroi
            ataqueinimigo = randint(inimigo.ataque - 1, inimigo.ataque +1)
            self.life -= ataqueinimigo
            if inimigo.vida < 0:
                inimigo.vida = 0
            if self.life < 0:
                self.life = 0
            print( 'vida Heroi', self.life, 'Vida Orc',inimigo.vida)


heroi = Status('Seila') # Estas duas linhas são apenas para verificar seu a luta esta correta, apagar no futuro.
heroi.batalha()



                



