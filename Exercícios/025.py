# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

nome = input('Digite seu nome: ').strip()
texto = nome.lower().split()
print(f'Seu nome {"tem" if "silva" in texto else "não tem"} Silva no nome.')