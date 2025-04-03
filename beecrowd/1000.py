def palavra_valida(texto):
    palavra = input(texto).strip()
    while not palavra.isalpha():
        palavra = input('Deve conter somente letras... ').strip()
    
    return palavra


entrada = palavra_valida('Digite uma palavra: ')
ao_contrario = entrada[::-1].title()

print(f'Palavra: {entrada}, ao contrário: {ao_contrario}')
print('É palíndromo!' if ao_contrario == entrada else 'Não é palíndromo.')