from time import *
from os import *
import classes,funcoes,status
#Introdução
def part1():
    status.display()
    part1 = 'Mais um dia se passou no reino de Blue Soul, você está apreciando o crepúsculo após um longo dia de trabalho de campo e seu único sentimento é de que esse não é o seu lugar. \nVocê sonha com aventuras, desafios e conquistas. A vida de um simples plebeu não é mais suficiente. \nA partir de hoje tudo vai mudar, agora você está decidido a realizar as escolhas necessárias para mudar a sua vida e se tornar o maior cavaleiro do reino.'
    for i in part1:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar\n')
def part2():
    status.display()
    part2 = 'A lua cheia nasce no horizonte, iluminando os vastos campos, de repente o galopar de um cavalo ecoa no silêncio. \nDistante, onde começa a floresta sem fim, emerge um cavalo branco, refletindo a luz do luar, manchado com o sangue do seu cavaleiro, que sobre ele varia entre a vida e a morte. \nSem hesitar você corre de encontro e espera poder evitar o destino desse cavaleiro.'
    for i in part2:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar\n')
def part3():
    status.display()
    part3 = 'Enquanto a distância entre vocês diminui, a vida do cavalheiro é perdida a cada galopar. \nO cavalo cansado e machucado para e seu instinto indica que já está fora de perigo, sobre ele está o corpo sem vida do seu companheiro.\n\n\nO que você faz:\n'
    for i in part3:
        sleep(0.01)
        print(i ,end='',flush=True)
def part4_5():
    escolha1 = input('\n[1] Ir embora e fingir que nada aconteceu.\n\n[2] Pegar a espada do cavaleiro.\n\nFaça sua escolha:\n')
    while escolha1 != '1' and escolha1 != '2':
        status.display()
        escolha1 = input('\n[1] Ir embora e fingir que nada aconteceu.\n\n[2] Pegar a espada do cavaleiro.\n\nFaça sua escolha:\n')
    if escolha1 == '1':
        status.display()
        part4 = 'O rugido de um Orc ecoa brutalmente, rasgando o silêncio da noite. \nVocê sente o arrepio e a morte sussurra no seu ouvido, você não deseja ter uma morte longa e dolorosa, como a do cavaleiro a sua frente.'
        for i in part4:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()
        part5 = 'Um Orc corre em sua direção, a sede de sangue nos seus olhos brilha com um vermelho intenso na noite, \nsua velocidade diminui as distâncias entre vocês e você percebe que tem que tomar uma decisão ou a sua morte será inevitável.'
        for i in part5:
            sleep(0.01)
            print(i ,end='',flush=True)
        escolha1a = input('\n\nO que você fará:\n[1] Tentar correr\n\n[2] Pegar a espada\n')
        while escolha1a != '1' and escolha1a != '2':
            escolha1a = input('\n\nO que você fará:\n[1] Tentar correr\n\n[2] Pegar a espada\n')
        
        if escolha1a == '1':
            system('cls')
            morte = 'O Orc é mais rápido do que você e com um brutal ataque rasgou a carne das suas costas, levando você até a morte.\n\n\n\n'
            for i in morte:
                sleep(0.01)
                print(i, end='',flush=True)
            print()
            print('█▀▀█ █▀▀█ █▀▄▀█ █▀▀▀   █▀▀▀█ █░░▒█ █▀▀▀ █▀▀█')
            print('█░▄▄ █▄▄█ █▒█▒█ █▀▀▀   █░░▒█ ▒█▒█░ █▀▀▀ █▄▄▀')
            print('█▄▄█ █░▒█ █░░▒█ █▄▄▄   █▄▄▄█ ░▀▄▀░ █▄▄▄ █░▒█')
            print()
            return 'Game Over'
        elif escolha1a == '2':
            status.display()
            print('Você pegou a espada e se colocou em posição de batalha.')
            sleep(0.8)

    elif escolha1 == '2':
        status.display()
        part4 = 'O rugido de um Orc ecoa brutalmente, rasgando o silêncio da noite. \nVocê sente o arrepio e a morte sussurra no seu ouvido. \nVocê não deseja ter uma morte longa e dolorosa, como a do cavaleiro a sua frente.'
        for i in part4:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()
        part5 = 'Um Orc corre em sua direção, a sede de sangue nos seus olhos brilha com um vermelho intenso na noite, sua velocidade diminui as distâncias entre vocês. \nVocê está com a espada e em posição de batalha.'
        for i in part5:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')    
        sleep(0.8)


