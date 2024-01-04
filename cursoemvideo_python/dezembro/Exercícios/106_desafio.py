# Exercício Python #106 - Sistema interativo de ajuda em Python - Aula 00 até 21 - Mundo 3
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
comando = str(input('\033[1;34mSOBRE O QUE GOSTARIA DE LER? \033[m')).strip().lower()
def ajuda(comando):
    while True:
        print('\033[7;37;40m', end='')
        print(help(comando))
        print('\033[m')
        continuar = str(input('\033[1;33mVER OUTRA DOCUMENTAÇÃO? S/N\033[m')).strip().upper()
        while continuar not in 'SN':
            continuar = str(input('\033[1;31mESSE COMANDO É INVÁLIDO. DIGITE S OU N\033[m')).strip().upper()
        if continuar in 'N':
            print('\033[1;31mOK, FINALIZANDO O PROGRAMA\033[m')
            break
        else:
            print('\033[1;32mCERTO! VAMOS EM FRENTE.\033[m')
            comando = str(input('\033[1;34mSOBRE O QUE DESEJA SABER?  \033[m')).strip().lower()


ajuda(comando)