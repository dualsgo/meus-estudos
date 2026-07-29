# Estruturas de Repetição (Loops)

## EXPLICAÇÃO

Loops permitem repetir blocos de código sem a necessidade de reescrevê-los.

1. **`while`**: Repete **enquanto** uma condição for verdadeira. Ideal quando não sabemos exatamente quantas vezes a repetição ocorrerá (ex: esperar uma entrada específica do usuário).
2. **`for`**: Itera sobre uma sequência definida (lista, string, range). Ideal para contagens ou percorrer coleções.
3. **`range(start, stop, step)`**: Função essencial para o `for`. Gera uma sequência de números.
    * Por padrão, começa em 0 e pula de 1 em 1.
4. **Autoatribuição:** Operadores como `+=`, `-=`, `*=`, `/=` são usados dentro de loops para atualizar contadores ou acumuladores.

## EXEMPLO PRÁTICO

```python
# Loop While (Controle manual)
contador = 5
while contador > 0:
    print(f"Contagem regressiva: {contador}")
    contador -= 1

# Loop For com Range
# Do 1 ao 10, de 2 em 2
for i in range(1, 11, 2):
    print(f"Número ímpar: {i}")

# Percorrendo uma String
for letra in "Python":
    print(letra.upper())
```
