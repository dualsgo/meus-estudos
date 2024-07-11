# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print(f'\033[1;32mContém "Silva"\033[m' if 'Silva' in input('Digite seu nome completo: ') else '\033[1;31mNão contém "Silva"\033[m')