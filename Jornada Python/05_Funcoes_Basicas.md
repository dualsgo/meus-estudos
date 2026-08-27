# Funções Básicas e Interação

## EXPLICAÇÃO

Python oferece funções embutidas (*built-in*) que facilitam a interação e formatação de dados sem a necessidade de importar módulos externos.

1. **`print()`**: Exibe informações na saída padrão.
    * **Argumentos Posicionais:** Valores separados por vírgula.
    * **`sep=' '`**: Define o separador entre os argumentos (padrão é espaço).
    * **`end='\n'`**: Define o que imprimir ao final (padrão é quebra de linha).
2. **`input()`**: Solicita uma entrada do usuário. **Importante:** Sempre retorna uma String (`str`). Se precisar de números, deve-se usar o *casting* (ex: `int(input())`).
3. **Interpolação de Strings (f-strings):** A forma mais moderna e eficiente de inserir variáveis em textos usando `{variavel}` dentro de uma string prefixada com `f`.
4. **ANSI Colors:** Permite colorir a saída do terminal usando códigos como `\033[STYLE;COLORm`.

## EXEMPLO PRÁTICO

```python
# Uso avançado do print
print("Python", "é", "demais", sep="-", end="!!!\n")

# Entrada de dados com casting
idade = int(input("Digite sua idade: "))
print(f"Você tem {idade} anos.")

# Texto com cores (Negrito e Verde)
print("\033[1;32mAcesso Garantido!\033[0m")

# Replicação de strings
print("-" * 20)
```
