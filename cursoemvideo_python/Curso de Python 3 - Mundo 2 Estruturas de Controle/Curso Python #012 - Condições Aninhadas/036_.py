s = 100000.  # Saldo devedor inicial
entrada = 0  # Valor da entrada inicial (se houver)
n = 100  # Número total de parcelas
m = 0  # Número de parcelas já pagas
taxa_juros_anual = 0.08  # Taxa de juros anual (8% ao ano)

# Convertendo a taxa de juros anual para mensal
taxa_juros_mensal = taxa_juros_anual / 12

# Se houver uma entrada, subtraí-la do saldo devedor inicial
s -= entrada
juros = taxa_juros_mensal

for i in range(1, n+1):
    p = (taxa_juros_mensal * s) / (1 - (1 + taxa_juros_mensal)**(-n))
    m += 1
    amortizacao = p - juros
    juros = s * taxa_juros_mensal
    print(f'Parcela {i}: R$ {p:.2f} (Amortização: R$ {amortizacao:.2f}, Juros: R$ {juros:.2f}, Saldo Devedor: R$ {s:.2f})')
    s -= p