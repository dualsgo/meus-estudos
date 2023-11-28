# MIMO - 03 - Declarações Condicionais

# 03.3 - Programando condições ELSE

# Um ótimo software não decide apenas o que fazer quando uma condição é True, mas também possui um plano de backup se a condição for False.

# Já sabemos que as instruções if nos ajudam a executar o código se uma condição como disponivel for True.
disponivel = True
if disponivel:
    print('Em estoque!')

# Vamos adicionar outra instrução if que usa nao_disponivel para executar o código diferente se a condição for False
if not disponivel:
    print('Sem estoque!')

# Em vez de criar duas instruções if, usamos uma instrução if/else para obter o mesmo resultado
if disponivel:
    print('Em estoque!')
else:
    print('Sem estoque!')

# A instrução else vai sempre no final. Ela não precisa de sua própria condição, pois trata de casos em que a condição if não é atendida.

# É como uma resposta padrão. Aqui irá exibir 'Número incorreto!' para todos os números diferentes de 1.
numero = 99
if numero == 0:
    print('Número correto!')
else:
    print('Número incorreto!')