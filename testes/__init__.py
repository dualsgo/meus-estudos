def retornar_lista(valor):
    valor.sort()
    return valor
    
print(retornar_lista(input('Valor: ').strip().replace('', ' ').split()))