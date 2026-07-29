# Listas: Fundamentos e Manipulação

## EXPLICAÇÃO

Listas são coleções ordenadas e mutáveis de elementos. São uma das estruturas de dados mais versáteis do Python.

1. **Criação e Acesso**:
   * Criadas com colchetes `[]`.
   * **Índices**: Começam em `0`. Índices negativos (ex: `-1`) acessam do fim para o começo.
2. **Adição de Elementos**:
   * `.append(valor)`: Adiciona ao final.
   * `.insert(índice, valor)`: Adiciona em uma posição específica, deslocando os outros.
3. **Remoção de Elementos**:
   * `del lista[índice]`: Remove por posição.
   * `.pop(índice)`: Remove e **retorna** o elemento (padrão é o último).
   * `.remove(valor)`: Remove a primeira ocorrência do **valor** especificado.
   * `.clear()`: Limpa a lista toda.
4. **Outras Funções**:
   * `len(lista)`: Tamanho da lista.
   * `valor in lista`: Verifica se o valor existe na lista (retorna True/False).

## EXEMPLO PRÁTICO

```python
frutas = ["Maçã", "Banana", "Laranja"]

# Adicionando
frutas.append("Uva")
frutas.insert(1, "Morango") # Inserido no índice 1

# Removendo
ultimo = frutas.pop()
print(f"Removido: {ultimo}") # Uva
frutas.remove("Banana")

# Consultando
print(f"Lista atual: {frutas}")
print(f"Tamanho: {len(frutas)}")
print("Maçã" in frutas) # True
```
