distancia_km = float(input("Digite a distância da viagem em km: "))

tarifa_curta = 0.50  
tarifa_longa = 0.45  

if distancia_km <= 200:
    preco_passagem = distancia_km * tarifa_curta
else:
    preco_passagem = distancia_km * tarifa_longa

print(f"O preço da passagem para uma viagem de {distancia_km:.2f} km é: R$ {preco_passagem:.2f}")
