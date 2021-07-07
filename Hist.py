from objects import *
from time import *

def part1():
    part1 = 'Mais um dia se passou no reino Blue Soul, você está apreciando o crepúsculo apor um longo dia de trabalho de campo, e o único que consegue sentir é que esse não é o seu lugar. Você sonha com aventuras, desafios e conquistas. A vida de um simples plebeu não é mais suficiente para você, mas a partir de hoje tudo vai mudar, agora você está decidido a realizar as escolhas necessárias para mudar a sua vida e se tornar o maior cavalheiro do reino.'
    for i in part1:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar')
def part2():
    part2 = 'A lua cheia nasce no horizonte, iluminando os vastos campos ao seu redor, de repente o galopar de um cavalo ecoa pelo silencio do campo, atraído pelas suaves brisas do verão. La distante, onde começa a floresta sem fim, emerge um cavalo branco, refletindo a luz do luar, manchado com a sangue do seu cavalheiro que sobre ele varia entre a vida e a morte. Sem duvidar você corre na direção do seu encontro esperando poder evitar o destino desse cavalheiro.'
    for i in part2:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar')
def part3(ask,game):
    part3 = 'Enquanto a distancia entre vocês é encurtada a vida do cavalheiro é perdida a cada galopar do seu cavalo, para quando seu encontro sucede o destino já está traçado. O cavalo cansado e machucado para frente a você, seu instinto indica que já está fora de perigo, sobre ele esta o corpo sem vida do seu companheiro.\n'
    part4 = 'O rugido de um Orc ecoa brutalmente, rasgando o silencio da noite. Você sente o arrepio pelo seu corpo e a morte sussurra ao seu ouvido, o único que você pode sentir é que seu futuro será a morte, uma morte longa e dolorosa, como a do cavalheiro a sua frente.'
    part5 = 'Um Orc caçador corre em sua direção, a sede de sangue nos seus olhos brilha com um vermelho intenso na noite, sua velocidade diminui as distancias entre vocês tão rápido que em segundos você percebe que tem que tomar uma decisão ou a sua morte será inevitável.'
    for i in part3:
        sleep(0.01)
        print(i ,end='',flush=True)
    choice = int(input('\n[1] Ir embora e fingir que nada aconteceu.\n\n[2] Buscar pertences de valor e abandonar o cavalo e o corpo.\n\n[3] Pegar a espada do cavalheiro por se aparece alguém ou algo.\n\nFaça sua escolha:\n'))
    if choice == 1:
        ask.printStatus()
        for i in part4:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar')
        ask.printStatus()
        for i in part5:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar')
        choice = int(input('\nOque você fará:\n\n[1] Tentar correr\n\n[2] Pegar a espada'))
        if choice == 1:
            system('cls')
            print('█▀▀█ █▀▀█ █▀▄▀█ █▀▀▀   █▀▀▀█ █░░▒█ █▀▀▀ █▀▀█')
            print('█░▄▄ █▄▄█ █▒█▒█ █▀▀▀   █░░▒█ ▒█▒█░ █▀▀▀ █▄▄▀')
            print('█▄▄█ █░▒█ █░░▒█ █▄▄▄   █▄▄▄█ ░▀▄▀░ █▄▄▄ █░▒█')
            game = str(input('Deseja jogar novamente ?').upper())
            
                
            
            
            