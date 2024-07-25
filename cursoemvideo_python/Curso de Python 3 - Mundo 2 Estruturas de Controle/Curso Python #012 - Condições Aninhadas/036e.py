# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

def obter_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Valor inválido para essa operação. Digite novamente.')


def verificação(v, s, p):
    parcela = v / p
    parcela_máxima = s * .3
    consulta = True if parcela <= parcela_máxima else False

    print(
        f'{'Valor do imóvel:':<20}{f'R$ {v:.2f}':>15}\n'
        f'{'Salário:':<20}{f'R$ {s:.2f}':>15}\n'
        f'{'Prazo em anos:':<20}{f'{p/12:.1g} anos':>15}\n'
        f'{'-' * 35}\n'
        f'{'Parcelas:':<20}{prazo:>15}\n'
        f'{'Parcela máxima:':<20}{f'R$ {parcela_máxima:.2f}':>15}\n'
        f'{'Parcela simulada:':<20}{f'R$ {parcela:.2f}':>15}\n'
        f'{'-' * 35}\n'
        f'{'Resultado:':<20}{'APROVADO' if consulta else 'NEGADO':>15}\n')


valor_casa = obter_valor('Digite o valor da casa: R$ ')
salário = obter_valor('Digite o valor do salário: R$ ')
prazo = int(obter_valor('Prazo em anos: ')) * 12
verificação(valor_casa, salário, prazo)