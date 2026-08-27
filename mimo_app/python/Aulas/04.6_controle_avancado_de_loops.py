# MIMO - 04 - Loops

# 4.6 - Controle avançado de loops

# Vamos explorar o uso de continue, break e else para controlar o fluxo do loop, pular iterações, sair antecipadamente ou executar código após o loop.

# continue é usado par apular o bloco de código atual e continuar com a próxima iteração do loop.

for i in range(1, 6):
    if i == 2:
        continue
    print(i)
    
# Se i for igual a 2, o bloco de código abaixo do continue não será executado e o loop continuará com a próxima iteração.
# Saída: 1, 3, 4, 5

# Use continue para pular elementos específicos, como "chips" em um loop, e passar para a próxima iteração.

shopping_list = ["apples", "bananas", "bread", "milk", "chips", "eggs"]

for item in shopping_list:
  if item == "chips":
    continue
  print(f"Don't forget to buy: {item}")

# O comando break sai completamente do loop. Se for invocado, ele não executa o restante das iterações.

for i in range(1, 6):
    if i == 3:
        break
    print(i)
    
# Podemos usar a palavra-chave break para sair de um loop while se uma determinada condição for atendida, como uma senha correspondente.

password = "open_sesame"

while True:
  if input("Enter the password: ") == password:
    print("Access granted!")
    break
  print("Incorrect password. Try again.")
  
# Finalmente, a declaração else em loops é executada quando o loop termina. Lembre-se, else em um loop difere de else em uma declaração if.

for i in range(1, 6):
    print(i)
else:
    print("Loop finished!")
    
# O bloco else só será executado se o loop não for encerrado antecipadamente por uma instrução break.

for i in range(1, 6):
    if i == 5:
        break
    print(i)
else:
    print("Loop finished!")