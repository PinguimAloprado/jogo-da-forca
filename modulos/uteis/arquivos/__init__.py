from modulos.uteis.strings import cabeçalho

def arquivoexister(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaarquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um Erro')
    else:
        print(f'{nome} criador com sucesso')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except Exception as erro:
        print(f'O erro encontrado foi {erro.__class__}, causado por {erro.__cause__}')
    else:
        cabeçalho('PESSOAS CADRASTRADAS')
        c = 0
        for linha in a:
            c += 1
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{c:>2}-->Nome {dado[0]:.<21}{dado[1]} Anos')
    finally:
        a.close()


def cadrasta(local, nome='DESCONHECIDO', idade=0):
    try:
        a = open(local, 'at')
    except:
        print('Houver um erro na hora de abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houver um erro na hora de escreve os dados')
        else:
            print(f'O cadrasto de {nome} foi efetuado com sucesso')
            a.close()
