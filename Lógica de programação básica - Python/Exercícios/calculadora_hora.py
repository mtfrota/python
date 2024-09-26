from datetime import datetime, timedelta

def add_times(start_time, durations):
    # Converte o horário de início para um objeto datetime
    start = datetime.strptime(start_time, '%H:%M')

    # Converte o horário de início para minutos totais
    total_minutes = start.hour * 60 + start.minute

    # Itera sobre cada duração e soma os minutos
    for duration in durations:
        duration_time = datetime.strptime(duration, '%H:%M')
        total_minutes += duration_time.hour * 60 + duration_time.minute
    
    # Cria um objeto timedelta com o total de minutos
    new_time = timedelta(minutes=total_minutes)
    
    # Calcula a nova hora e minuto com base no total de minutos
    total_hours, minutes = divmod(total_minutes, 60)
    hours = total_hours % 24
    
    # Formata o resultado como uma string no formato HH:MM
    return f'{int(hours):02}:{int(minutes):02}'

# Entrada do usuário
start_time = input('Digite o horário de início (HH:MM): ')
durations = []

while True:
    duration = input('Digite uma duração (HH:MM) ou "sair" para encerrar: ')
    if duration.lower() == 'sair':
        break
    durations.append(duration)

# Chama a função e exibe o resultado
print(f'Soma: {add_times(start_time, durations)}')
