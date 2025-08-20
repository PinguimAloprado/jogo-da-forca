#import uteis
# no caso tb pode ser [from uteis import fatorial, doblo ]
#from modulos.uteis import numeros    ///   para importar modulos em pastas vizinhas
from uteis import numeros
print('=' * 40)
print('    Descubra o fatorial de um numero')
print('=' * 40)
nu = int(input('Informe um numero de sua escolhar: '))
re = numeros.fatorial(nu)
print('=' * 40)
print(f'O fatorial de {nu} é {re}.')
print(f'O doblo de {nu} é {numeros.doblo(nu)}')
print('=' * 40)
