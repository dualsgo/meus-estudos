# Variáveis em Python

## EXPLICAÇÃO

Variáveis são "recipientes" ou "etiquetas" que usamos para acessar locais na memória do computador onde valores estão armazenados. Elas permitem que o código seja flexível e reutilizável.

Componentes de uma variável:
1. **Nome:** Identificador (deve começar com letra ou sublinhado).
2. **Operador de Atribuição (`=`):** Associa o nome ao valor.
3. **Valor:** O conteúdo armazenado (número, texto, etc.).

Python possui **tipagem dinâmica**, o que significa que você não precisa declarar o tipo; o interpretador infere o tipo pelo valor atribuído. Variáveis são **mutáveis**, podendo ter seu valor e tipo alterados ao longo do script.

**Constantes:** Por convenção, variáveis que não devem mudar são escritas em MAIÚSCULAS (ex: `PI = 3.14`), embora o Python não impeça tecnicamente sua alteração.

## EXEMPLO PRÁTICO

```python
# Atribuição Simples
nome_usuario = "Carlos"
print("Seja bem-vindo, " + nome_usuario + "!") 

# Reatribuição (Mudança de valor)
nome_usuario = "Luiza"
print("Seja bem-vindo, " + nome_usuario + "!")

# Tipagem Dinâmica
caixa = 10       # Tipo int
caixa = "Texto"  # Agora é str

# Convenção de Constantes
PI = 3.14159
print(PI)

# Snake Case (Recomendado)
saldo_conta = 1000.0
```
