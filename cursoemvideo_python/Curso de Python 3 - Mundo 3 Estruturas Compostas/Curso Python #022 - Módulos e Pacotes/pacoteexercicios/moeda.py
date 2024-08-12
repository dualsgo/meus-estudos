def aumentar(numero=0, num=0):
    aumentado = numero + (numero * (num/100))
    return moeda(aumentado)


def diminuir(numero=0, num=0):
    diminuido = numero - (numero * (num/100))
    return moeda(diminuido)


def dobro(numero=0):
    dobrado = numero * 2
    return moeda(dobrado)


def metade(numero=0):
    meio = numero / 2
    return moeda(meio)


def moeda(numero=0):
    money = f'{numero:.2f}'.replace('.', ',')
    return money

def resumo(v, ta=10, tr=10):
    valor = v
    taxa_aumento = ta
    taxa_reducao = tr
    # Aumentando
    print(f'O valor {moeda(valor)} aumentado em {taxa_aumento}% é {aumentar(valor, ta)}')
    # Diminuindo
    print(f'O valor {moeda(valor)} diminuído em {taxa_reducao}% é {diminuir(valor, tr)}')
    # Dobrando
    print(f'O valor {moeda(valor)} dobrado é {dobro(valor)}')
    # Dividindo
    print(f'O valor {moeda(valor)} pela metade é {metade(valor)}')