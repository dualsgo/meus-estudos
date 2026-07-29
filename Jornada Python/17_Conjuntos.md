# Conjuntos (Sets) em Python

## EXPLICAÇÃO

Conjuntos são coleções não ordenadas de elementos **únicos**. São ideais para remover duplicatas de uma lista ou realizar operações matemáticas de conjuntos (união, intersecção, etc).

1. **Sintaxe**: Criados com chaves `{}` ou a função `set()`.
   * **Atenção**: `{}` vazio cria um dicionário. Use `set()` para um conjunto vazio.
2. **Características**:
   * Não permitem duplicatas.
   * Não possuem ordem (não aceitam índices `s[0]`).
   * São mutáveis (podemos adicionar/remover itens).
3. **Operações Principais**:
   * **União (`|` ou `.union`)**: Tudo que há nos dois.
   * **Intersecção (`&` ou `.intersection`)**: Apenas o que há em comum.
   * **Diferença (`-` ou `.difference`)**: O que há no primeiro mas não no segundo.

## EXEMPLO PRÁTICO

```python
# Removendo duplicatas de uma lista
numeros_sujos = [1, 2, 2, 3, 4, 4, 4, 5]
numeros_limpos = set(numeros_sujos)
print(f"Sem repetidos: {numeros_limpos}") # {1, 2, 3, 4, 5}

# Operações Matemáticas
time_a = {"Ana", "Beto", "Caio"}
time_b = {"Caio", "Duda", "Eva"}

print(f"União: {time_a | time_b}")        # Todos os nomes
print(f"Intersecção: {time_a & time_b}")  # Quem está nos dois (Caio)
print(f"Diferença A-B: {time_a - time_b}") # Quem é só do A

# Conjunto imutável
congelado = frozenset([1, 2, 3])
# congelado.add(4) # Erro!
```
