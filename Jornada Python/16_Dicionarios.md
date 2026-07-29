# Dicionários em Python

## EXPLICAÇÃO

Dicionários são coleções mutáveis que armazenam dados no formato **Chave: Valor**. Ao contrário das listas, o acesso não é por índice numérico, mas sim por uma chave única (geralmente uma string).

1. **Sintaxe**: Usa-se chaves `{}` e o separador `:`.
   * Ex: `aluno = {"nome": "Maria", "idade": 22}`
2. **Acesso Seguro**:
   * `dict[chave]`: Pode causar erro se a chave não existir.
   * `.get(chave, valor_padrao)`: Retorna o valor ou um padrão caso não encontre, sem travar o programa.
3. **Manipulação**:
   * Adicionar/Atualizar: `dict[nova_chave] = valor`
   * Remover: `del dict[chave]` ou `.pop(chave)`
4. **Iteração**:
   * `.keys()`: Apenas chaves.
   * `.values()`: Apenas valores.
   * `.items()`: Pares (chave, valor).

## EXEMPLO PRÁTICO

```python
pessoa = {
    "nome": "Douglas",
    "idade": 30,
    "cidade": "São Paulo"
}

# Adicionando e atualizando
pessoa["profissao"] = "Programador"
pessoa["idade"] = 31

# Acesso seguro
print(pessoa.get("email", "Não informado"))

# Loops em dicionários
print("\n--- Dados Cadastrais ---")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")

# Dicionário dentro de lista (Estrutura comum de APIs)
usuarios = [
    {"id": 1, "login": "admin"},
    {"id": 2, "login": "guest"}
]
print(f"\nPrimeiro usuário: {usuarios[0]['login']}")
```
