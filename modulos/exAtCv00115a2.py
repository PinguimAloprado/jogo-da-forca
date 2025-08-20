from uteis.numeros import validaçãoint
from Bancodedadosdecadrastos import mostracadrastros, adcionardados
from uteis.strings import opções, linha, cabeçalho
from uteis.arquivos import arquivoexister, criaarquivo

existe = arquivoexister('banco2.txt')
if not existe:
    criaarquivo('banco2.txt')
while True:
    cabeçalho('MENU')
    opções(['VER PESSOAS CADRASTADAS', 'UM NOVO CADRASTO', 'SAIR'])
    linha()
    escolhar = validaçãoint('SUA ESCOLHAR: ')
    if escolhar == 1:
        linha()
        mostracadrastros()
    elif escolhar == 2:
        linha()
        adcionardados()
    elif escolhar == 3:
        break
    else:
        print(f'{escolhar} não é uma opção validar')
print(f'{" FIM ":=^46}')