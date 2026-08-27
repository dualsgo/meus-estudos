# Funções em Python

## EXPLICAÇÃO

Funções são blocos de código reutilizáveis que executam tarefas específicas. Elas ajudam a organizar o código, evitar repetições e facilitar a manutenção.

1. **Definição (`def`)**: Usa-se a palavra-chave `def` seguida do nome da função e parênteses.
   * Ex: `def minha_funcao():`
2. **Parâmetros vs. Argumentos**:
   * **Parâmetros**: Variáveis definidas na declaração da função (dentro dos parênteses).
   * **Argumentos**: Valores reais passados para a função quando ela é chamada.
3. **Tipos de Argumentos**:
   * **Posicionais**: A ordem importa.
   * **Nomeados (Keywords)**: Especifica-se o nome do parâmetro (ex: `funcao(nome="Ana")`). A ordem não importa.
   * **Padrão (*Default*)**: Define-se um valor no parâmetro caso nenhum argumento seja passado.
4. **Retorno (`return`)**: Envia um valor de volta para quem chamou a função. Se não houver `return`, a função retorna `None`.

## EXEMPLO PRÁTICO

```python
# Função com parâmetro padrão e retorno
def saudar(nome="Visitante"):
    return f"Olá, {nome}!"

# Chamadas diferentes
print(saudar("Douglas"))  # Argumento posicional
print(saudar(nome="Maria")) # Argumento nomeado
print(saudar())             # Usa o valor padrão

# Função com múltiplos retornos (empacotados em tupla)
def operacoes(a, b):
    return a + b, a * b

soma, multi = operacoes(5, 2)
print(f"Soma: {soma}, Multiplicação: {multi}")
```
