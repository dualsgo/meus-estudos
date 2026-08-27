# Exercício Python #008 - Conversor de Medidas
# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor_em_metros = float(input('Digite um valor em metros: '))

em_km = valor_em_metros / 1000
em_hm = valor_em_metros / 100
em_dam = valor_em_metros / 10
em_dm = valor_em_metros * 10
em_cm = valor_em_metros * 100
em_mm = valor_em_metros * 1000

print(f'{'Em quilômetros':<15}{em_km:>10}{'km':>5}')
print(f'{'Em hectômetros':<15}{em_hm:>10}{'hm':>5}')
print(f'{'Em decâmetros':<15}{em_dam:>10}{'dam':>5}')
print(f'\033[31m{'Em metros':<15}{valor_em_metros:>10}{'m':>5}\033[m')
print(f'{'Em decímetros':<15}{em_dm:>10}{'dm':>5}')
print(f'{'Em centímetros':<15}{em_cm:>10}{'cm':>5}')
print(f'{'Em milímetros':<15}{em_mm:>10}{'mm':>5}')