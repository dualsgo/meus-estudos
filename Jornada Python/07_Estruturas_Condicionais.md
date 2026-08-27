# Estruturas de Controle (Condicionais)

## EXPLICAÇÃO

Permitem que o programa tome decisões baseadas em condições lógicas (Booleanos).

1. **`if`**: Executa o bloco se a condição for verdadeira.
2. **`elif`** (*else if*): Verifica uma nova condição caso as anteriores tenham falhado.
3. **`else`**: Executa um "plano B" caso nenhuma das condições anteriores seja atendida.
4. **`match case` (Python 3.10+):** Uma forma elegante de lidar com múltiplas opções para uma mesma variável (semelhante ao *switch* em outras linguagens).
5. **Operador Ternário:** Condicional em uma única linha: `valor_se_true if condicao else valor_se_false`.

**Indentação:** Em Python, o recuo do código (geralmente 4 espaços) define o que pertence a cada bloco. Uma indentação errada causa o `IndentationError`.

## EXEMPLO PRÁTICO

```python
# Exemplo de if/elif/else
nota = 8.5
if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado")
else:
    print("Recuperação")

# Operador Ternário
status = "Maior de idade" if nota >= 18 else "Menor de idade"

# Match Case
opcao = 2
match opcao:
    case 1: print("Perfil")
    case 2: print("Configurações")
    case _: print("Opção Inválida")
```
