# MIMO - 03 - Declarações Condicionais

# 03.3 - Programando condições ELSE

# Um ótimo software não decide apenas o que fazer quando uma condição é True, mas também possui um plano de backup se a condição for False.

# Já sabemos que as instruções if nos ajudam a executar o código se uma condição como disponivel for True.
disponivel = True
if disponivel:
    # O código abaixo será executado, pois a condição é verdadeira.
    print('Em estoque!')

# Vamos adicionar outra instrução if que usa a variavel nao_diponivel para verificar se o item não está disponível.
nao_disponivel = True  # Confirma que o item não está disponível.

# Se o item não estiver disponível, queremos exibir uma mensagem diferente.
if nao_disponivel:
    # O código abaixo será executado, pois a condição é verdadeira.
    print('Sem estoque!')

# Em vez de criar duas instruções if, usamos uma instrução if/else para obter o mesmo resultado

disponivel = False # Controla se o item está disponível ou não.

# Se o item estiver disponível, queremos exibir uma mensagem.
if disponivel:
    # Se disponivel for True, o código abaixo será executado.
    print('Em estoque!')
    
# Se o item não estiver disponível, queremos exibir uma mensagem diferente.
else:
    # Se disponivel for False, o código abaixo será executado.
    print('Sem estoque!')

# Se o valor de dispoivel for atualizado para True, a estrutura acima irá avaliar novamente para decidir qual bloco de código executar.


# A instrução else vai sempre no final. Ela não precisa de sua própria condição, pois trata de casos em que a condição if não é atendida.

# É como uma resposta padrão. Aqui irá exibir 'Número incorreto!' para todos os números diferentes de 1.
numero = 13

if numero == 1:
    print('Número correto!')
else:
    print('Número incorreto!')
    
# As vezes não queremos apenas que o programa faça isso ou aquilo, mas queremos que ele faça isso e aquilo