# 4.3.8 LAB Convertendo o consumo de combustível

# O consumo de combustível de um carro pode ser expresso de várias maneiras diferentes. Por exemplo, na Europa, ele é mostrado como a quantidade de combustível consumida por 100 quilômetros.

# Nos EUA, é mostrado como o número de quilômetros percorridos por um carro usando um litro de combustível.

# Sua tarefa é escrever um par de funções convertendo l/100 km em mpg e vice-versa.

# As funções:

# são nomeados liters_100km_to_miles_gallon e miles_gallon_to_liters_100km respectivamente;
# use um argumento (o valor correspondente aos nomes)

# Aqui estão algumas informações para ajudá-lo:

# 1 milha americana = 1609.344 metros;
# 1 galão americano = 3,785411784 litros.

# Saída prevista:
"""
60.31143162393162
31.36194444444444
23.52145833333333
3.9007393587617467
7.490910297239916
10.009131205673757
"""

def liters_100km_to_miles_gallon(liters):
    miles = 100 * 1000 / 1609.344
    gallons = liters / 3.785411784
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km = miles * 1609.344 / 1000
    liters = 3.785411784
    return 100 * liters / km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))