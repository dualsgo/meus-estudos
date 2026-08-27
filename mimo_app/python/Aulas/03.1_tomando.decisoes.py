# MIMO - 03 - Declarações Condicionais

# 03.1 - Tomando decisões

# Condições e declarações condicionais
# Programas inteligentes usam booleans (True e False) para tomar decisões sobre executar linhas de código ou ignorá-las.

# Usamos uma instrução SE (if) para escrever código que responda a diferentes situações. Nós utilizamos a palavra-chave if. A instrução só executa o código se a condição for avaliada como verdade (True). É como dizer 'SE algo é verdade, faça isso'

# Podemos salvar o valor boolean em uma variável.
algo = True

# Valores como True são chamados de condições e declarações que dependem de condições são chamadas de condicionais. As condições ficam entre o if e :, decidindo se o código será executado ou ignorado.

if algo:
    print('É verdade!')

# Se quisermos pular o código, a condição deverá ser falsa (False)
algo = False
if algo:
    print('Falso!')  # Nada será exibido
    
# Bloco de código
# As instruções if não decide pular ou executar o código inteiro. Eles só tomam decisões sobre um bloco de código.

# Usamos o recuo de dois espaços para destacar blocos de código. O recuo refere-se ao espaço entre o código e a margem do editor de código.

# Um bloco de código pode ser mais do que uma linha. Todas as linhas com o mesmo recuo pertencem ao mesmo bloco de código.

# Se o recuo estiver incorreto, o computador não conseguirá entender seu código. Isso retorna um erro Indentation Error no console.

# Qualquer código que não esteja recuado será executado independentemente da condição.
print('Será executada independente do resultado!')



