from random import *
class Monstros():
    def __init__(self, nome, vida, ataque, experiencia):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.experiencia = experiencia
    
    def vidamonstro(self):
        return self.vida
    def ataquemonstro(self):
        return self.ataque

    def perder_vida(self, quantidade):
        self.vida -= quantidade
        return self.vida
    def atacar(self):
        ataque1 = self.ataque
        ataque2 =  self.ataque - 2
        ataque3 = self.ataque + 2
        ataque = randint(ataque1, ataque2, ataque3)
        return ataque
    def dar_exp(self):
        return self.experiencia
   

def rondomicOrc():
    orc_mago = ('Orc Mago', 20, 5, 20)
    orc_cacador = ('Orc Caçador', 29, 8, 20)
    orc_guerreiro = ('Orc Guerreiro', 29, 8, 20)
    lista = [orc_mago,orc_cacador,orc_guerreiro]
    result = choice(lista)
    return result
inimico = rondomicOrc()
nome= inimico[0]
vida = inimico[1]
ataque = inimico[2]
xp = inimico[3]
inimigo = Monstros(nome,vida,ataque,xp)
print(vars(inimigo))




#Criando os monstros (objetos)
# orc_ferido = Monstros('Orc Ferido', 20, 5, 20)
# orc_cacador = Monstros('Orc Caçador', 30, 10, 20)
# orc_guerreiro = Monstros('Orc Guerreiro', 30, 10, 20)
# orc_mago = Monstros('Orc Mago', 30, 10, 20)
# campeao_orc = Monstros('Orc Campeão', 80, 12, 40)
# orc_cacador2 = Monstros('Orc Caçador', 60, 15, 20)
# orc_guerreiro2 = Monstros('Orc Guerreiro', 60, 15, 20)
# orc_mago2 = Monstros('Orc Mago', 60, 15, 20)
# rei_orc = Monstros('Rei Orc, ', 200, 15, 100)
# lista = [orc_mago,orc_cacador,orc_guerreiro]