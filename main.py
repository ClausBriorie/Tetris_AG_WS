##################################################################
##                                                              ##
##      CODIGO CRIADO PELO GRUPO TURING - POLI USP 2017         ##
##      https://www.facebook.com/grupoturing.poliusp            ##
##      Todos podem usar este código livremente                 ##
##                                                              ##
##################################################################

import jogo
import algoritmoGenetico as ag

#O main é interessante deixar que escrevam pois dá uma ideia geral do que está acontecendo
# e tudo que é necessário para o jogo acontecer e evoluir

##    Nessa funcao voce deve procurar um individuo capaz de vencer o jogo,
##    Para isso você precisa:
##
##    1) Declarar a Geracao Zero, com 10 individuos
##
##    2) Avaliar os individuos de cada geracao (jogando o jogo)
##
##    3) Selecionar os 4 melhores e utilizar eles para reproduzir a proxima Geracao
##
##    4) Voltar para "2" até a condição de parada seja atingida (ex: conseguir passar de nível, fazer uma pontuação maior que 5000 pontos)
##
##    5) Retornar um objeto Geracao com os individuos treinados (pode ser apenas 1 individuo)
##
##
##    Dicas: você ja criou diversas funcoes no outro arquivo e deve chamá-las quando achar necessário.
##        As que você vai precisar usar são:        
##            -ag.Geracoes()
##            -individuo.fitness(gameState)
##            -geracao.selecao(numSelec)
##            -geracao.reproduzir(m, chanceCO, chanceMut)
##        Alem disso, você deve usar a funcão ja pronta:
##            -gameState = jogo.jogar(individuo,numBat,multVelocidade)
##                -essa função utiliza o individuo para um novo jogo de Tetris, e retorna variáveis do jogo (gameState)
##                    além disso, deve-se escolher a pontuação máxima para "ganhar" e finalizar o jogo
##                    e também definir o quão rápido deve estar o jogo (recomendo usar multVelocidade = 50)
##
##                -lembrando que gameState possui:    
##                   ???

    
    #COMPLETE AQUI

def main():

    numInd = 10
    geracao = ag.Geracao(numInd)
    #vel_jogo = int(input('Velocidade de jogo desejada: '))*100
    vel_jogo = 500
    for j in range(numInd):
        print (' \n')
        print (' - - - - Geração atual: {} - - - - ' .format(j+1))
        print (' \n')
        #print("   Score: ",geracao.individuos[i].fitness(gameState),"\n")
        for i in range(10):
            gameState = jogo.jogar(geracao.individuos[i], vel_jogo, scoreMax = 200000, jogoRapido = False)
            geracao.individuos[i].fitness(gameState)
            geracao.selecao(1)
            print("melhor individuo da geração!!!")
        geracao.selecao(3)
        geracao.reproduzir(10)

    geracao.selecao(1)
    print("melhor individuo!!!")
    gameState = jogo.jogar(geracao.individuos[0], vel_jogo, 1)    

    return(geracao)


#-----------------------------------------------

gen = main()

#essa parte do código serve para exportar os individuos em formato de texto
#dessa forma é possível guardar os valores e usar depois se necessário
#nao precisa mexer
for i in range(len(gen.individuos)):
    arq = open('inds/ind{}.txt'.format(i), 'w')
    arq.write(' '.join(map(str, gen.individuos[i].pesos)))
    arq.close()

