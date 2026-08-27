# Integração: Funções, Loops e Listas

## EXPLICAÇÃO

A verdadeira força do Python aparece quando combinamos as estruturas básicas para resolver problemas reais.

1. **Listas como Argumentos**: Podemos passar listas inteiras para funções para processamento em massa.
2. **Processamento em Loops**: Funções que iteram sobre listas recebidas para aplicar lógica a cada elemento (ex: calcular descontos, filtrar usuários).
3. **Eficiência com Geradores (`Expressions`)**: Para volumes massivos de dados, usamos geradores entre parênteses `(for...)` em vez de listas `[...]`. Eles economizam memória processando um item por vez sob demanda.

## EXEMPLO PRÁTICO

```python
# Função que processa uma lista (Aplica 10% de desconto)
def aplicar_desconto(precos):
    precos_novos = []
    for p in precos:
        precos_novos.append(round(p * 0.9, 2))
    return precos_novos

carrinho = [100.0, 50.0, 25.0]
print(f"Preços com desconto: {aplicar_desconto(carrinho)}")

# Mesmo exemplo usando List Comprehension dentro da função
def aplicar_desconto_v2(precos):
    return [round(p * 0.9, 2) for p in precos]

# Exemplo de Gerador (Lazy Evaluation)
# Promete calcular, mas só o faz quando percorrido
gerador = (x**2 for x in range(1000000)) 
print(next(gerador)) # 0
print(next(gerador)) # 1
```
