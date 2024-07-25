# Exercício Python #089 - Boletim com listas compostas - Aula 00 até 18 - Mundo 3
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from emoji import emojize

boletim = []

# Loop para entrada de dados
while True:
    nome = str(input(emojize(':aluno: Aluno: ', language='pt'))).strip().title()
    nota1 = float(input(emojize(':memorando: NOTA 1: ', language='pt')))
    nota2 = float(input(emojize(':memorando: NOTA 2: ', language='pt')))
    media = (nota1 + nota2) / 2

    # Adiciona os dados do aluno à lista composta
    boletim.append([nome, [nota1, nota2, media]])

    continuar = str(input('Continuar? S/N ')).strip().upper()

    # Loop para garantir que o usuário forneça uma entrada válida
    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()

    # Se o usuário escolher 'N', exibe o boletim e encerra o programa
    if continuar == 'N':
        print('Encerrando...')
        print(f'{"BOLETIM DA TURMA":^20}')
        print(f'{"Número":<8}{"Nome":<10}{"Média":>8}')
        for i, aluno in enumerate(boletim):
            nome = aluno[0]
            nota1, nota2, media = aluno[1]
            # Formatação melhorada usando f-strings
            print(f'{i:<8}{nome:<10}{media:>8.1f}')
        break

# Loop para visualizar as notas de cada aluno individualmente
while True:
    ident = int(input('Digite o ID do aluno:'))

    # Verifica se o ID do aluno é válido
    if 0 <= ident < len(boletim):
        # Desempacotamento dos valores para nome e notas
        nome, notas = boletim[ident]

        # Atribuição de valores individuais para nota1, nota2 e media
        nota1, nota2, media = notas

        # Formatação melhorada usando f-strings para imprimir as informações do aluno
        print(f'O aluno {nome} teve as notas {nota1} e {nota2}. Sua média foi {media}')
    else:
        # Caso o ID seja inválido, exibe uma mensagem de erro
        print('ID do aluno inválido. Tente novamente.')

    continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Loop para garantir que o usuário forneça uma entrada válida
    while continuar not in 'SN':
        continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Se o usuário escolher 'N', encerra o programa
    if continuar == 'N':
        print('Encerrando...')
        break


"""**Desempacotamento:**

No Python, o desempacotamento é um recurso que permite atribuir os elementos de uma sequência (como uma lista ou tupla) a variáveis individuais. No trecho de código mencionado:

```python
# Desempacotamento dos valores para nome e notas
nome, notas = boletim[ident]
```

- `boletim[ident]` retorna uma lista que representa as informações de um aluno específico no boletim.
- `nome, notas` realiza o desempacotamento, atribuindo o primeiro elemento da lista (nome) à variável `nome` e o segundo elemento (que é uma lista de notas) à variável `notas`.

**Atribuição de valores individuais:**

Após o desempacotamento, a linha seguinte realiza a atribuição de valores individuais às variáveis `nota1`, `nota2`, e `media`:

```python
# Atribuição de valores individuais para nota1, nota2 e media
nota1, nota2, media = notas
```

- `notas` é a lista que contém as notas do aluno, onde `notas[0]` é a primeira nota, `notas[1]` é a segunda nota, e `notas[2]` é a média.
- `nota1, nota2, media` realiza a atribuição desses valores individuais às variáveis correspondentes.

Então, após essa linha de código, você tem acesso direto às notas individuais do aluno através das variáveis `nota1` e `nota2`, bem como à média através da variável `media`. Isso facilita o uso desses valores posteriormente no código, como na linha seguinte onde eles são usados na impressão formatada.

Em resumo, o desempacotamento e a atribuição de valores individuais ajudam a tornar o código mais legível e a facilitar o acesso a elementos específicos dentro de listas ou tuplas."""