"""Calculadora com While"""

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numero_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numero_validos = None

        if numero_validos is None:
            print('Um ou ambos os números digitados são invalidos. ')
            continue
        
    sair = input('Quer sair? [s]im:').lower().startswith('s')

    if sair is True:
        break