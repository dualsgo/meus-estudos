import pacoteexercicios

def escolha(e, a):
    if e == 1:
        print(f'{'Aumentar':^30}')
        return aumentar(a)
    elif e == 2:
        print(f'{'Diminuir':^30}')
        return diminuir(a)
    elif e == 3:
        print(f'{'Dobrar':^30}')
        return dobro(a)
    elif e == 4:
        print(f'{'Metade':^30}')
        return metade(a)
    elif e == 5:
        print(f'{'Em BRL':^30}')
        return moeda(a)