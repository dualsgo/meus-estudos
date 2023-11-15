import os

# Diretório onde você deseja criar os arquivos
# Substitua pelo caminho desejado
diretorio = "C:\\Users\\mdbsi\\OneDrive\\Documentos\\GitHub\\meus-estudos\\cursoemvideo_python\\exercicios"

# Loop para criar os arquivos
for i in range(6, 101):
    # Formata o número para ter três dígitos
    numero_formatado = str(i).zfill(3)
    nome_arquivo = f"ex_{numero_formatado}.py"
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)

    # Conteúdo a ser adicionado em cada arquivo
    conteudo = f'Desafio {numero_formatado} - Título (Aula 00 a 00): Descrição.'
    # Cria o arquivo e escreve o conteúdo
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write(conteudo)

print("Arquivos criados com sucesso!")
