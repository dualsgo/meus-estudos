# Tuplas em Python

## EXPLICAÇÃO

Tuplas são coleções de elementos imutáveis. Uma vez criada, você não pode alterar, adicionar ou remover seus itens. São comumente usadas para dados que não devem mudar (como coordenadas ou configurações).

1. **Sintaxe**: Definidas por parênteses `()` e vírgulas.
   * Ex: `ponto = (10, 20)`
2. **Imutabilidade**: Diferente das listas, tuplas não possuem métodos como `.append()` ou `.pop()`. Se tentar alterar um índice (`t[0] = 1`), o Python retornará um `TypeError`.
3. **Tupla unitária**: Para criar uma tupla com apenas um elemento, é obrigatório colocar uma vírgula no final.
   * Ex: `unica = (5,)`
4. **Desempacotamento (*Unpacking*)**: Permite atribuir os valores da tupla diretamente a variáveis.
   * Ex: `x, y = ponto`
5. **Vantagens**: São mais leves na memória e mais rápidas que as listas.

## EXEMPLO PRÁTICO

```python
# Criação e Acesso
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])  # Suco

# Desempacotamento com asterisco (Pega o primeiro e o resto vira lista)
primeiro, *resto = lanche
print(f"Primeiro: {primeiro}")
print(f"Resto: {resto}")

# Métodos disponíveis (Apenas leitura/busca)
print(f"Quantas pizzas? {lanche.count('Pizza')}")
print(f"Onde está o Suco? Índice {lanche.index('Suco')}")

# Tuplas em Funções (Retorno múltiplo)
def dimensões():
    return 1920, 1080

largura, altura = dimensões()
print(f"Resolução: {largura}x{altura}")
```
