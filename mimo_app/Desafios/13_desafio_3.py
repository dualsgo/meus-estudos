# MIMO - 13 - Módulos e Bibliotecas - Desafio 3

# Como gerente do clube de basquete, Kugo tabula e analisa o desempenho do clube. Kugo descobre que statistics são muito longas para serem digitadas e quer simplificá-las para apenas s , mas esqueceu de renomear o módulo quando o importou. Ajude Kugo a renomear sua importação para s .

import statistics as s

scores = [87, 76, 75, 65, 54, 50, 43, 23, 56, 68, 97]
print(f'The highest score the team scored was {max(scores)}')
print(f'The lowest score the team scored was {min(scores)}')
print(f'The average score the team scored was {s.mean(scores)}')
print(f'The median score the team scored was {s.median(scores)}')