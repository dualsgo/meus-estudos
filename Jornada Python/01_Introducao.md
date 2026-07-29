# Introdução à Programação com Python

## EXPLICAÇÃO

Programar é fundamentalmente um exercício de **comunicação**. Instruímos o computador a realizar tarefas através de **algoritmos**, que são sequências finitas de passos bem definidos. No Python, a clareza e legibilidade são essenciais, seguindo o mantra: *"Código é lido muito mais vezes do que é escrito"*.

Os pilares da qualidade em Python (PEP 8) são:
* **Legibilidade:** O código deve ser natural e expressiva.
* **Eficiência:** Resolver problemas sem desperdício de recursos.
* **Manutenibilidade:** Código organizado que facilita evolução e correções.

A estrutura do código baseia-se em:
1. **Sequência:** Execução de cima para baixo.
2. **Decisão:** Uso de condicionais (`if`, `elif`, `else`) com foco na **Indentação**.
3. **Repetição:** Loops (`for`, `while`) para iterar sobre coleções ou repetir blocos.

Python é uma linguagem de alto nível e **interpretada**, com uma sintaxe limpa que obriga a organização através de espaços em branco (indentação).

## EXEMPLO PRÁTICO

```python
# Seu primeiro programa: Hello World
print("Hello, World!")

# Exemplo de erro de sintaxe vs semântica
# Erro de Sintaxe (Ponto onde não deveria): print(1.000.000) -> Gera SyntaxError
# Erro Semântico (Vírgula em vez de separador): print(1,000,000) -> Exibe 1 0 0

# Forma correta de legibilidade para números grandes:
print(1_000_000) # O underscore é ignorado pelo interpretador mas ajuda o humano
```
