# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

print('\033[1;32mComeça com Santo."\033[m' if input('Digite o nome da cidade: ').strip().title().split()[0] == 'Santo' else '\033[1;31mNão começa com "Santo"\033[m')

print('\033[1;32mComeça com "Santo"\033[m' if input('Nome da cidade: ').strip().title().startswith('Santo') else '\033[1;31mNão começa com "Santo"\033[m')