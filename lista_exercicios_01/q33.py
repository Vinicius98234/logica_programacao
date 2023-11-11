tempo_viagem1 = float(input("Digite o tempo gasto na primeira viagem (em horas): "))
velocidade_media1 = float(input("Digite a velocidade média na primeira viagem (em km/h): "))
tempo_viagem2 = float(input("Digite o tempo gasto na segunda viagem (em horas): "))
velocidade_media2 = float(input("Digite a velocidade média na segunda viagem (em km/h): "))
distancia1 = tempo_viagem1 * velocidade_media1
litros_necessarios1 = distancia1 / 12
distancia2 = tempo_viagem2 * velocidade_media2
litros_necessarios2 = distancia2 / 12
print(f"{litros_necessarios1:.3f}")
print(f"{litros_necessarios2:.3f}")
