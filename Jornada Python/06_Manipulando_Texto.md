# Manipulação de Texto (Strings)

## EXPLICAÇÃO

Strings em Python são sequências imutáveis de caracteres. Isso significa que métodos de string sempre retornam uma **nova** string, sem alterar a original.

1. **Fatiamento (*Slicing*):** `string[início:fim:passo]`.
    * O índice inicial é incluído, mas o final é **excluído**.
2. **Análise:**
    * `len()`: Tamanho da string.
    * `.count()`: Conta ocorrências de um caractere/trecho.
    * `.find()` / `.index()`: Localiza a posição de um trecho. (`find` retorna -1 se não encontrar, `index` gera erro).
3. **Transformação:**
    * `.upper()` / `.lower()`: Maiúsculas/Minúsculas.
    * `.capitalize()` / `.title()`: Formata início de frases ou palavras.
    * `.strip()`: Remove espaços inúteis no início e fim.
    * `.replace()`: Substitui trechos de texto.
4. **Verificação (is...):** `.isalpha()`, `.isnumeric()`, `.isalnum()`, etc.

## EXEMPLO PRÁTICO

```python
frase = "  Jornada Python  "

# Slicing e Transformação
print(frase.strip().upper()) # "JORNADA PYTHON"
print(frase[2:9])            # "Jornada"

# Busca e Substituição
nova_frase = frase.replace("Python", "Expert")
print(nova_frase)

# Verificações
print("123".isnumeric()) # True
print("Python".isalpha()) # True

# Inversão de string
print(frase[::-1])
```
