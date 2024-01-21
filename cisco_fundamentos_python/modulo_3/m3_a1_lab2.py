# 3.1.10 LAB Operadores de comparação e execução condicional
# Cenário

# Spathiphyllum, mais conhecido como um lírio da paz ou planta de vela branca, é um dos mais populares plantas de interior que filtra as toxinas nocivas do ar. Alguns dos efeitos tóxicos que ele neutraliza incluem o benzeno, o formaldeído e a amônia.

# Imagine que seu software adora essas fábricas. Sempre que recebe uma entrada na forma da palavra Spathiphyllum, involuntariamente grita para o console a seguinte string: "Spathiphyllum é a melhor fábrica de todos os tempos!"

# Escreva um programa que utilize o conceito de execução condicional, use uma string como entrada e:

# imprime a frase "Sim - Spathiphyllum é a melhor fábrica de todos os tempos!" para a tela se a sequência inserida for "Spathiphyllum" (maiúscula)

# imprime "Não, eu quero um grande Spathiphyllum!" se a sequência inserida for "spathiphyllum" (letra minúscula)

# Imprime "Spathiphyllum! Não [input]!", caso contrário. Nota: [input] é a string usada como entrada.
# Teste seu código usando os dados que fornecemos para você. E compre um Spathiphyllum também!

palavra = str(input('Digite uma palavra: ')).strip()

if palavra == 'Spathiphyllum':
    print('Sim - Spathiphyllum é a melhor fábrica de todos os tempos!')
elif palavra == 'spathiphyllum':
    print('Não, eu quero um grande Spathiphyllum!')
else:
    print(f'É Spathiphyllum! Não {palavra}!')