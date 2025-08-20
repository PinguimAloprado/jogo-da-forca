from random import choice
from modulos.uteis.strings import cabeçalho, opções, linha, validaçãostr, parar, pontinhos
from modulos.uteis.numeros import validaçãoint
from jogodaforcaferramentas import palavra, teladojogo, escondepalavra, checar,printa, olharoquefalta
from time import sleep


temas = ['comida', 'bebida', 'animal', 'objetos']
sair = 1
vida = 6
temasbase = ['comida', 'bebida', 'animal', 'objetos']
while True:   #COMEÇO/MENU
    cabeçalho('MENU', 70)
    opções(['JOGAR', 'CONFIGURAÇÕES', 'SAIR'])
    escolhar = validaçãoint('\033[97mESCOLHAR:\033[m ')

    if escolhar == 1:      # o JOGO EM SI
        while True:
            vida = vida
            chutes = ''
            local = choice(temas)
            PalavraSorteada = palavra(local)
            while True:
                PalavraEscondida = escondepalavra(PalavraSorteada, chutes)
                teladojogo(local, PalavraEscondida, vida, chutes)
                player = validaçãostr('\033[97mESCOLHAR UMA LETRA:\033[m ').strip().lower()[0]
                chutes = checar(player, chutes)
                if player not in PalavraSorteada:
                    vida -= 1
                    if vida == 0:
                        print(f'\033[31mVocê perdeu mais sorte na proxima. a palavra era {PalavraSorteada}\033[m')
                        break
                if PalavraSorteada == escondepalavra(PalavraSorteada, chutes):
                    linha(70)
                    print(f'\033[32mPARABENS VOÇÊ GANHOU!!!\033[m')
                    break
                if player == '0':
                    sair = 0
                    break
            if sair == 0:
                sair = 1
                break
            stop = parar('DESEJA JOGAR NOVAMENTE: ', 'CARREGANDO', 'VOLTANDO PARA O MENU', 70)
            if stop == 'n':
                break

    elif escolhar == 2:         #CONFIGURAÇÕES MANIPULAVEIS, TODOS VÃO TER UM 2 NO COMEÇO
        while True:
            cabeçalho('CONFIGURAÇÕES', 70)
            opções(['MUDA A QUANTIDADE DE VIDAS', 'TIRA TEMA', 'ADICIONAR TEMA', 'VOLTAR AO MENU'])
            linha(70)
            escolhar = validaçãoint('SUA ESCOLHAR: ')
            if escolhar == 1:      #  2 QUANTIDADE DE VIDA/CHANCES
                print(f'\033[97m{vida} atuaL\033[m')
                vida = validaçãoint('\033[97mDESEJA COLOCAR QUAL QUANTIDADES DE VIDAS/TENTATIVAS: \033[m')
                print(f'\033[97mVIDA ATUAL {vida}\033[m')
                sleep(2)

            elif escolhar == 2:  # 2 REMOVER TEMA
                while True:
                    if len(temas) > 1:
                        printa(temas, 70)
                        escolhar = validaçãoint('\033[97mqual deseja remove: \033[m')
                        if len(temas) + 1 > escolhar > -1:
                            temas.remove(temas[escolhar - 1])
                        else:
                            print('ESCOLHAR INVALIDAR')
                        printa(temas, 70)
                        stop = parar('DESEJA REMOVER MAIS ALGUM TEMA: ', 'CARREGANDO', 'VOLTANDO PARA CONFIGURANÇÕES', 70)
                        if 'n' in stop:
                            break
                    else:
                        print('\033[31mO JOGO TEM QUE TER AUMENOS 1 TEMA, SOLICITAÇÃO NEGADA!!!\n\033[97mVOLTANDO A CONFIGURAÇÃO\033[m\nCARREGANDO', end='')
                        pontinhos()
                        break

            elif escolhar == 3:   # 2 ADICIONAR TEMA REMOVIDO
                while True:
                    linha(70)
                    n1 = olharoquefalta(temas, 70)
                    if not n1 == '':
                        temas.append(n1)
                    else:
                        break
                    stop = parar('DESEJA ADICIONAR MAIS ALGUM TEMA: ', 'CARREGANDO', 'VOLTANDO PARA CONFIGURAÇÕES', 70)
                    if stop in 'n':
                        break

            elif escolhar == 4:   # 2 VOLTAR AO MENU PRINCIPAL
                break

    elif escolhar == 3: # SAIR/TEMINAR SESSÃO
        print(f'\033[34m{" VOLTE SEMPRE ":=^70}\033[1m')
        break

    else:
        print(f'\033[31mESCOLHAR INVALIDAR\033[m')
