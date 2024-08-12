def escolha(e, a):
    if e == 1:
        return aumentar(a)
    elif e == 2:
        return diminuir(a)
    elif e == 3:
        return dobro(a)
    elif e == 4:
        return metade(a)
    elif e == 5:
        return moeda(a)


def aumentar(numero, num=1):
    aumentado = numero + num
    return aumentado


def diminuir(numero, num=1):
    diminuido = numero - num
    return diminuido


def dobro(numero):
    dobrado = numero * 2
    return dobrado


def metade(numero):
    meio = numero / 2
    return meio


def moeda(numero):
    numero = float(numero)
    monetario = f'R$ {numero:.2f}'
    return monetario