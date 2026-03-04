# MIMO - 02 - Tipos e comparações - DESAFIO 2
# Lorde esqueceu sua senha e está usando um programa para restaurá-la. O programa verifica se a nova senha dela é diferente da antiga. Também faz com que lorde digite a nova sena duas vezes para ter certeza que está escrita corretamente. Vamos terminar esse programa.

senha_antiga = 'hello123'
nova_senha = 'goodbye321'

# Tarefa 1: Use o operador de desigualdade em comparar_senhas para mostrar que as senhas não são iguais.
comparar_senhas = senha_antiga != nova_senha
repetir_nova_senha = 'goodbye321'

# Tarefa 2: Certifique-se de que nova_senha corresponda a repetir_nova_senha.
comparar_nova_senha = nova_senha == repetir_nova_senha

print(f'A nova senha é diferente da antiga? {comparar_senhas}.')
print(f'A nova senha foi digitada corretamente? {comparar_nova_senha}.')