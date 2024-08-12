
m = int(input('Quantos metros deseja calcular?: '))
medidas = ('Km', m/1000, 'Hm', m/100, 'Dam', m/10, 'Dm', m*10, 'Cm', m*100, 'Mm', m*1000)


def titulo():
    print(f'{'-=' * 20}')
    print(f"{'Conversor de medidas':^20}")
    print(f'{'-=' * 20}')
    print('-' * 40)
    for pos in range(0, (len(medidas))):
        if pos % 2 == 0:
            print(f'|- {m} metros para {medidas[pos]:.<10}', end=' ')
        else:
            print(f'{medidas[pos]:.>7.1f}    |')
    print('-=' * 20)


titulo()