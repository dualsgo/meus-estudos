# 2.2.1 Literais - Os dados em sí

# Literais são dados cujos valores são determinados pelo próprio literal. Em outras palavras, um literal representa um valor fixo, não variável. Por exemplo, a string "Olá" é um literal de string, enquanto a variável nome pode ser um literal de string ou um literal numérico, dependendo do valor que ela contém.

# Neste exemplo, você encontrará dois tipos diferentes de literais:
# Uma string, que você já conhece e um número inteiro, algo completamente novo.
print("2")
print(2)

# A função print() os apresenta exatamente da mesma maneira ‒ este exemplo é óbvio, pois sua representação legível por humanos também é a mesma.

# Internamente, na memória do computador, esses dois valores são armazenados de formas completamente diferentes ‒ a string existe apenas como uma string ‒ uma série de letras.
# O número é convertido em representação de máquina (um conjunto de bits). A função print() é capaz de mostrar ambos em um formato legível para humanos.

# 2.2.2 Inteiros

# Os números manipulados pelos computadores podem ser de dois tipos:
# inteiros, ou seja, aqueles desprovidos da parte fracionária (int)
# e números de ponto flutuante (ou simplesmente float), que contêm (ou conseguem conter) a parte fracionária.

# Tomemos, por exemplo, o número onze milhões cento e onze mil cento e onze. Se você pegasse um lápis na mão agora, escreveria o número assim: 11.111.111, ou até mesmo assim: 11 111 111.

# É claro que essa disposição facilita a leitura, especialmente quando o número consiste em muitos dígitos. No entanto, o Python não aceita coisas como essas. É proibido. O que o Python 3.6+ permite, porém, é o uso de sublinhados em literais numéricos.*

# Portanto, você pode escrever este número da seguinte forma: 11111111 ou desta forma: 11_111_111.
# Para números negativos basta colocar o sinal de menos na frente do literal: -11111111 ou -11_111_111.
# Números positivos não carecem de um sinal, mas você pode colocá-lo se quiser: +11111111 ou +11_111_111.

# Números octais e hexadecimais
# Se um número inteiro for precedido por um prefixo 0O ou 0o (zero-o), ele será tratado como um valor octal. Isso significa que o número deve conter dígitos retirados apenas do intervalo 0 a 7.
# 0o123 é um número octal com um valor (decimal) igual a 83.
# A função print() faz a conversão automaticamente.
print(0o123)
print(int('0123', 8))  # 8 é a base do número octal (0123)

# Hexadecimais são números precedidos pelo prefixo 0x ou 0X (zero-x).
# 0x123 é um número hexadecimal com um valor (decimal) igual a 291. A função print() também pode gerenciar esses valores.
print(0x123)

# Podemos converter um número hexadecimal em decimal usando a função int() e especificando a base do número hexadecimal (16) como segundo argumento:
print(int('0x' + '123', 16))  # 16 é a base do número hexadecimal (0x123)

# Assim utilizaremos a função format() para converter um número decimal em octal ou hexadecimal:
print(format(83, 'o'))
# Basta especificar a base como segundo argumento da função format(). 'o' para octal e 'x' para hexadecimal.

# 2.2.3 Floats

# Valores float são aqueles que contêm uma parte fracionária. Eles são escritos com um ponto decimal como separador entre a parte inteira e a parte fracionária. Por exemplo: 2.5 ou -0.4

# Embora se o seu idioma nativo preferir usar vírgula em vez de um ponto no número, você deve garantir que seu número não contenha nenhuma vírgula. O Python não aceitará isso, ou (em casos muito raros, mas possíveis) pode interpretar mal suas intenções, pois a própria vírgula tem seu próprio significado reservado em Python.

# Se você quiser usar apenas um valor de dois e meio, escreva-o como mostrado acima. Observe mais uma vez: há um ponto entre 2 e 5, não uma vírgula.

# Como você provavelmente pode imaginar, o valor de zero ponto quatro poderia ser escrito em Python como 0.4
# Mas não se esqueça desta regra simples - você pode omitir zero quando for o único dígito antes ou depois da vírgula.

# Em essência, você pode escrever o valor 0.4 como .4

# O valor de 4.0 pode ser escrito como 4.
# 4 é um número inteiro, enquanto 4.0 é um número de ponto flutuante.

# Isso não mudará seu tipo nem seu valor de float para int, desde que haja um ponto decimal no literal.

# Por outro lado, não são apenas os pontos que fazem um float. Você também pode usar a letra e.

