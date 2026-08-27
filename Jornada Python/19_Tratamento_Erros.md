# Tratamento de Erros e Exceções

## EXPLICAÇÃO

Mesmo o melhor código pode falhar (falta de internet, arquivo inexistente, entrada inválida do usuário). O tratamento de erros evita que o programa "quebre" bruscamente.

1. **`try`**: Bloco onde colocamos o código "perigoso" que pode falhar.
2. **`except`**: Bloco executado se ocorrer um erro. Podemos capturar erros específicos (ex: `ZeroDivisionError`).
3. **`else`**: Executado apenas se **não** houver erro no `try`.
4. **`finally`**: Executado **sempre**, com ou sem erro (usado para fechar arquivos/conexões).
5. **`raise`**: Usado para forçar a ocorrência de um erro personalizado.

## EXEMPLO PRÁTICO

```python
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero!"
    except TypeError:
        return "Erro: Digite apenas números!"
    else:
        return f"Sucesso! Resultado: {resultado}"
    finally:
        print("Operação finalizada.")

# Testes
print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, "5"))

# Raise Personalizado
idade = -5
if idade < 0:
    # raise ValueError("A idade não pode ser negativa!")
    print("Simulação de Raise: Erro disparado!")
```
