from uteis import numeros

print('=' * 40)
print((f'{"manipulação de valores":^40}'))
print('=' * 40)
n = int(input('Informe o valor a ser manipulador: '))
print('-' * 40)
n1 = float(input('Informe a porcentagem de sua escolhar: '))
print('=' * 40)
print(f'O doblo de {n} é {numeros.doblo(n):5.2f}.')
print(f'A metade de {n} é{numeros.metade(n):5.2f}.')
print(f'O aumento de {n1}% em {n} é {numeros.aumento(n, n1):5.2f}.')
print(f'A redução de {n1}% em {n} é {numeros.redução(n, n1):5.2f}.')
print('=' * 40)