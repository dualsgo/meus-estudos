# 3.2.10 LAB A declaração continue – o Feio Comedor de Vogais
# Cenário
# A instrução continue é usada para ignorar o bloco atual e avançar para a próxima iteração, sem executar as instruções dentro do loop.
# Ele pode ser usado com loops while e for.

# Sua tarefa aqui é muito especial: você deve criar um comedor de vogal!
# Escreva um programa que use:
# um loop for
# o conceito de execução condicional (if-elif-else)
# a declaração continue.

# Seu programa deve:
# peça ao usuário para inserir uma palavra;
# use user_word = user_word.upper() para converter em maiúsculas a palavra inserida pelo usuário; falaremos sobre métodos de string o método top upper() muito em breve - não se preocupe;
# use execução condicional e a declaração continue para "consumir" as seguintes vogais A, E, I, O, U da palavra inserida;
# imprima as letras não consumidas na tela, cada uma delas em uma linha separada.

# Solicita que o usuário insira uma palavra e atribua-a à variável user_word.
user_word = input('Digite uma palavra: ').strip().upper()  # strip() remove
# espaços em branco desnecessários e upper() converte para maiúsculas
for letter in user_word:  # para cada letra na palavra do usuário
    if letter in 'AEIOU':  # se a letra for uma vogal
        continue  # continue para a próxima iteração do loop
    print(letter, end='')  # Imprime a letra que não atendeu a condição do if, ou seja, não é vogal. Separando-as por espaço