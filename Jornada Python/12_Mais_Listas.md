# Listas Avançadas: Slicing e Comprehension

## EXPLICAÇÃO

Técnicas avançadas para manipular listas de forma eficiente e elegante.

1. **Fatiamento (*Slicing*)**: `lista[início:fim:passo]`
   * Permite extrair partes da lista ou criar cópias completas (`[:]`).
   * O índice `fim` não é incluído.
2. **Cópia vs. Referência**:
   * `lista_b = lista_a` cria uma **referência** (alterar uma afeta a outra).
   * `lista_b = lista_a[:]` ou `lista_a.copy()` cria uma **cópia independente**.
3. **List Comprehension**: Forma concisa de criar listas.
   * Sintaxe: `[expressão for item in iterável if condição]`
4. **Listas Multidimensionais**: Listas dentro de listas (matrizes).
   * Acesso: `matriz[linha][coluna]`.

## EXEMPLO PRÁTICO

```python
numeros = [0, 10, 20, 30, 40, 50]

# Slicing
print(numeros[1:4])  # [10, 20, 30]
print(numeros[::-1]) # Inverte a lista

# List Comprehension (Números pares ao quadrado)
pares_quadrado = [x**2 for x in range(10) if x % 2 == 0]
print(pares_quadrado) # [0, 4, 16, 36, 64]

# Matriz (Tabuleiro 3x3)
tabuleiro = [[0 for i in range(3)] for j in range(3)]
tabuleiro[1][1] = "X" # Centro do tabuleiro
print(tabuleiro)
```
