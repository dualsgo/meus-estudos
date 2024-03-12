# Automatizando Planilhas com Python
# Introdução
# Este ebook aborda um projeto de automação de planilhas utilizando a linguagem de programação Python. O objetivo é apresentar na prática como Python pode ser utilizado para automatizar informações em planilhas, seguindo um caso real de negócio.

# erão abordados conceitos introdutórios sobre Python, instalação e configuração do ambiente, importação de dados com a biblioteca Pandas, manipulação de dados, criação de tabelas dinâmicas (Pivot Tables), geração de gráficos, totalização de dados e envio automatizado por e-mail.

# Estudo de Caso
# Foi apresentado o seguinte caso: a empresa fictícia XY Corporation, que atua como revendedora de automóveis de luxo com sede em São Paulo, iniciou suas operações no Brasil em 2012.

# O novo CEO da empresa solicitou a apresentação dos resultados da equipe de vendas para conhecer o desempenho dos últimos anos. Ele deseja saber, especificamente, como foram as vendas dos diferentes fabricantes a cada ano.

# Para isso, será necessário:

# Gerar uma tabela Pivot em Python com as colunas: Fabricante, Preço Venda e Ano (sendo Ano o índice);
# Importar a tabela Pivot gerada e criar um gráfico de barras com o total de vendas por fabricante ao longo dos anos;
# Adicionar uma fórmula para totalizar vendas por fabricante;
# Enviar a planilha final por e-mail como anexo para o CEO.
# A empresa fornecerá uma planilha Excel com os dados históricos de vendas coletados do sistema CRM. Esta planilha possui as seguintes colunas:

# Data Nota Fiscal
# Fabricante
# Estado
# Preço Venda
# Preço Custo
# Total Desconto
# Custo Entrega
# Custo Mão de Obra
# Nome Cliente
# Modelo
# Ano
# O projeto será desenvolvido utilizando Python para automatizar as informações solicitadas pelo CEO a partir desta base de dados.

# Instalando e Configurando o Python
# O primeiro passo é instalar o interpretador Python. Existem várias opções, como o próprio interpretador, a distribuição Anaconda ou até mesmo um interpretador online.

# Neste projeto, para permitir a automação no computador local, será utilizada a instalação padrão do Python disponível em python.org.

# Durante a instalação, é muito importante marcar a opção para adicionar o Python ao PATH do sistema. Isso permite que o interpretador seja acessado de qualquer lugar pela linha de comando ou prompt de comando.

# Após concluir a instalação, para validar se o Python está configurado corretamente, basta abrir o prompt de comando e digitar python. Deve aparecer algo similar a:

# Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.>>>
# Isso indica que o interpretador Python foi encontrado na versão instalada (no exemplo, 3.11.1) e está pronto para executar códigos Python.

# Importando Dados com Pandas
# Agora que o Python está configurado, o próximo passo é importar a planilha Excel com os dados de vendas fornecida pela empresa.

# Para facilitar a manipulação dos dados, será utilizada a biblioteca Pandas, uma das mais populares do Python voltada para análise de dados.

# Primeiro, deve-se instalar o Pandas via pip, que é o gerenciador de pacotes do Python:

# pip install pandas
# Em seguida, basta importar a biblioteca:

import pandas as pd
# O "as pd" serve para criar um apelido e simplificar a referência ao Pandas no código.

# Para importar a planilha, utiliza-se a função read_excel() do Pandas:

data = pd.read_excel('data/vendas-carros.xlsx')
# Onde:

# data: variável que armazenará o conjunto de dados importado
# pd: apelido dado ao Pandas
# read_excel(): função do Pandas para ler arquivos Excel
# 'data/vendas-carros.xlsx': caminho para a planilha Excel no sistema de arquivos
# Feito isso, o Pandas já disponibiliza vários métodos para manipular o conjunto de dados armazenado na variável data, como:

# Exibe os 5 primeiros registrosprint(data.head()) # Exibe os 5 últimos registrosprint(data.tail())# Contagem de registros por fabricanteprint(data['Fabricante'].value_counts())
# Estes são apenas alguns exemplos simples de análises que podem ser feitas com Pandas. Nas próximas seções, dados mais avançados serão apresentados.

# Criando a Tabela Pivot
# Conforme apresentado no estudo de caso, o primeiro requisito é gerar uma tabela Pivot contendo Fabricante, Preço Venda e Ano. Para isso, o Pandas possui a função pivot_table().

# Antes de aplicá-la, porém, é interessante reorganizar as colunas do conjunto de dados, deixando apenas as colunas de interesse e já na ordem desejada:

