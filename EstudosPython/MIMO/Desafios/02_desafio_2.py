# MIMO - 02 - Tipos e comparações - DESAFIO 2
# Lorde esqueceu sua senha e está usando um programa para restaurá-la. O programa verifica se a nova senha dela é diferente da antiga. Também faz com que lorde digite a nova sena duas vezes para ter certeza que está escrita corretamente. Vamos terminar esse programa.

old_password = 'hello123'
new_password = 'goodbye321'

# Tarefa 1: Use o operador de desigualdade em compare_old_new para mostrar que as senhas não são iguais.
compare_old_new = old_password != new_password
repeat_new_password = 'goodbye321'

# Tarefa 2: Certifique-se de que new_password corresponda a repeat_new_password.
compare_new = new_password == repeat_new_password

print(f'A nova senha é diferente da antiga? {compare_old_new}.')
print(f'A nova senha foi digitada corretamente? {compare_new}.')