from os import system
import classes
def display():
    
    separador = '=-' * 80
    line1 = "Nome: {0:^1}".format(classes.heroi.nome)
    line2 = "\U0001F499 Vida: {0:<20}".format(classes.heroi.vida) + "\U0001F31F Exp: {0:>2}".format(classes.heroi.exp)
    line3= "\U0001F4C6 Dia: {0:<20}".format(classes.heroi.dia) +  "\U0001F5E1 Arma: {0:>2}".format(classes.heroi.arma[0])
    line4 = "\U0001F3C5 Level: {0:^2}".format(classes.heroi.level)
    system('cls')
    print("{0:^100}".format(separador))
    print()
    print("{0:^160}".format(line1))
    print()
    print("{0:^160}".format(line2))
    print()
    print("{0:^160}".format(line3))
    print()
    print("{0:^160}".format(line4))
    print()
    print("{0:^160}".format(separador))
    print()
