import funcoes
from time import *
from os import *

class Heroi():
    def __init__(self, nome, vida = 100, exp = 0, dia = 1, arma = ['soco' , 2], level = 1):
        self.nome = nome
        self.__vida = vida
        self.exp = exp
        self.dia = dia
        self.arma = arma
        self.level = level

    # encapsulamento do atributo vida
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, nova_vida):
        raise ValueError('Impossível alterar a vida. Apenas se altera se passar de level')

    def prox_dia(self):
        self.dia += 1
        proxdia = f'O dia se passou e você adormeceu. Estamos no {self.dia}° dia de jogo.'
        for i in proxdia:
            sleep(0.06)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar')
        return self.dia
    def pegar_arma(self, arma, dano):
        self.arma.append(arma)
        self.arma.append(dano)
        del self.arma[0]
        del self.arma[0]
        return self.arma
    def ganhar_exp(self, quantidade):
        self.exp += quantidade
        return self.exp
    def perder_vida(self, quantidade):
        self.__vida -= quantidade
        return self.__vida
    def atacar(self):
        ataque2 =  self.arma[1] - 2
        ataque3 = self.arma[1] + 2
        ataque = randint(ataque2, ataque3)
        return ataque
    def passar_level(self):
        if self.exp >= 100:
            self.exp -= 100
            self.arma[1] += 3
            self.__vida = 100
            self.level += 1
            print(f'Parabéns! Você passou para o nível {self.level}.')
            sleep(1.5)
heroi = Heroi(funcoes.heroi())

from random import randint

class Monstros():
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def perder_vida(self, quantidade):
        self.vida -= quantidade
        return self.vida
    def atacar(self):
        ataque1 = self.ataque
        ataque2 =  self.ataque - 2
        ataque3 = self.ataque + 2
        ataque = randint(ataque1, ataque2, ataque3)
        return ataque

#Herança
class Orc(Monstros):
    def __init__(self, nome, vida, ataque, experiencia):
        super().__init__(nome, vida, ataque)
        self.experiencia = experiencia

    def dar_exp(self):
        return self.experiencia

class Troll(Monstros):
    def __init__(self, nome, vida, ataque, experiencia, roubo_de_vida = 0.1):
        super().__init__(nome, vida, ataque, ataque)
        self.experiencia = experiencia
        self.roubo_de_vida = roubo_de_vida

    def atacar(self):
        ataque1 = self.ataque
        ataque2 =  self.ataque - 2
        ataque3 = self.ataque + 2                    #polimorfismo, o ataque do troll é diferente do Orc
        ataque = randint(ataque1, ataque2, ataque3)
        roubo = ataque * self.roubo_de_vida
        self.vida += roubo
        return ataque


#Criando os monstros (objetos)
orc_cacador = Orc('Orc Caçador', 70, 3, 20)
orc_guerreiro = Orc('Orc Guerreiro', 70, 3, 20)
orc_mago = Orc('Orc Mago', 70, 3, 20)
campeao_orc = Orc('Campeão Orc', 200, 5, 40)
orc_cacador2 = Orc('Orc Caçador', 140, 4, 20)
orc_guerreiro2 = Orc('Orc Guerreiro', 140, 4, 20)
orc_mago2 = Orc('Orc Mago', 140, 4, 20)
rei_orc = Orc('Rei Orc, ', 300, 7, 100)

