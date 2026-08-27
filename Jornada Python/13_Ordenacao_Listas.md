# Ordenando Listas: Bubble Sort e .sort()

## EXPLICAÇÃO

Organizar dados é fundamental. Existem algoritmos manuais (pedagógicos) e métodos nativos (eficientes).

1. **Bubble Sort**: Algoritmo simples onde os maiores valores "flutuam" para o final através de comparações e trocas sucessivas entre elementos adjacentes. É didático, mas pouco eficiente para grandes volumes (O(n²)).
2. **Métodos Nativos (Timsort)**:
   * **`.sort()`**: Altera a lista original permanentemente. Não retorna valor (`None`).
   * **`sorted(lista)`**: Retorna uma **nova** lista ordenada, mantendo a original intacta.
3. **Parâmetro `reverse`**: Ambos aceitam `reverse=True` para ordenação decrescente.
4. **Extremos e Soma**:
   * `max(lista)` / `min(lista)`: Encontra o maior/menor valor.
   * `sum(lista)`: Soma todos os elementos numéricos.

## EXEMPLO PRÁTICO

```python
precos = [45.9, 10.5, 99.0, 5.0]

# Ordenação Nativa
precos.sort() # Permanente: [5.0, 10.5, 45.9, 99.0]
print(f"Ordenada: {precos}")

# Ordenação Decrescente (Nova lista)
decrescente = sorted(precos, reverse=True)
print(f"Decrescente: {decrescente}")

# Análise Básica
print(f"Mais barato: {min(precos)}")
print(f"Total: {sum(precos)}")

# Lógica Simplificada do Bubble Sort
lista = [5, 2, 9, 1]
for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
print(f"Bubble Sort: {lista}")
```
