valor_saque = int(input('Digite o valor: R$ '))

for cedula in [100, 50, 20, 10, 5, 2]:
    quantidade = 0
    if valor_saque >= cedula:
        quantidade = valor_saque // cedula 
        print(f'Sacando {quantidade} cédula de R$ {cedula}')
        valor_saque %= cedula
