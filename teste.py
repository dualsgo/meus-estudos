idade = int(input('Digite a sua idade: '))

if idade >= 16:
    print(f'Com {idade} anos você está apto para votar!')
    if idade >= 18 and idade <= 70:
        print('Seu voto é obrigatório!')
    else:
        print('Seu voto é facultativo!')

    if idade >= 18:
        print('Você tem idade suficiente para dirigir!')
        habilitado = input('Possui habilitação? (S ou N): ')
        if habilitado == 'S':
            print('Como possui habilitação, você está apto para dirigir!')
        else:
            print(
                'Apesar de ter idade suficiente, você não é habilitado, portanto não deve dirigir!')
    else:
        print('Você não tem idade suficiente para dirigir!')
else:
    print(f'Com {idade} anos você não está apto para votar!')
