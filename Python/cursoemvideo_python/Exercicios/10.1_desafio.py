# Exercício Python #010 - Conversor de Moedas - Aula 00 até 07 - Mundo 1
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27.

while True:
    carteira = float(input('Digite quanto possui na carteira: R$ '))
    print('Qual moeda deseja converter?')
    print('[1] R$ - Real')
    print('[2] U$ - Dólar')
    print('[3]  € - Euro')
    converter = int(input(''))
    while converter == 1 or 2 or 3:
        if converter == 1:
            print('Deseja converter R$ - Real para qual moeda?')
            print('[1] U$ - Dólar')
            print('[2]  € - Euro')
            para = int(input(''))
            if para == 1:
                print('Converter R$ - Real para U$ - Dólar')
                cotacao_dolar = 4.90
                dolar = carteira / cotacao_dolar
                print(
                    f'Você possui R$ {carteira:.2f}. Na cotação atual (US$ 1,00 = R$ 3.27) você pode comprar US$ {dolar:.2f}.')
            continuar = int(input('[1] Continuar ou [2] Encerrar'))
            while continuar != 1 or 2:
                print('Opção inválida!')
                continuar = int(input('[1] Continuar ou [2] Encerrar'))
                if continuar == 2:
                    print('Encerrando o programa!')
                    break
                else:
                    continue













carteira = float(input('Digite quanto possui na carteira: R$ '))

cotacao_dolar = 4.90
cotacao_euro = 5.36
cotacao_peso = 72.89

dolar = carteira / cotacao_dolar
euro = carteira / cotacao_euro
peso = carteira * cotacao_peso

print(f'Você possui R$ {carteira:.2f}. Na cotação atual (US$ 1,00 = R$ 3.27) você pode comprar US$ {dolar:.2f}.')
print('')
print(f'Você possui R$ {carteira:.2f}. Na cotação atual (1,00 € = R$ 5.36) você pode comprar {euro:.2f} €.')
print('')
print(f'R$ {carteira:.2f} equivalem a $ {peso:.2f} pesos argentinos.')
