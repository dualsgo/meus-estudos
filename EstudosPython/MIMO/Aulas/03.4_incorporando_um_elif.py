# MIMO - 03 - Declarações Condicionais

# 03.4 - Incorporando um ELIF

# Vamos aprender como escrever instruções condicionais que tratam de condições específicas, como no programa abaixo. Ele usa instruções condicionais para mostrar saudações diferentes se a hora for inferior a 7, 12, 17, e 21.

# Usando if e else, podemos escrever um programa que mostre uma saudação se hora for menor que 12 e outra se não atender a condição

# Para uma condição mais específica, como se hora for maior que 12, mas menor que 17, podemos codificar elif hora < 17:

# elif significa 'senão se': elif é usado quando há uma segunda condição a ser verificada quando a condição do bloco if não foi atendida.

# Contanto que venha antes do else, podemos adicionar quantas instruções elif quisermos.

# Por se tratar de um intervalo limitado, vamos definir bem as condições.

hora = 5
if 4 < hora <= 11: # Dia entre 5 e 11
    print('Bom dia!')
elif 12 < hora <= 17: # Tarde entre 12 e 17
    print('Boa tarde!')
elif 18 < hora <= 23: # Noite entre 18 e 23
    print('Boa noite!')
else: # Madrugada será entre 24 e 4
    print('Boa madrugada!')

