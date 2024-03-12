# 4.3.4 LAB Um ano bissexto: escrevendo suas próprias funções

# Sua tarefa é escrever e testar uma função que usa um argumento (um ano) e retorna True se o ano for um ano bissexto ou False caso contrário.

def is_year_leap(year):  # define a função is_year_leap com o parâmetro year
    
    if year % 4 == 0 or (year % 400 == 0 and year % 100 != 0):  # se o ano for divisível por 4 ou (se o ano for divisível por 400 e não for divisível por 100)
        return True  # retorna True
    else:  # caso contrário
        return False  # retorna False


ano = is_year_leap(int(input('Digite o ano: '))) # chama a função is_year_leap e atribui o retorno a variável ano (True ou False) - o valor digitado é convertido para inteiro e verificado se é bissexto pela função

if ano:  # se ano for True
    print(f'O ano digitado é bissexto')
else:  # caso contrário
    print('O ano digitado não é bissexto')