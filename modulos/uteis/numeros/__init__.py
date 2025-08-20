def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def validação(msg):
    while True:
        try:
            n = input(f'{msg}').strip().replace(',', '.')
            if '.' in n and n.count('.') == 1:
                n1 = n.replace('.', '')
                if n1.isnumeric():
                    n = float(n)
                    return n
            if n.isnumeric():
                n = int(n)
                return n
            print(f'\033[31mO Conjunto de Caracteris não Formar um Numero Valido\033[m')
        except KeyboardInterrupt:
            print(f'\nO usuario preferio não informa um numero, retornando 0')
            n = 0
            return n



def validaçãoint(msg):
    while True:
        try:
            n = input(f'\033[97m{msg}\033[m').strip()
            if n.isnumeric():
                n = int(n)
                return n
            print(f'\033[31mO Conjunto de Caracteris não Formar um Numero inteiro Valido\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuario preferio não informa um numero, retornando 0\033[m')
            n = 0
            return n

"""a = validação('Digite um numero: ')
print(a)"""
