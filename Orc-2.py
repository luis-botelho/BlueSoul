from random import *
class Monstros():
    def __init__(self, nome, vida, ataque, experiencia):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.experiencia = experiencia

lista = [(orc_ferido = Monstros('Orc Ferido', 20, 5, 20),(orc_cacador = Monstros('Orc Caçador', 30, 10, 20),(orc_guerreiro = Monstros('Orc Guerreiro', 30, 10, 20))]
aleatorio = randint(lista)


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

