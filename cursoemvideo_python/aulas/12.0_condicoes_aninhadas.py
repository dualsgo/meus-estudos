# Curso Python Aula 13 - Condições aninhadas

"""RESUMO"""
# O professor inicia a segunda parte do curso de Python, focando nos conceitos de estruturas de controle.

# Introdução à ideia de declarações condicionais alinhadas, que envolvem a colocação de condições em uma estrutura maior.

# Explicação de que, à medida que a complexidade de um problema aumenta, podem surgir mais opções, tornando inútil a ideia de condições alinhadas com mais de duas opções em Python.

# Lembrete sobre a disponibilidade de uma playlist da primeira parte do curso no canal do YouTube e a possibilidade de obter um certificado após a conclusão do curso.

# Introdução à importância das estruturas condicionais na programação, mencionando o alinhamento de várias condições.

# Discussão sobre como condições podem ser aninhadas e os desafios de aninhar várias condições.

# Uso de um exemplo envolvendo escolher um caminho em uma viagem de carro para explicar o conceito de "else" ou condições não alinhadas na programação.

# Conclusão com a descrição do padrão básico de condições aninhadas na programação.

# Introdução ao conceito de alinhamento condicional e sua aplicação em estruturas de controle em programação.

# Explicação do termo "ninho condicional" e seu uso na comparação de variáveis em programação.

# Uso de uma metáfora musical para enfatizar a complexidade da aninhamento condicional e encorajar a prática por meio de desafios estáticos.

# Descrição do primeiro desafio, que envolve o uso de alinhamento condicional para determinar se uma pessoa pode comprar uma casa usando um empréstimo bancário.

# O desafio requer cálculos envolvendo o valor da casa, o salário da pessoa e o prazo de pagamento ao banco.

# Explicação da importância da prática prática na aprendizagem da programação e da necessidade de colocar a teoria em ação.

# Ênfase na ideia de que somente através da ação e experimentação os conceitos de programação podem ser efetivamente aprendidos e aplicados.

# Incentivo aos alunos a se envolverem totalmente com o material do curso, realizando os desafios propostos e colocando suas habilidades de programação à prova.

# Aviso contra o hábito de apenas assistir ao curso sem participar ativamente, enfatizando que isso não levará a resultados tangíveis na aprendizagem e domínio do assunto.

# Encorajamento aos alunos a verem o curso como uma oportunidade de aprimorar suas habilidades e adquirir aplicações do mundo real.

# Lembrete de que as recompensas de seus esforços, como obter um certificado ou conseguir um emprego, dependem de sua diligência, perseverança e disposição para se envolver em exercícios práticos.

"""CONTEÚDO"""

# Condições aninhadas - Oferecem possibilidades extras
# elif (senão se) - Se a primeira condição não for atendida, elif recebe outra possibilidade

# Exemplo 1: Verificando o valor de 'numero'
numero = 2
if numero == 1:
    print('Se for 1')
elif numero == 0:
    print('Se for zero')
else:
    print('Se for qualquer outro número')

# Exemplo 2: Verificando o nome inserido pelo usuário
nome = input('Digite um nome: ').strip()
# Se o nome for 'Gustavo', atenderá a primeira condição. Se não, a próxima será verificada.
if nome == 'Gustavo':
    print('Que nome bonito!')
# Se o nome for 'Maria', 'Pedro' ou 'Paulo', atenderá a condição, senão irá verificar a próxima.
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
# Se o nome for 'Ana', 'José', 'Rafael' ou 'Matheus'.
elif nome in 'Ana José Rafael Matheus':
    print('Seu nome é comum.')
# Se for qualquer outro nome...
else:
    print('SEU NOME NÃO ESTÁ NA LISTA')
# Esta última instrução está fora da estrutura condicional, portanto sempre será executada.
print(f'Tenha um bom dia, {nome}.')
