import math
lado_quadrado = float(input("Digite o valor do lado do quadrado: "))
perimetro = 4 * lado_quadrado
area = lado_quadrado ** 2
diagonal = lado_quadrado * math.sqrt(2)
print(f"Perímetro do quadrado: {perimetro}")
print(f"Área do quadrado: {area}")
print(f"Diagonal do quadrado: {diagonal}")
