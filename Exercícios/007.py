# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
print('A média de {} + {} é {}'.format(nota1, nota2, (nota1 + nota2) / 2))