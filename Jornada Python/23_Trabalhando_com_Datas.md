# Manipulando Datas e Horas (Datetime)

## EXPLICAÇÃO

O tratamento de datas é um desafio comum (fusos horários, anos bissextos, formatos diferentes). O módulo nativo `datetime` resolve a maioria desses casos.

1. **`datetime.date`**: Trabalha apenas com dia, mês e ano.
2. **`datetime.datetime`**: Inclui horas, minutos e segundos.
3. **`strftime` (String Format Time)**: Converte objeto de data para texto formatado.
4. **`strptime` (String Parse Time)**: Converte texto para objeto de data.
5. **`timedelta`**: Usado para cálculos de tempo (somar ou subtrair dias/horas).

## EXEMPLO PRÁTICO

```python
from datetime import datetime, timedelta

# Data e Hora atual
agora = datetime.now()
print(f"Agora: {agora}")

# Formatação Brasileira (Dia/Mês/Ano)
data_formatada = agora.strftime("%d/%m/%Y %H:%M")
print(f"Formatado: {data_formatada}")

# Criando uma data específica
aniversario = datetime.strptime("25/12/2024", "%d/%m/%Y")
print(f"Natal: {aniversario}")

# Cálculos com datas
amanha = agora + timedelta(days=1)
ontem = agora - timedelta(days=1)
dias_para_natal = aniversario - agora

print(f"Faltam {dias_para_natal.days} dias para o Natal!")
```
