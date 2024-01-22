# 3.2.9 LAB A declaração break – Preso em um loop
# Cenário
# A declaração break é usada para sair/encerrar um loop.

# Projete um programa que use um loop while e solicite continuamente que o usuário insira uma palavra.
# Caso o usuário insira "chupacabra" como a palavra de saída secreta, exiba a
# mensagem "Você saiu do loop com sucesso" e termine o loop.

while True:
    palavra = input('Digite uma palavra: ')
    if palavra == 'chupacabra':
        break
print('Você saiu do loop com sucesso!')