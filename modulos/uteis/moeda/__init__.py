#from modulos.uteis import numeros
def doblo(n, f=False, n1='R$'):
    n = n * 2
    if f:
        n = str(f'{n1}{n:4.2f}'.replace('.', ','))
    return n


def metade(n, f=False, n1='R$'):
    n = n / 2
    if f:
        n = str(f'{n1}{n:4.2f}'.replace('.', ','))
    return n

def aumento(n, n1=100, f=False, n2='R$'):
    s = n + (n * n1 / 100)
    if f:
        s = str(f'{n2}{s:4.2f}'.replace('.', ','))
    return s


def redução(n, n1=100, f=False, n2='R$'):
    s = n - (n * n1 / 100)
    if f:
        s = str(f'{n2}{s:4.2f}'.replace('.', ','))
    return s

def moeda(n, n1='R$'):
    n = str(f'{n1}{n:4.2f}'.replace('.', ','))
    return n


def conpor(n):
    n = float(n)
    n = str(f'{n:4.2f}%'.replace('.',','))
    return n


def resumo(n, n1):
    if len(f'O aumento{"":.^35}{aumento(n, n1, True)}') > len(f'O doblo{"":.^37}{doblo(n, True)}'):
        l = len(f'O aumento{"":.^35}{aumento(n, n1, True)}') + 1
    else:
        l = len(f'O doblo{"":.^37}{doblo(n, True)}') + 1
    print('=' * l)
    print(' ' * int((l - 6) / 2), end='')
    print(f'RESUMO')
    print('=' * l)
    print(f'Pocentagem usada{"":.^28}{conpor(n1)}')
    print(f'Preço analisado{"":.^29}{moeda(n)}')
    print(f'O doblo{"":.^37}{doblo(n, True)}')
    print(f'A metade{"":.^36}{metade(n, True)}')
    print(f'O aumento{"":.^35}{aumento(n, n1, True)}')
    print(f'A redução{"":.^35}{redução(n, n1, True)}')
    print('=' * l)
