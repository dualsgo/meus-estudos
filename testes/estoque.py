import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Abre uma janela para o usuário selecionar o diretório onde a pasta será criada
Tk().withdraw()  # Esconde a janela principal do Tkinter
directory = askdirectory(title="Selecione o diretório onde deseja salvar a pasta 'cursoemvideo'")

# Cria o caminho completo para a pasta 'cursoemvideo'
folder_name = os.path.join(directory, 'cursoemvideo')
os.makedirs(folder_name, exist_ok=True)

# Gera 115 arquivos de exercícios
for i in range(1, 116):
	file_name = f'ex{i:03d}.py'
	file_path = os.path.join(folder_name, file_name)

	with open(file_path, 'w') as file:
		file.write(f'# Curso em Video Python - Exercicio {i:03d}\n')

print(f'115 arquivos criados na pasta "{folder_name}".')