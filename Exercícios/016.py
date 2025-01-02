# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

valor = float(input('Digite um valor qualquer: '))
print('O valor digitado é {} e a sua porção inteira é {}'.format(valor, trunc(valor)))

# Ou
print('O valor digitado é {} e a sua porção inteira é {:.0f}'.format(valor, valor))

# Ou
print('O valor digitado é {} e a sua porção inteira é {}'.format(valor, int(valor)))