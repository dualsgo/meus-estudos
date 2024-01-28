# 4.3.5 LAB Quantos dias: escrevendo e usando suas próprias funções

# Sua tarefa é escrever e testar uma função que usa dois argumentos (um ano e um mês) e retorna o número de dias para o determinado par de ano-mês (embora apenas fevereiro seja sensível ao valor do year, sua função deve ser universal).

def is_year_leap(year):  # define a função is_year_leap com o parâmetro year
    
    if year % 4 == 0 or (year % 400 == 0 and year % 100 != 0):  # se o ano for divisível por 4 ou (se o ano for divisível por 400 e não for divisível por 100)
        return True  # retorna True
    else:  # caso contrário
        return False  # retorna False


def days_in_month(year, month): # define a função days_in_month com os parâmetros year e month

    if is_year_leap(year):  # se o ano for bissexto
        
        if month == 2:  # se o mês for fevereiro
            return 29  # retorna 29 (fevereiro tem 29 dias em anos bissextos)
        else:  # caso contrário
            if month in (1, 3, 5, 7, 8, 10, 12):  # se o mês for janeiro, março, maio, julho, agosto, outubro ou dezembro
                return 31  # retorna 31 (esses meses tem 31 dias)
            elif month in (4, 5, 9, 11):  # se o mês for abril, junho, setembro ou novembro
                return 30  # retorna 30 (esses meses tem 30 dias)
            
    else: # caso o ano não seja bissexto
        
        if month == 2:  # se o mês for fevereiro
            return 28  # retorna 28 (fevereiro tem 28 dias em anos não bissextos)
        else:
            if month in (1, 3, 5, 7, 8, 10, 12):
                return 31
            elif month in (4, 5, 9, 11):
                return 30


resposta = days_in_month(int(input('Digite o ano: ')), int(input('Digite o mês: ')))  # chama a função days_in_month e atribui o retorno a variável resposta (quantidade de dias do mês do ano digitado) - os valores digitados são convertidos para inteiro e verificados pela função

print(f'O mês do ano digitado possui {resposta} dias')