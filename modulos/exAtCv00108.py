from uteis import moeda
from uteis import numeros

print('=' * 60)
print((f'{"manipulação de valores":^60}'))
print('=' * 60)
n = numeros.validação('Informe o valor a ser manipulador: ')
print('-' * 60)
n1 = numeros.validação('Informe a porcentagem de sua escolhar: ')
moeda.resumo(n, n1)
"""print('=' * 60)
print(f'O doblo de {moeda.moeda(n)} é {moeda.doblo(n, True)}.')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}.')
print(f'O aumento de {n1:5.2f}% em {moeda.moeda(n)} é {moeda.aumento(n, n1, True)}.')
print(f'A redução de {n1:5.2f}% em {moeda.moeda(n)} é {moeda.redução(n, n1, True)}.')
print('=' * 60)"""
