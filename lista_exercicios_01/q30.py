a, b, c = map(float, input("Digite os valores a, b e c (separados por espaço): ").split())
area_tri_retangulo = (a * c) / 2
PI = 3.14159
area_circulo = PI * c ** 2
area_trapezio = ((a + b) * c) / 2
area_quadrado = b ** 2
area_retangulo = a * b
print(f"TRIANGULO: {area_tri_retangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")