# A letra e (ou E) é usada para indicar a potência de dez. Por exemplo, para evitar escrever tantos zeros, os livros de física usam uma forma abreviada, que você provavelmente já viu: 3 x 10 ** 8. O Python permite que você escreva o mesmo valor como 3e8. A letra E (você também pode usar a letra minúscula e - vem da palavra expoente) é um registro conciso da frase vezes dez à potência de.

# o expoente (o valor após o E) tem que ser um número inteiro;
# a base (o valor na frente do E) pode ser um número inteiro ou um valor flutuante.

# Codificação de flutuantes
# Vamos ver como essa convenção é usada para registrar números muito pequenos (no sentido de seu valor absoluto, que é próximo de zero).

# Uma constante física chamada constante de Planck (e indicada como h), conforme os livros didáticos, tem o valor de: 6,62607 x 10-34.

# O Python permite que você escreva o mesmo valor como 6.62607e-34.

# O Python sempre escolhe a forma mais econômica de apresentação do número, e você deve levar isso em consideração ao criar literais.
print(0.0000000000000000000001)  # 1e-22

# 2.2.4 Strings

# Strings são usadas quando você precisa processar texto (como nomes de todos os tipos, endereços, romances, etc.), não números. Strings precisam de aspas assim como floats precisam de pontos.

# O Python pode usar um apóstrofo em vez de uma aspa. Qualquer um desses caracteres pode delimitar cadeias de caracteres, mas você deve ser coerente. Se você abrir uma sequência com aspas, será necessário fechá-la com aspas.

print('Eu gosto "Monty Python"')  # Eu gosto "Monty Python"

# Também é possível usar barras invertidas para escapar de aspas numa string. Ou aspas triplas para strings de várias linhas.

# Uma string vazia ainda permanece uma string:
print('')
print("")

# 2.2.5 Valores boolean

# Essas literais não são tão óbvias quanto as anteriores, pois são usadas para representar um valor muito abstrato - a veracidade. O nome vem do matemático George Boole, o primeiro a definir um sistema de álgebra booleana, a base da lógica moderna e da computação que usa apenas dois valores: verdadeiro e falso denotados como 1 e 0, respectivamente.

# Cada vez que você pergunta ao Python se um número é maior que outro, a pergunta resulta na criação de alguns dados específicos - um valor booleano. Você nunca receberá uma resposta como: não sei ou Provavelmente, sim, mas não tenho certeza.

# O Python sempre responderá com um dos dois valores: True ou False.

# Você não pode mudar nada. É necessário aceitar esses símbolos como eles são, inclusive distinção entre maiúsculas e minúsculas.

"""2.2.7 RESUMO DA SEÇÃO
1. Literais são notações para representar alguns valores fixos no código. Python tem vários tipos de literais - por exemplo, um literal pode ser um número (literais numéricos, por exemplo, 123) ou uma string (literais de string, por exemplo, "Eu sou um literal".).

2. O sistema binário é um sistema de números que emprega 2 como base. Portanto, um número binário é composto de 0s e 1s apenas, por exemplo, 1010 é 10 em decimal.

Os sistemas de numeração octal e hexadecimal, da mesma forma, empregam 8 e 16 como suas bases respectivamente. O sistema hexadecimal usa os números decimais e seis letras extras.
3. Inteiros (ou simplesmente ints) são um dos tipos numéricos compatíveis com o Python. São números escritos sem um componente fracionário, por exemplo, 256 ou -1 (números inteiros negativos).

4. Ponto flutuante (ou simplesmente float) são outro dos tipos numéricos compatíveis com o Python. São números que contêm (ou são capazes de conter) um componente fracionário, por exemplo, 1.27.

5. Para codificar um apóstrofo ou uma aspas dentro de uma string, você pode 
usar o caractere de escape, por exemplo, 'I\'m happy.' ou abrir e fechar a string usando um conjunto oposto de símbolos aos que você deseja codificar, por exemplo, "I'm happy." para codificar um apóstrofo e 'Ele disse "Python", não "typhoon"' para codificar uma aspas (dupla).

6. Valores booleanos são os dois objetos constantes True e False usados para representar valores de verdade (em contextos numéricos, 1 é True, enquanto 0 é False.


  Extra  

Há mais um literal especial usado em Python: o literal None. Esse literal é um objeto NoneType e é usado para representar a ausência de um valor. Vamos contar mais sobre isso em breve."""