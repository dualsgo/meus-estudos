# Curso Python Aula 04 - Introdução aos Comandos Iniciais em Python

'''RESUMO'''

# Comandos básicos em Python, enfatizando a função print() para exibir mensagens na tela e o uso de aspas para delimitar mensagens e realizar cálculos com números.
# Introdução ao conceito de variáveis e como elas armazenam informações, incluindo representação de strings com aspas e concatenação de várias strings.
# Interatividade com o usuário por meio da função input, permitindo a personalização das saídas dos programas.
# Criação e execução de scripts Python para programar e testar funcionalidades de maneira eficiente.
# Apresentação de três desafios práticos para os espectadores, incentivando a aplicação dos conceitos aprendidos.

'''CONTEÚDO'''

# Função print()
# Em Python, todos os comandos são funções, e todas as funções são chamadas usando parênteses. Para exibir mensagens de texto, é necessário envolvê-las entre aspas, como em:
print('Olá, Mundo!')  # Isso exibirá 'Olá, Mundo!'

# Caso contrário, sem as aspas, ocorrerá um erro "SyntaxError: invalid syntax".

# Quando trabalhamos com números, não é necessário usar aspas. Por exemplo, a expressão a seguir retornará o valor 11:
print(7 + 4)  # Exibirá 11

# Se você adicionar números entre aspas, eles serão tratados como texto e concatenados, como em:
print('7' + '4')  # Isso exibirá '74'

# É possível unir textos usando o operador + ou a vírgula. Entretanto, ao usar o operador + para concatenar, lembre-se de que ele só funciona com tipos string. Caso contrário, você receberá um erro "TypeError: must be str, not int".

# Por exemplo:
# print('Olá' + 5)  # Isso gerará um erro.

# Por outro lado, a concatenação com vírgula permite a utilização de tipos diferentes, como mostrado abaixo:
print('Olá', 5)  # Isso exibirá 'Olá 5'

# Variáveis

# Variáveis em Python são objetos que recebem valores e armazenam essas informações. O operador de atribuição = pode ser lido como "recebe". Por exemplo:

nome = 'Guanabara'  # Soa como nome recebe Guanabara
idade = 25  # idade recebe 25
peso = 75.8  # peso recebe 75.8

# Podemos mostrar os valores dessas variáveis usando a instrução print(), assim:
print(nome, idade, peso)  # Isso exibirá Guanabara 25 75.8

# Função input()
# A função input() em Python permite que o usuário insira um valor, que será armazenado em uma variável. Por exemplo:

# nome recerá o valor digitado pelo usuário em vez de ter um valor pré definido como no exemplo anterior.
nome = input('Digite o seu nome: ')

# A mensagem entre os parênteses será exibida no console.
idade = input('Digite a sua idade: ')

# Com isso, o programa espera que o usuário digite seu nome, idade e peso, armazenando essas informações nas variáveis correspondentes, e em seguida, exibe esses valores com a instrução print().
peso = input('Digite o seu peso: ')

# Isso exibirá os valores fornecidos pelo input. O tipo padrão de retorno do input() é str, portanto é possível nesse caso concatenar as variáveis nome, idade e peso com o operador +.
print(nome, idade, peso)
