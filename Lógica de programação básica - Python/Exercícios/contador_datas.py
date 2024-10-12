from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcular_diferenca(data_inicio, data_fim):
    data_inicio = datetime.strptime(data_inicio, "%m/%Y")
    data_fim = datetime.strptime(data_fim, "%m/%Y")
    diferenca = relativedelta(data_fim, data_inicio)
    print(f"A diferença é de {diferenca.years} anos e {diferenca.months} meses.")

while True:
    data_inicio = input("Digite a data de início (formato: mês/ano): ")
    data_fim = input("Digite a data final (formato: mês/ano): ")
    calcular_diferenca(data_inicio, data_fim)

    repetir = input("Deseja calcular uma nova data? (s/n): ").lower()

    if repetir != 's':
        print("Saindo")
        break
