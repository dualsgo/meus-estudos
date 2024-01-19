# 2.4.9 LAB Variáveis ‒ um simples conversor
# Cenário
# Milhas e quilômetros são unidades de comprimento ou distância.

# Lembrando que 1 milha (1,61 km) é igual a aproximadamente 1,61 quilômetros, complete o programa no editor para converter:

# Milhas em quilômetros;
# quilômetros em milhas.
# Não altere nada no código atual. Escreva seu código nos locais indicados por ###. Teste seu programa com os dados que fornecemos no código-fonte.

# Preste atenção especial ao que está acontecendo na função de print(). Analise como fornecemos multiples argumentos para a função e como produzimos os dados esperados.

# Observe que alguns dos argumentos dentro da função print() são strings (por exemplo, "milhas é", enquanto outros são variáveis (por exemplo, miles).

# Dica
# Há mais uma coisa interessante acontecendo lá. Você pode ver outra função dentro da função print()? É a função round(). Seu trabalho é arredondar o resultado de saída para o número de casas decimais especificadas entre parênteses e retornar um float (dentro da função round() você pode encontrar o nome da variável, uma vírgula e o número de casas decimais que pretendemos por). Falaremos sobre funções muito em breve, então não se preocupe que tudo pode não estar totalmente claro ainda. Só queremos despertar a sua curiosidade.

# Após concluir o laboratório, abra o Sandbox e experimente um pouco mais. Tente escrever conversores diferentes, por exemplo, um conversor de USD para EUR, um conversor de temperatura, etc. - deixe sua imaginação voar! Tente gerar os resultados combinando strings e variáveis. Tente usar e experimentar a função round() para arredondar seus resultados para uma, duas ou três casas decimais. Confira o que acontece se você não fornecer nenhum número de dígitos. Lembre-se de testar seus programas.

# Experimente, tire conclusões e aprenda. Seja curioso.

# Saída esperada
# 7,38 milhas (ca. 12 km) é 11,88 quilômetros
# 12,25 quilômetros é 7,61 milhas (ca. 12 km)

milhas = 1.61
print(f'1 quilômetro equivale a {milhas} milhas')
kilometres = 1 / milhas
print(f'1 milha equivale a {round(kilometres, 2)} quilômetros')
milhas_convertidas = 7.38 * milhas
kilometres_convertidos = 12.25 / milhas
print(f'7.38 milhas é {round(milhas_convertidas, 2)} quilômetros.')
print(f'12.25 quilômetros é {round(kilometres_convertidos, 2)} milhas.')