# Exercício Python #058 - Jogo da Adivinhação v2.0 - Aula 00 até 14 - Mundo 2
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from emoji import emojize
from random import randint
print(emojize('Sou o seu computador... :rosto_de_robô:\nAcabei de pensar em um número entre 0 e 10. :rosto_pensativo:\nTente adivinhar!', language='pt'))
palpites = 1  # Inicializa o contador de palpites
computador = randint(0, 10)  # Gera um número aleatório entre 0 e 10

jogador = int(input('Digite seu palpite: '))  # Solicita e converte o palpite do jogador para inteiro

while jogador != computador:
    palpites += 1  # Incrementa o contador de palpites
    print(emojize('ERROU! :xis:', language='pt'))  # Exibe mensagem de erro
    print(emojize(':seta_para_cima: Mais...', language='pt') if jogador < computador else emojize(':seta_para_baixo: Menos...', language='pt'))
    jogador = int(input('Tente outro palpite: '))  # Solicita outro palpite ao jogador

print(emojize(f'Acertou com {palpites} palpites! :cone_de_festa:', language='pt'))  # Exibe mensagem de acerto com o número de palpites realizados

if palpites < 2:
    print('Você lê mentes')
elif palpites < 3:
    print('Essa foi sorte!')
elif palpites < 4:
    print('Você foi bem!')
elif palpites < 5:
    print('Esse é o mínimo de tentativas se utilizar a estratégia certa!')
else:
    print('Reveja sua estratégia!')

