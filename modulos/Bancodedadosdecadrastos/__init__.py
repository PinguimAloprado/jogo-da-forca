from time import sleep
from modulos.uteis.strings import validaçãostr, linha
from modulos.uteis.numeros import validaçãoint

n = [{'nome': 'synthia', 'idade': 20},
     {'nome': 'carlos', 'idade': 40},
     {'nome': 'massia', 'idade': 16}
]
def retorna():
    return n


def save(dadostemp):
    global n
    n.append(dadostemp.copy())
    return 'cadrastada com sucesso'

def mostracadrastros():
    dados = retorna()
    print('carregando', end='')
    for c in range(3):
        print('.', end='')
        sleep(0.75)
    print('')
    for d, c in enumerate(dados):
        r = 0
        print(f'{d + 1}--> ', end='')
        for chave, valor in c.items():
            r += 1
            if r == 1:
                print(f'{chave} {valor:.<21}', end='')
            else:
                print(f'{chave} {valor:2} anos ', end='')
        print('')
    sleep(2)


def adcionardados():
    while True:
        dadostemp = {}
        dadostemp['nome'] = validaçãostr('Informe o seu nome: ')
        dadostemp['idade'] = validaçãoint('Informe a sua idade: ')
        print('cadrastrando', end='')
        for c in range(3):
            print('.', end='')
            sleep(0.75)
        print('')
        print(save(dadostemp))
        while True:
            linha()
            stop = validaçãostr('deseja cadrasta mais alguem [S/N]: ').lower()[0]
            linha()
            if stop in 's':
                print('se preparando para cadrastra.')
                sleep(0.5)
                break
            elif 'n' in stop:
                print('voltando para o menu.')
                sleep(1)
                break
            else:
                print(f'\033[31mConjunto de caracteris não é valido\033[m')
        if stop == 'n':
            break