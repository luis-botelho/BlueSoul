import os
import pygame

if __name__ == "__main__":
    pygame.init()
    if os.path.exists('./Audios/MusicaInicial.mp3'):
        pygame.mixer.music.load('./Audios/MusicaInicial.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.03)

        clock = pygame.time.Clock()
        clock.tick(10)

        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            clock.tick(10)

            separador = '=-' * 80
            welcome = 'Bem vindo(a) ao mundo de Blue Soul'
            print("{0:^100}".format(separador))
            print("{0:^170}".format(welcome))
            print("{0:^100}".format(separador))
            input('\n\n\n\nAperte ENTER para continuar\n')
            
            import classes,funcoes,historia

            classes.heroi
            historia.part1()
            historia.part2()
            historia.part3()
            if historia.part4_5() == 'Game Over':
                break
            funcoes.pegar_espada()
            funcoes.batalhar1()
            historia.part6_7_8()
            classes.heroi.prox_dia()
            historia.part9()
            classes.heroi.prox_dia()
            historia.part10()
            historia.part11_12()
            funcoes.matou_orc_campeao()
            break
        print('\n\nEsperamos que tenha se divertido.\n\nMax LyFe\n\nLuis Botelho\n\nCaio Giovani')

    else:
        print('O arquivo musica.mp3 não está no diretório do script Python')
    
    