data = data[['Fabricante', 'Preço Venda', 'Ano']]
# Agora sim a tabela Pivot pode ser criada:

tabela_pivot = pd.pivot_table(  data,   values='Preço Venda',   index='Ano',   columns='Fabricante',   aggfunc=sum)
# Analisando:

# data: conjunto de dados sendo utilizado como origem dos dados
# values: coluna que terá seus valores agregados (soma nesse caso)
# index: coluna que será utilizada como índice/linha da tabela
# columns: coluna que será espalhada em colunas na tabela
# aggfunc: função de agregação (soma, média, contagem etc)
# A saída é armazenada na variável tabela_pivot, que contém a tabela Pivot consolidada já no formato desejado.

# Em seguida, basta exportá-la para uma nova planilha Excel:

tabela_pivot.to_excel('tabela_pivot.xlsx', index=True)
# O parâmetro index=True mantém o índice (coluna Ano) na exportação.

# Criando Gráficos com Matplotlib
# Com a tabela Pivot devidamente exportada, o próximo passo é criar um gráfico de barras para visualizar as vendas por fabricante ao longos dos anos.

# Para plotagem de gráficos, será utilizada a biblioteca Matplotlib, outra biblioteca Python muito popular para análise de dados e visualização.

# Novamente, basta instalar com Pip:

# pip install matplotlib
# E importar:

import matplotlib.pyplot as plt
# Em seguida, basta carregar a planilha recém-gerada com a tabela Pivot:

tabela_pivot = pd.read_excel('tabela_pivot.xlsx')
# E utilizar o método .plot() do Pandas, passando alguns parâmetros para definir o tipo de gráfico:

tabela_pivot.plot(kind='bar', figsize=(10, 6))
plt.title('Total Vendas por Fabricante')
plt.ylabel('Faturamento')
plt.show()
# Neste exemplo, definiu-se:

# kind='bar': gráfico de barras
# figsize=(10, 6): tamanho da figura como 10x6 polegadas
# plt.title: título do gráfico
# plt.ylabel: rótulo do eixo y
# plt.show(): exibe o gráfico
# Com isso, um gráfico de barras é gerado com o total de vendas de cada fabricante ao longo dos anos analisados.

# Totalizando Valores com Numpy
# Para deixar a análise mais completa, foi solicitado também a totalização do valor de vendas de cada fabricante.

# # Isso pode ser feito com a biblioteca Numpy, especializada em computação científica e análise de dados.

# Instalando o Numpy:

# pip install numpy  
# Importando:

import numpy as np
# Carregando os dados:

tabela_pivot = pd.read_excel('tabela_pivot.xlsx') 
# E aplicando a função .sum() do Numpy em cada coluna:

total_jaguar = np.sum(tabela_pivot['Jaguar'])
total_aston = np.sum(tabela_pivot['Aston Martin'])
# e assim por diante com os demais fabricantes
# Para finalizar, basta salvar esses dados em uma nova planilha Excel, aplicando formatação como células monetárias.

# O último requisito é automatizar o envio desta planilha consolidada por e-mail para o CEO solicitante.

# Isso pode ser feito com a biblioteca Win32Com Client, que permite acessar aplicativos do Windows via Python, como Outlook, Word, Excel etc.

# Primeiro, instale a biblioteca:

# pip install pypiwin32
# Depois, importe:

# import win32com as win32
# Em seguida, inicie uma sessão com o Outlook:

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
#Configure o e-mail:

mail.To = 'ceo@xycorporation.com'
mail.Subject = 'Relatório de Vendas'
mail.Body = '''Prezado,Segue o relatório de vendas conforme solicitado.Att.,[Seu Nome]'''
# Anexe a planilha:

mail.Attachments.Add('relatorio_vendas.xlsx')
# E envie:

mail.Send()
# Pronto! O e-mail será enviado automaticamente com a planilha em anexo.

# Conclusão
# Neste projeto, foi possível ter uma amostra significativa do poder da linguagem Python para automatizar informações em planilhas, seguindo um caso real de negócio com etapas como importação, transformação, análise e compartilhamento de dados.

# Foram utilizadas bibliotecas amplamente adotadas como Pandas, Matplotlib, Numpy e Win32com para executar tarefas como manipulação de dados, visualização, cálculos e envio automatizado por e-mail.

# Python se mostra uma excelente opção para automação de planilhas, integrando poderosas bibliotecas para análise de dados e customizações limitadas apenas pela lógica aplicada no código. Conforme apresentado, em poucas linhas de código é possível obter resultados expressivos.

# Espero que este material sirva como referência e estímulo para novas automações com este fantástico ecossistema que é a linguagem Python.