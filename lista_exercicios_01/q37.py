tempo_segundos = int(input("Digite o tempo em segundos: "))
horas = tempo_segundos // 3600
minutos = (tempo_segundos % 3600) // 60
segundos = tempo_segundos % 60
print(f"{horas}:{minutos:02d}:{segundos:02d}")