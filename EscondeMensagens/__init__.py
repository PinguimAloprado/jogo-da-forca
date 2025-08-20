from random import choice

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', ' ', ',', '!', '?']

codigo = [5, 7, 3, 13]

def escondemensagem(msg):
    total = ''
    rotação = 0
    contador = 0
    for c in msg:
        while True:
            if codigo[contador]-1 == rotação:
                total += c
                rotação = 0
                if codigo[contador] == codigo[len(codigo) - 1]:
                    contador = 0
                else:
                    contador += 1
                break
            else:
                total += choice(letras)
                rotação += 1
    return total


def formarpalavra(msg):
    total = ''
    rotação = 0
    contador = 0
    for c in msg:
        if codigo[contador]-1 == rotação:
            total += c
            rotação = 0
            if codigo[contador] == codigo[len(codigo) - 1]:
                contador = 0
            else:
                contador += 1
        else:
            rotação += 1

    return total
