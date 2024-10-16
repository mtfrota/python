
Entenda o algoritimo do CPF:

CPF: 625.837.693-24
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma contagem regressiva
começando de 10.

Ex.: 625.837.693-24
10  9   8   7   6   5   4   3   2   
6   2   5   8   3   7   6   9   3
60 18  40  56  18  35  24  27  6

Somar todos os resultados:
60+18+40+56+18+35+24+27+6 = 284

multiplicar o resultado anterior por 10
284*10 = 2840

Obter o resto da divisão da conta anterior por 11
2840 % 11 = 2

se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

o primeiro digito do CPF é 

Para o segundo dígito verificador:

Multiplica-se os primeiros 10 números (os 9 originais mais o primeiro dígito verificador) por valores decrescentes de 11 a 2.
Soma-se o resultado de cada multiplicação.
O valor da soma é multiplicado por 10 e dividido por 11.
O resultado é o segundo dígito verificador, 
com a mesma regra de exceção para o resto 10.

Ex.: 625.837.693-24
11  10  9   8   7   6   5   4   3   2
6   2   5   8   3   7   6   9   3   2
66  20  45  64  21  42  30  36  9   4

Somar todos os resultados:
66+20+45+64+21+42+30+36+9+4 = 337

337*10 = 3370
3370 % 11 = 4

segundo digito é 4

