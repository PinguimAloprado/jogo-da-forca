from random import choice
from modulos.uteis.strings import linha, pontinhos, linhafina
from modulos.uteis.numeros import validaçãoint
from time import sleep

temasbase = ['comida', 'bebida', 'animal', 'objetos']

def palavra(local):
    try:
        a = open(local, 'rt')
    except Exception as erro:
        print(f'O erro encontrado foi {erro.__class__}, causado por {erro.__cause__}1')
    else:
        sorteio = []
        for itens in a:
            itens1 = itens.replace('\n', '')
            sorteio.append(itens1)
        ganhandor = choice(sorteio)
        a.close()
        return ganhandor


def teladojogo(local, palavra, vida=6, chutes='', divisolia=70):
    try:
        linha(divisolia)
        print(f'\033[97mTEMA: {local.upper():<31}VIDA[{vida}]:\033[m ', f'\033[31mS2 \033[m' * vida, '\n\n')
        print(f'\033[97mPALAVRA[{len(palavra):>2}]: {palavra.upper():<23} CHUTES: \033[97m{chutes.upper()}\033[m')
        linha(divisolia)
    except:
        print('algo de errado não está certo')


def escondepalavra(palavra, chutes=''):
    escondida =''
    for letra in palavra:
        if letra in chutes:
            escondida += letra
        else:
            escondida += '*'
    return escondida


def checar(letra, chutes):
    if letra not in chutes:
        chutes += ' ' + letra
    return chutes


def printa(objtos, tamanho=46):
    a = 1
    linha(tamanho)
    print('\033[97mTEMAS ATUAIS: \033[m')
    for c in objtos:
        print(f'\033[97m{a}-{c}\033[m')
        a +=1


def olharoquefalta(temas, tamanho=46):
    if len(temas) != len(temasbase):
        n = []
        n1 = 1
        for c in temasbase:
            if c not in temas:
                print(f'\033[97m{n1}-{c}\033[97m')
                n.append(n1)
            n1 += 1
        while True:
            escolhar = validaçãoint('INFORME A SUA ESCOLHAR: ')
            if escolhar in n:
                 n2 = temasbase[escolhar - 1]
                 return n2
            else:
                linhafina(tamanho)
                print('\033[31mESCOLHAR INVALIDA TENTE NOVAMENTE\033[m')
    else:
        print('\033[31mNÃO A TEMAS DISPONIVEIS A SEREM ADICIONADOS!!!\n\033[97mVOLTANDO A CONFIGURAÇÕES\033[m', end='')
        pontinhos()
        return ''

