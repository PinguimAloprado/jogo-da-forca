from time import sleep

def validaçãostr(msg):
    try:
        valida = str(input(f'\033[97m{msg}\033[m')).strip()
        return valida
    except KeyboardInterrupt:
        print('\n')
        return 'Desconhecido'


def linha(tamanho=46):
    print('\033[34m=\033[m' * tamanho)


def cabeçalho(txt, tamanho1=46):
    linha(tamanho1)
    print(f'\033[33m{txt.center(tamanho1)}\033[m')
    linha(tamanho1)


def opções(opções):
    c = 1
    print('\033[97mOPÇÕES:\033[m')
    for itens in opções:
        if type(itens) == str:
            itens = itens.upper()
        print(f'\033[97m[{c}] PARA {itens}\033[m')
        c += 1


def parar(msg, msg2, msg3, tamanho=46):
    while True:
        linha(tamanho)
        stop = validaçãostr(f'\033[97m{msg}\033[m').lower().strip()[0]
        if stop in 's':
            print(f'\033[97m{msg2}\033[m', end='')
            pontinhos()
            break
        elif 'n' in stop:
            linha(tamanho)
            print(f'\033[97m{msg3}\033[m', end='')
            pontinhos()
            break
        else:
            print(f'\033[31mConjunto de caracteris não é valido\033[m')
    return stop


def pontinhos():
    for c in range(3):
        print('.', end='')
        sleep(1)
    print('')


def linhafina(tamanho=46):
    print('\033[34m-\033[m' * tamanho)