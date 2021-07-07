
class Monstros():
    def __init__(self, name, life, attack, xp):
        self.name = name
        self.life = life
        self.attack = attack
        self.xp = xp
    
    def vidamonstro(self):
        return self.life
    def ataquemonstro(self):
        return self.attack

    def perder_vida(self, quant):
        self.life -= quant
        return self.life
    def atacar(self):
        atk1 = self.attack
        atk2 =  self.attack - 2
        atk3 = self.attack + 2
        atk = randint(atk1, atk2, atk3)
        return atk
    def dar_exp(self):
        return self.xp

def rondomicOrc():
    orc_mago = ('Orc Mago', 20, 5, 20)
    orc_cacador = ('Orc Caçador', 29, 8, 20)
    orc_guerreiro = ('Orc Guerreiro', 29, 8, 20)
    lista = [orc_mago,orc_cacador,orc_guerreiro]
    result = choice(lista)
    return result
enemy = rondomicOrc()
name= enemy[0]
life = enemy[1]
attack = enemy[2]
xp = enemy[3]
enemy = Monstros(name,life,attack,xp)
# print(vars(enemy))




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