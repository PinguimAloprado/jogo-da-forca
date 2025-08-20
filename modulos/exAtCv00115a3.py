from uteis.numeros import validaçãoint
from uteis.strings import opções, linha, cabeçalho, validaçãostr
from uteis.arquivos import arquivoexister, criaarquivo, lerarquivo,cadrasta
from time import sleep

local = 'banco2.txt'
existe = arquivoexister(local)
if not existe:
    criaarquivo('banco2.txt')
while True:
    cabeçalho('MENU')
    opções(['VER PESSOAS CADRASTADAS', 'UM NOVO CADRASTO', 'SAIR'])
    linha()
    escolhar = validaçãoint('SUA ESCOLHAR: ')
    if escolhar == 1:
        print('CARREGANDO', end='')
        for ponto in range(3):
            print('.', end='')
            sleep(1)
        print('')
        lerarquivo(local)
        sleep(3)
    elif escolhar == 2:
        while True:
            linha()
            nome = validaçãostr('Informe o seu nome: ')
            idade = validaçãoint('Informe a sua idade: ')
            linha()
            cadrasta(local, nome, idade)
            linha()
            while True:
                stop = validaçãostr('deseja cadrasta mais alguem [S/N]: ').lower()[0]
                if stop in 's':
                    print('se preparando para cadrastra.')
                    sleep(0.5)
                    break
                elif 'n' in stop:
                    print('voltando para o menu.')
                    sleep(0.5)
                    break
                else:
                    print(f'\033[31mConjunto de caracteris não é valido\033[m')
            if stop == 'n':
                break
    elif escolhar == 3:
        break
    else:
        print(f'{escolhar} não é uma opção validar')
print(f'{" FIM ":=^46}')