# De qualquer forma LUTA

def part6_7_8():
    status.display()
    part6 = 'Apenas o som das batidas rápidas e fortes do seu coração podem ser escutadas, parece que ele bate fora de você. \nVocê nunca tinha sentido tanta adrenalina correndo pelo seu corpo, suas mãos tremem entre medo e êxtases por ter sobrevivido.'
    for i in part6:
        sleep(0.02)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar\n')
    status.display()
    part7 = 'Com a chegada do orc o cavalo correu em direção a floresta. \nVocê caminha pelo campo, apenas pensando em como poderia ter perdido a sua vida caso a luta tivesse sido diferente.'
    for i in part7:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar\n')
    status.display()
    part8 = 'O seu corpo está cansado e machucado, quando a adrenalina diminui você começa a se sentir cansado e a sua vista escurece, \nvocê tenta \nmas um sono muito pesado está tomando conta de você…'
    for i in part8:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar\n')
    status.display()

# Começa dia 2
# Duas opções ir para casa ou para a cidade

def part9():
    part9 = '...O sol do amanhecer começa a esquentar o seu corpo e a luz invade os seus olhos, você acorda pensando ter sonhado com toda a ação, mas ela foi real. \n\nVocê agora tem duas opções:'
    for i in part9:
        sleep(0.01)
        print(i ,end='',flush=True)
    escolha2 = input('\n\nO que você fará:\n\n[1] Ir para sua casa.\n\n[2] Ir para a cidade conseguir alguma informação sobre o que aconteceu.\n')
    status.display()
    while escolha2 != '1' and escolha2 != '2':
        escolha2 = input('\n\nO que você fará:\n\n[1] Ir para sua casa.\n\n[2] Ir para a cidade conseguir alguma informação sobre o que aconteceu.\n')
        status.display()

    
    if escolha2 == '1':
        part9a1 = 'Você está em sua casa e seu pai já o chama para trabalhar na terra, você conta a ele o que aconteceu e ele responde: \n\n“Eu já falei para você não ir para longe de casa, essas terras são perigosas. \nAgora, vamos trabalhar!”'
        for i in part9a1:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()
        part9a2 = 'Após horas de trabalho, sua mente não te deixa em paz, você quer descobrir quem era o dono daquela espada. \nDe repente você escuta batidas em sua porta e ao abrí-la se depara com 2 cavaleiros, com armaduras parecidas com o cavaleiro que encontrou morto na noite anterior.'
        for i in part9a2:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()
        part9a3 = 'Um deles se aproxima e diz: \n"Vocês escutaram algo ontem a noite? \nAlgum barulho fora do normal ou viram alguém?" \n\nCom prontidão você responde: \n"Sim, sim senhor, ontem estava no campo quando vi um cavaleiro se aproximando, mas ele estava morto. \nDe repente apareceu um Orc, peguei a espada do cavaleiro e em uma difícil luta matei o Orc". \n\nApós uma parada para respirar, continua: \n‘Acabei dormindo no campo e voltei para casa hoje pela manhã.'
        for i in part9a3:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()
        part9a4 = 'O cavaleiro responde admirado: \n"Você conseguiu matar o Orc sozinho?"\n\nSim senhor, fiquei até sem reação quando a luta terminou.'
        for i in part9a4:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()

        part9a5 = 'O cavaleiro aproxima de seu companheiro e conversam entre si. \nQuando volta até você, ele lhe diz: \n\n"Você mostrou muita coragem ao matar aquele Orc, e sem nenhum treino. \nImagine se você fosse um guerreiro, você gostaria de treinar para ser um cavaleiro?".'
        for i in part9a5:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()

        part9a6 = 'É claro que sim, e tudo o que eu quero.\n\nCavaleiro: "Então vá até o castelo e se apresente amanhã!."'
        for i in part9a6:
            sleep(0.0)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()

    elif escolha2 == '2':
        escolha3 = input('\nVocê chegou até a cidade:\n\n[1] Ir para a Taberna.\n\n[2] Ir para o Castelo.\n')
        while escolha3 != '1' and escolha3 != '2':
            status.display()
            escolha3 = input('\nVocê chegou até a cidade:\n\n[1] Ir para a Taberna.\n\n[2] Ir para o Castelo.\n')
        status.display()
        if escolha3 == '1':
            escolha4 = input('\nVocê chegou na Taberna, local de confraternização e bebedeiras. \nVocê logo avista Lui, o mestre cervejeiro:\n\n[1] Pedir uma cerveja.\n\n[2] Pedir informação. \n')
            status.display()
            while escolha4 != '1' and escolha4 != '2':
                escolha4 = input('\nVocê chegou na Taberna, local de confraternização e bebedeiras. \nVocê logo avista Lui, o mestre cervejeiro:\n\n[1] Pedir uma cerveja.\n\n[2] Pedir informação. \n')
                status.display()
            while escolha4 == '1':
                print('Que delícia! Você tomou uma cerveja.')
                escolha4 = input('\n[1] Pedir outra cerveja.\n\n[2] Pedir informação. \n')
                status.display()
                while escolha4 !='1' and escolha4 != '2':
                    escolha4 = input('\n[1] Pedir outra cerveja.\n\n[2] Pedir informação. \n')
                status.display()
            if escolha4 == '2':
                part9b1c = 'Lui diz que ouviu boatos que um cavaleiro foi atrás do Orc Rei há uns dias \ne que até agora não tinha retornado, os outros cavaleiros já estão desesperançosos quanto ao seu retorno.'
                for i in part9b1c:
                    sleep(0.01)
                    print(i ,end='',flush=True)
                input('\n\nAperte ENTER para continuar\n')
                status.display()
            part9b1d = 'Ao sair da Taberna, você se depara com dois cavaleiros, eles reconhecem a espada que você carrega e lhe empurram contra a parede: \n"Onde você conseguiu essa espada?" \n"Ela é de um cavaleiro que foi em uma missão e ainda não retornou." \nApós explicar toda a história para o cavaleiro ele afasta e conversa com seu companheiro.'
            for i in part9b1d:
                sleep(0.01)
                print(i ,end='',flush=True)
            input('\n\nAperte ENTER para continuar\n')
            status.display()
            part9b1e = 'Quando volta até você, ele lhe diz: \n"Você mostrou muita coragem ao matar aquele Orc." \n"E sem nenhum treino, imagine se você fosse um guerreiro." \n"Você gostaria de treinar para ser um cavaleiro.?"'
            for i in part9b1e:
                sleep(0.01)
                print(i ,end='',flush=True)
            input('\n\nAperte ENTER para continuar\n')
            status.display()          
            part9b1f = 'É claro que sim, e tudo o que eu quero.\n\nCavaleiro: "Então vá até o castelo e se apresente amanhã!."'
            for i in part9b1f:
                sleep(0.01)
                print(i ,end='',flush=True)
            input('\n\nAperte ENTER para continuar\n')
            status.display()
        elif escolha3 == '2':
            part9b2a = 'Você está no castelo e vai conversar com o primeiro cavaleiro que você vê, mas de repente um guarda passa esbarrando e corre em direção ao cavaleiro. \nVocê escuta a conversa de longe...  \n"acharam o corpo de um cavaleiro, próximo a floresta sem fim." \nVocê sabia que estavam falando do mesmo cavaleiro que encontrou ontem. \nQuando pensa em intervir na conversa, um cavaleiro lhe empurra por trás e questiona \n"Foi você que matou Alexander?" \n"Essa era a espada dele!"'
            for i in part9b2a:
                sleep(0.01)
                print(i ,end='',flush=True)
            input('\n\nAperte ENTER para continuar\n')
            status.display()
            part9b2b = 'Após explicar toda a história para o cavaleiro ele afasta e conversa com seu companheiro. \nQuando volta até você, ele lhe diz: \n"Você mostrou muita coragem ao matar aquele Orc." \n"E sem nenhum treino, imagine se você fosse um guerreiro, você gostaria de treinar para ser um cavaleiro.?"'
            for i in part9b2b:
                sleep(0.01)
                print(i ,end='',flush=True)
            input('\n\nAperte ENTER para continuar\n')
            status.display()
            part9b2c = 'É claro que sim, e tudo o que eu quero.\n\nCavaleiro: "Então vá até o castelo e se apresente amanhã!."'   
            for i in part9b2c:
                sleep(0.01)
                print(i ,end='',flush=True)
            input('\n\nAperte ENTER para continuar\n')
            status.display()

