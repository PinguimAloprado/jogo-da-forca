from uteis.numeros import validaçãoint
from Bancodedadosdecadrastos import retorna, save
from time import sleep
from uteis.strings import validaçãostr

while True:     #MENU
    print('=' * 46)
    print(f'{"MENU":^46}')
    print('=' * 46)
    print('OPÇÕES, DIGITE:\n[1] PARA VER PESSOAS CADRASTADAS\n[2] PARA UM NOVO CADRASTO\n[0] PARA SAIR')
    print('=' * 46)
    while True:
        n = validaçãoint('Informe a sua escolhar: ')
        if -1 < n < 3:
            break
        else:
            print(f'{n} não é uma opção validar')
            print('=' * 46)


    if n == 1:      #MOSTRA CADRASTROS
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


    if n == 2:     #CADRASTAS PESSOAS
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
                print('=' * 46)
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


    if n == 0:   #SAIR
        break



