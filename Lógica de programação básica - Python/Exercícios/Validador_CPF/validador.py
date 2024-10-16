def get_cpf():
    cpf = input("Digite o CPF, com apenas númeoros: ")
    return cpf

def extract_nine_digits(cpf):
    return [int(digit) for digit in cpf[:9]]

def calculate_first_digit(cpf_numbrs):
    sum = 0
    for i, multiplier in enumerate(range(10, 1, -1)):
        sum += cpf_numbrs[i]*multiplier

    result = (sum * 10) % 11

    if result >= 10:
        return 0
    else: 
        return result
    
def calculate_second_digit(cpf_numbrs, first_digit):
    cpf_numbrs.append(first_digit)
    sum = 0
    for i, multiplier in enumerate(range(11,1, -1)):
        sum += cpf_numbrs[i]*multiplier
    result = (sum * 10) % 11

    if result >= 10:
        return 0
    else:
        return result
        
def check_cpf(cpf, first_digit, second_digit):
    return cpf[-2] == str(first_digit) and cpf[-1] == str(second_digit)

def validate_cpf():

    while True: 
        cpf = get_cpf()
        cpf_numbrs = extract_nine_digits(cpf)

        first_digit = calculate_first_digit(cpf_numbrs)
        second_digit = calculate_second_digit(cpf_numbrs, first_digit)

        if check_cpf(cpf, first_digit, second_digit):
            print("CPF válido")
        else:
            print("CPF inválido")

        repeat = input("Deseja realizar uma nova consulta? [S]im / [N]ão ").lower()
        if repeat != 's':
            print("Encerrando o programa.")
            break

if __name__ == "__main__":
    validate_cpf()