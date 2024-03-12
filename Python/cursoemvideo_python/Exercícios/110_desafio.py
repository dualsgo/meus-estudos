# Exercício Python #110 - Reduzindo ainda mais seu programa - Aula 00 até 22 - Mundo 3
# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from pacoteexercicios import moeda

valor = float(input('Digite um valor: R$ '))
taxa_aumento = int(input(f'Aumentar {moeda.moeda(valor)} em quantos % '))
taxa_reducao = int(input(f'Diminuir {moeda.moeda(valor)} em quantos % '))

moeda.resumo(valor, taxa_aumento, taxa_reducao)