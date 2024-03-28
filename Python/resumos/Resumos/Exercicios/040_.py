from time import sleep

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
dias_frequentados = int(input(f'{'\033[1;31m'}Quantos dias frequentou a escola:{'\033[m'} '))

# faz a média das notas
media_nota = (nota1 + nota2) / 2

# valida se o aluno teve uma frequência escolar de mais de 50 dias.
# caso a frequência seja menor que 50 dias, aluno será reprovado
if dias_frequentados >= 50:
    if media_nota < 5: # Condição quando a média do aluno é menor que 5 pontos
        print('\nInfelizmente você foi reprovado, sua nota\n'
              f'foi {media_nota:.2f}')
    elif 5 <= media_nota <= 6.9: # Valida se o aluno teve nota entre 5 e 6.9.
        print(f'\nInfelizmente a sua nota foi {media_nota:.2f} e nesse caso,\n'
              f'será necessário fazer a recuperação.\n')

        validar_repeteco = int(input('Digite 1 para agendar ou 2 para sair: ')) # Confirmando com o aluno.

        print(f'\n{'\033[1;31m'}VALIDANDO INFORMAÇÕES...{'\033[m'}')
        sleep(1) # dellay de 1 segundo

        if validar_repeteco == 1: # se o aluno escolheu agendar a recuperação, cai nessa condição.
            print(f'\nProva agendada para o dia 17, a prova será composta\n'
                  'de 10 questões e cada questão valerá 1 ponto, deverá\n'
                  'tirar uma media de 7 para ser aprovado.')

            sleep(2) # dellay de 2 segundo
            print(f'\n{'\033[1;31m'}Dois mil anos depois...{'\033[m'}')

            sleep(1) # dellay de 1 segundo
            print('\nDia da prova.')

            acertos = int(input('Digite quantas questões acertou das 10: ')) # aqui pergunto quantas quantas
            # questões o aluno acertou.

            print(f'\n{'\033[1;31m'}PROCESSANDO INFORMAÇÃO...{'\033[m'}')
            sleep(1) # dellay de 1 segundo

            # Valida se o aluno acertou 7 ou mais de 7 pontos na prova da recuperação.
            if acertos >= 7:
                print(f'\nParabéns, você foi aprovado, sua nota foi {acertos}')
            else: # Caso ele tenha acertado menos que 7 pontos, será reprovado e cairá nessa condição.
                print(f'\nInfelizmente, você foi reprovado, sua nota foi {acertos}')
        else: # essa condição só será executada caso o aluno selecione a opção 2 para não
              # agendar a prova da recuperação. Na verdade, caso ele escolha qualquer opção
              # diferente de 1, já cai nessa condição.
            print('Tudo bem, lembrando que deverá voltar\n'
                  'antes do dia 13 para agendar a sua recuperação ')

    elif media_nota >= 7: # se a nota do aluno for 7 ou maior que 7, entrará nessa condição.
        print(f'\nParabéns, você foi aprovado com exíto, sua nota foi {media_nota:.2f}.')

else: # Caso o aluno tenha uma frequência menor que 50 dias, será reprovado sem as validações das notas
    print('\nInfelizmente, você foi reprovado, sua frequência escolar\n'
          'foi menor que 50 dias de aula.')