def part10():
    part10 = 'Você acorda em sua casa de prontidão. \nSeu pai não está nada satisfeito com você ter aceitado o convite sem ao menos conversar com ele.\n\n"Filho", ele diz "isso é muito perigoso, porque você nao continua trabalhando comigo no campo?"'
    for i in part10:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar\n')
    status.display()
    part10a = '"Não é isso que eu quero pai!" \n"Eu quero conhecer lugares diferentes, batalhar, sentir novamente a adrenalina correndo em minhas veias." \n"Desculpe, mas o meu destino não é continuar aqui."\n\nPai: "Por favor, pense no que falei"'
    for i in part10a:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar\n')
    status.display()
    escolha4 = input('\nO que você deseja fazer:\n\n[1] Ir para o Castelo.\n\n[2] Ficar em casa e trabalhar com o seu pai. \n')
    while escolha4 != '1' and escolha4 !='2':
        status.display()
        escolha4 = input('\nO que você deseja fazer:\n\n[1] Ir para o Castelo.\n\n[2] Ficar em casa e trabalhar com o seu pai. \n')
    status.display()
    if escolha4 == '1':
        part10x = 'No castelo você logo se depara com o Rei com os dois cavaleiros de ontem ao seu lado. \nE ele lhe fala: \n"Jovem, ouvi sobre a sua luta com o Orc e primeiramente gostaria de lhe conceder toda a minha gratidão por ter matado uma criatura que nos traz tanto mal." \n"Meus cavaleiros o chamaram até aqui para que eu dê a minha permissão para que você comece a treinar."'
        for i in part10x:
            sleep(0.01)
            print(i ,end='',flush=True)    
        escolha5 = input('É realmente isso que você quer?\n\n[1] Sim\n\n[2] Não\n')
        while escolha5 != '1' and escolha5 != '2':
            status.display()
            escolha5 = input('É realmente isso que você quer?\n\n[1] Sim\n\n[2] Não\n')
        status.display()   
        if escolha5 == '1':
            part10b = '"Era isso que eu queria escutar." \n"Eu lhe dou a permissão para utilizar a espada de ‘Alexander’, mas ela só será sua realmente quando você se tornar um cavaleiro." \n"Amanhã você começa a treinar."'
            for i in part10b:
                sleep(0.01)
                print(i ,end='',flush=True)
            input('\n\nAperte ENTER para continuar\n')
            status.display()
            classes.heroi.prox_dia()            
        elif escolha5 == '2':
            part10c = '"Infelizmente você precisa devolver sua espada e espero que um dia você encontre o seu verdadeiro caminho." \n"Adeus."'
            for i in part10c:
                sleep(0.01)
                print(i ,end='',flush=True)
            input('\n\nAperte ENTER para continuar\n')
            status.display()
            part10y = '"Que bom que você voltou meu filho. \nVamos, vem trabalhar comigo.\n\nSão essas próximas ações que você fará toda a sua vida."'
            for i in part10y:
                sleep(0.01)
                print(i ,end='',flush=True)
            input('\n\nAperte ENTER para continuar\n')
            status.display()
            
            while escolha5 == '2':
                escolha6 = input('Você trabalhou por algumas horas. \nAgora você pode: \n\n[1] Ir para a Taberna\n\n[2]Descansar')
                while escolha6 != '1' and escolha6 != '2':
                    status.display()
                    escolha6 = input('Você trabalhou por algumas horas. \nAgora você pode: \n\n[1] Ir para a Taberna\n\n[2]Descansar')
                status.display()
                if escolha6 == '1':
                    escolha7 = input('\nVocê chegou na Taberna, local de confraternização e bebedeiras. \nVocê logo avista Lui, o mestre cervejeiro:\n\n[1] Tomar cerveja.\n\n[2] Jogar conversa fora com Lui. \n')
                    while escolha7 != '1' and escolha7 != '2':
                        status.display()
                        escolha7 = input('\nVocê chegou na Taberna, local de confraternização e bebedeiras. \nVocê logo avista Lui, o mestre cervejeiro:\n\n[1] Tomar cerveja.\n\n[2] Jogar conversa fora com Lui. \n')
                    status.display()
                    if escolha7 == '1':
                        part10e = 'Você está bêbado e precisa voltar para casa.'
                        for i in part10e:
                            sleep(0.01)
                            print(i ,end='',flush=True)
                        input('\n\nAperte ENTER para continuar\n')
                        status.display()
                    if escolha7 == '2':
                        part10f = 'Um tempo se passou e você precisa voltar para casa.'
                        for i in part10f:
                            sleep(0.01)
                            print(i ,end='',flush=True)
                        input('\n\nAperte ENTER para continuar\n')
                        status.display()
                elif escolha6 == '2':
                    pass
                classes.heroi.prox_dia()            
    
    elif escolha4 == '2':
        part10d = 'Isso que eu queria ouvir filho, vamos trabalhar.\n\nSão essas próximas ações que você fará toda a sua vida.'
        for i in part10d:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()
        
        while escolha4 == '2':
            escolha6 = input('Você trabalhou por algumas horas. \nAgora você pode: \n\n[1] Ir para a Taberna\n\n[2]Descansar')
            while escolha6 != '1' and escolha6 != '2':
                status.display()
                escolha6 = input('Você trabalhou por algumas horas. \nAgora você pode: \n\n[1] Ir para a Taberna\n\n[2]Descansar')
            status.display()
            if escolha6 == '1':
                escolha7 = input('\nVocê chegou na Taberna, local de confraternização e bebedeiras. \nVocê logo avista Lui, o mestre cervejeiro:\n\n[1] Tomar cerveja.\n\n[2] Jogar conversa fora com Lui. \n')
                while escolha7 != '1' and escolha7 !='2':
                    status.display()
                    escolha7 = input('\nVocê chegou na Taberna, local de confraternização e bebedeiras. \nVocê logo avista Lui, o mestre cervejeiro:\n\n[1] Tomar cerveja.\n\n[2] Jogar conversa fora com Lui. \n')
                status.display()
                if escolha7 == '1':
                    part10e = 'Você está bêbado e precisa voltar para casa.'
                    for i in part10e:
                        sleep(0.01)
                        print(i ,end='',flush=True)
                    input('\n\nAperte ENTER para continuar\n')
                    status.display()
                if escolha7 == '2':
                    part10f = 'Um tempo se passou e você precisa voltar para casa.'
                    for i in part10f:
                        sleep(0.01)
                        print(i ,end='',flush=True)
                    input('\n\nAperte ENTER para continuar\n')
                    status.display()
            elif escolha6 == '2':
                pass
            classes.heroi.prox_dia()

