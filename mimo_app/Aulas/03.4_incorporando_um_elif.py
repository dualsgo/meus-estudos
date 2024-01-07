# MIMO - 03 - Declarações Condicionais

# 03.4 - Incorporando um ELIF

# Vamos aprender como escrever instruções condicionais que tratam de condições específicas, como no programa abaixo. Ele usa instruções condicionais para mostrar saudações diferentes se a hora for inferior a 7, 12, 17, e 21.

# Usando if e else, podemos escrever um programa que mostre uma saudação se hora for menor que 12 e outra se não atender a condição

# Para uma condição mais específica, como se hora for maior que 12, mas menor que 17, podemos codificar elif hora < 17:

# elif significa 'senão se': elif é usado quando há uma segunda condição a ser verificada quando a condição do bloco if não foi atendida.

# Contanto que venha antes do else, podemos adicionar quantas instruções elif quisermos.

# Por se tratar de um intervalo limitado, vamos definir bem as condições.

hora = 12 # Define a hora atual


# Se a hora for menor que 12, exibe 'Bom dia!'
if 5 <= hora <= 11:  # Dia entre 5 e 11
    print('Bom dia!')
    
# Se a hora for maior que 12, mas menor que 17, exibe 'Boa tarde!'
elif 12 <= hora <= 17:  # Tarde entre 12 e 17
    print('Boa tarde!')
    
# Se a hora for maior que 17, mas menor que 23, exibe 'Boa noite!'
elif 18 <= hora <= 23:  # Noite entre 18 e 23
    print('Boa noite!')

# Se a hora for maior que 23, mas menor que 5, exibe 'Boa madrugada!'
# Basicamente, se nenhuma das condições acima for atendida, exibe 'Boa madrugada!'
else:  # Madrugada será entre 24 e 4
    print('Boa madrugada!')
    
# Diferença entre usar if elif e if if
hora = 10

# if elif é usado quando queremos que o programa execute apenas uma das condições.
# Exemplo de if elif
if 5 <= hora <= 11:  # Dia entre 5 e 11
    print('Bom dia!')
elif hora == 10:
    print('São 10 horas!')

# Se a hora for entre 5 e 11, o programa irá exibir 'Bom dia!'. Como a condição foi atendida, o programa não irá verificar as outras condições. Mesmo que seja 10 horas, o programa não irá exibir 'São 10 horas!' pois instruímos ele a exibir apenas uma das condições.


# if if é usado quando queremos que o programa execute todas as condições que forem atendidas.
# Exemplo de if if
if 5 <= hora <= 11:  # Dia entre 5 e 11
    print('Bom dia!')
if hora == 10:
    print('São 10 horas!')
    
# Se a hora for entre 5 e 11, o programa irá exibir 'Bom dia!'. Como há outra condição, o programa irá verificar se ela é atendida. Como é 10 horas, o programa irá exibir 'São 10 horas!'. Como instruímos ele a exibir todas as condições, ele irá exibir todas as condições que forem atendidas.