# 4.3.6 LAB Dia do ano: escrevendo e usando funções

# Sua tarefa é escrever e testar uma função que usa três argumentos (um ano, um mês e um dia do mês) e retorna o dia correspondente do ano ou retorna None se algum dos argumentos for inválido.

import datetime


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

def day_of_year(year, month, day):
    if year < 1 or 1 > month > 12 or day < 1 or day > days_in_month(year, month):  # verifica se o ano é menor que 1 ou se o mês é menor que 1 ou maior que 12 ou se o dia é menor que 1 ou maior que a quantidade de dias do mês
        return "Data inválida"

    date_object = datetime.date(year, month, day)  # cria um objeto date com os valores passados como parâmetro
    day_of_week = date_object.strftime("%A")  # Obtém o dia da semana em formato de string

    return day_of_week



# Argumentos para teste:
print(day_of_year(2000, 12, 31))