def part11_12():
    while classes.heroi.level < 4:
        part11 = 'Você acorda animado e pronto para o seu dia! \nLogo cedo você já tem uma decisão para tomar.'
        for i in part11:
            sleep(0.01)
            print(i ,end='',flush=True)
        input('\n\nAperte ENTER para continuar\n')
        status.display()
        escolha11a = input('\nVocê deseja:\n\n[1] Treinar.\n\n[2] Ir para a floresta matar algum orc. \n')
        while escolha11a != '1' and escolha11a != '2':
            status.display()
            escolha11a = input('\nVocê deseja:\n\n[1] Treinar.\n\n[2] Ir para a floresta matar algum orc. \n')
        status.display()
        if escolha11a == '1':
            funcoes.treinar()
            print('A parte da manhã se passou')
        elif escolha11a == '2':
            funcoes.batalhar1()
            print('A parte da manhã se passou')
        
        escolha11b = input('\n\nNa parte da tarde você deseja:\n\n[1] Treinar.\n\n[2] Ir para a floresta matar algum orc.\n\n[3] Descansar\n')
        while escolha11b != '1' and escolha11b != '2':
            status.display()
            escolha11b = input('\n\nVocê deseja:\n\n[1] Treinar.\n\n[2] Ir para a floresta matar algum orc.\n\n[3] Descansar\n')
        status.display()
        if escolha11b == '1':
            funcoes.treinar()
            print('A parte da tarde se passou')
            classes.heroi.prox_dia()
        elif escolha11b == '2':
            funcoes.batalhar1()
            print('A parte da tarde se passou')
            classes.heroi.prox_dia()            
        elif escolha11b == '3':
            classes.heroi.prox_dia()
    
    part12 = 'Parabens!!! \nVocê chegou ao level 4 e seus compnaheiros de batalha o chamaram para o Castelo.'
    for i in part12:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar\n')
    status.display()
    part12b = 'Chegando ao castelo você se depara com o Rei, que lhe explica o chamado:\n\n"Já é de seu conhecimento que Alexander foi atrás do Orc Rei, porém nossas fontes indicam de que na verdade foi o Orc Campeão, braço direito do Orc Rei, que o atacou. \nAvistamos ele próximo a entrada da floresta sem fim, acredito que agora você poderá tentar matá-lo, mas tenha cuidado para não acabar como Alexander!"\n\nDeixe comigo, vossa Majestade, não o decepcionarei.'
    for i in part12b:
        sleep(0.01)
        print(i ,end='',flush=True)
    input('\n\nAperte ENTER para continuar\n')
    status.display()

          
    while True:
        escolha12a = input('\nVocê deseja:\n\n[1] Treinar mais.\n\n[2] Ir para a floresta duelar com o campeão Orc. \n')
        while escolha12a !='1' and escolha12a !='2':
            status.display()
            escolha12a = input('\nVocê deseja:\n\n[1] Treinar mais.\n\n[2] Ir para a floresta duelar com o campeão Orc. \n')
        status.display()
        if escolha12a == '1':  
            funcoes.treinar()
            print('A parte da manhã se passou')
            escolha12b = input('\nNa parte da tarde você deseja:\n\n[1] Treinar mais.\n\n[2] Ir para a floresta duelar com o campeão Orc.\n')
            while escolha12b != '1' and escolha12b !='2':
                status.display()
                escolha12b = input('\nNa parte da tarde você deseja:\n\n[1] Treinar mais.\n\n[2] Ir para a floresta duelar com o campeão Orc.\n')
            status.display()
            if escolha12b == '1':
                funcoes.treinar()
                print('A parte da tarde se passou')
            elif escolha12b == '2':
                break
        elif escolha12a == '2':
            break
        classes.heroi.prox_dia()     
        
    funcoes.batalharcampeao()