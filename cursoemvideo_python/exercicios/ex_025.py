# Passo 1: Ler o nome da pessoa
nome = str(input('Digite o nome da pessoa: ')).strip()

# Passo 2: Verificar se 'SILVA' está no nome (ignorando maiúsculas/minúsculas)
tem_silva = 'SILVA' in nome.upper()

# Passo 3: Exibir o resultado
if tem_silva:
    print('Sim, o nome contém "SILVA".')
else:
    print('Não, o nome não contém "SILVA".')

