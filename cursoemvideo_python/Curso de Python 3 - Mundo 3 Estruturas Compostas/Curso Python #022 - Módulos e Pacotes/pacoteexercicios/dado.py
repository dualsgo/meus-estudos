def leia_dinheiro(dado):
    while True:
        if dado.isnumeric():
            return f'R${int(dado):.2f}'
        else:
            print(f'Dado "{dado}" não é válido!')
            dado = input('').strip()