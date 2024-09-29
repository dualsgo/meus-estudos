# Vamos criar um sistema para o usuário digitar um valor numério e iremos converter para hexadecimal e combinar com um texto para exibir um emoji aleatrório

# Recebemos o valor inteiro do usuário

while True:
  try:
    valor = int(input("Digite um valor inteiro: "))
    break
  except:
    print("Digite um valor inteiro válido")
    

# Convertendo o valor para hexadecimal
convertido = hex(valor)

unicode = '\\U0001' + str(convertido[2:])

print(unicode)