# MIMO - 14 - Erros e exceções
# 14.2 - Levantando exceções

# Às vezes, queremos gerar uma exceção quando uma condição que definimos não é atendida.

"""slices = 18
diners = 0
if diners < 1:
  # após a palavra chave raise, podemos usar a palavra chave Exception para criar uma exceção personalizada colocando o texto que queremos que apareça quando a exceção for levantada entre parênteses.
  raise Exception("There must be at least one diner.")
else:
  slices_per_diner = slices / diners
  print(f"Each person gets {slices_per_diner} slices of pizza.")"""
  
  
# A palavra chave raise é usada para levantar uma exceção. Quando a exceção é levantada, o programa para de ser executado e o traceback é mostrado.

# Podemos usar exceções para destacar quando algo não pode estar funcionando como deveria.
# Podemos usar condições para validar entradas e gerar execução quando as condições não são atendidas.

# Muitas vezes não queremos que um programa termine quando uma exceção é encontrada. Um bloco try except pode ser usado para tratamento de exceções!

# Os blocos try e except tender a ser usados onde sabemos que há uma chanve de a operação não ser possível. Por exemplo, quando tentamos abrir um arquivo, ele pode não existir. Nesse caso, podemos usar um bloco try except para lidar com a exceção.

# Usamos recuos para indicar que o código está dentro do bloco try. Se o código dentro do bloco try levantar uma exceção, o código dentro do bloco except será executado.
# Podemos usar pass para indicar que não queremos fazer nada no bloco except.

try:
    print('Hello' + 'user')
except:
    pass
  
#A palavra chave raise é usada junto com um tipo válido de erro e uma mensagem opicional. Geralmente é usado dentro do bloco de código except para levantar uma exceção quando uma condição é atendida.

# Podemos usar a instrução else no final se quisermos executar algum código somente quando nenhum erro for levantado.

details = {"name": "Ricky", "age": 24, "job": "Programmer"}

try:
    age = details["age"]
except:
    raise NameError("Age is not defined")
else:
    print("No errors were found")
  
# Podemos usar uma instrução finally para executar um código, independentemente de uma exceção ser levantada ou não.
finally:
    print("The try except block is finished")