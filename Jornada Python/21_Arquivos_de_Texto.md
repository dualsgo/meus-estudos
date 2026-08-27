# Manipulação de Arquivos

## EXPLICAÇÃO

Guardar informações permanentemente em arquivos de texto (`.txt`) é essencial para que os dados não sumam ao fechar o programa.

1. **Gerenciador de Contexto (`with`)**: A melhor prática. Garante que o arquivo seja fechado automaticamente, mesmo se houver erro.
2. **Modos de Abertura**:
   * `'r'` (Read): Leitura (padrão). Erro se o arquivo não existir.
   * `'w'` (Write): Escrita. **Apaga** o conteúdo anterior e cria um novo.
   * `'a'` (Append): Adicionar. Escreve no final do arquivo sem apagar o que já existe.
3. **`encoding='utf-8'`**: Protege o arquivo para suportar acentos da língua portuguesa.

## EXEMPLO PRÁTICO

```python
# 1. Escrevendo (ou criando) um arquivo
with open('notas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Douglas: 10\n')
    arquivo.write('Ana: 9.5\n')

# 2. Adicionando conteúdo sem apagar
with open('notas.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Beto: 8.0\n')

# 3. Lendo o conteúdo
print("--- Lendo o Arquivo ---")
with open('notas.txt', 'r', encoding='utf-8') as arquivo:
    # Opção A: Ler tudo de uma vez
    # conteudo = arquivo.read()
    
    # Opção B: Linha por linha (Melhor para arquivos grandes)
    for linha in arquivo:
        print(linha.strip()) # strip() remove o \n extra

# 4. Verificando se existe (Precisa importar os)
import os
if os.path.exists('notas.txt'):
    print("\nO arquivo existe no sistema.")
```
