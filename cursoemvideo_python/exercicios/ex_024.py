"""Desafio 024 - Título (Aula 01 a 09): Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'SANTO'
"""
# Passo 1: Ler o nome da cidade - Armazenamos o valor obtido através do input em uma variável. O input recebe o tratamento com strip para remover possíveis espaços adicionais. Poderia ser utilizado lstrip pra remover somente os do início
print("""\033[1;31;40mDIGITE O NOME DA SUA CIDADE!\033[m""")
cidade = str(input('')).strip()

# Passo 2: Verificar se começa com SANTO - Como queremos o início, indicamos a variavel com o inicio omitido e sinalizamos o ultimo caracter como 5 pois assim será considerado do indice zero ate 4 (5 digitos). Usamos upper() para deixar a string em maiusculas independente da forma digitada e o operador de igualdade para comparar a string com 'SANTO'
if cidade[:5].upper() == 'SANTO':
    # Nessa saída foi utilizado if e else para exibir uma frase diferente para cada caso

    # Se a comparação for verdadeira exibirá True, se não for exibirá False.
    print(
        f'\033[1;32mSIM\033[m. O nome da cidade digitada \033[32minicía\033[m com "SANTO".')
else:
    print(
        f'\033[1;31mNÃO\033[m. O nome da cidade digitada \033[31mnão inicía\033[m com "SANTO".')
