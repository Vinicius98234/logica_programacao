distancia_percorrida = float(input("Digite a distância total percorrida (em km): "))
combustivel_gasto = float(input("Digite o total de combustível gasto (em litros): "))
consumo_medio = distancia_percorrida / combustivel_gasto
print(f"{consumo_medio:.3f} km/l")