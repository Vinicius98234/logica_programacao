temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]

menor_temperatura = min(temperaturas)
maior_temperatura = max(temperaturas)

temperatura_media = sum(temperaturas) / len(temperaturas)

print(f"Menor temperatura: {menor_temperatura}°C")
print(f"Maior temperatura: {maior_temperatura}°C")
print(f"Temperatura média: {temperatura_media:.2f}°C")
