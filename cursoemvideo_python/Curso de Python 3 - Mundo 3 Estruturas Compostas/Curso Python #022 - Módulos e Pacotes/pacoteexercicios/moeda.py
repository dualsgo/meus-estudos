from pacoteexercicios import moeda

def aumentar(numero=0, num=1):
    try:
        aumentado = numero + (numero * (num / 100))
        return moeda(aumentado)

    except Exception as erro:
        print(erro)


def diminuir(numero=0, num=0):
    try:
        diminuido = numero - (numero * (num/100))
        return moeda(diminuido)
    except Exception as erro:
        print(erro)


def dobro(numero=0):
    dobrado = numero * 2
    return moeda(dobrado)


def metade(numero=0):
    meio = numero / 2
    return moeda(meio)


def moeda(numero=0):
    try:
        convertido = float(numero)
        money = f'R${convertido:.2f}'.replace('.', ',')
        return money
    except Exception as erro:
        print(erro)


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


def obter_valor_valido(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Valor inválido para essa operação!')