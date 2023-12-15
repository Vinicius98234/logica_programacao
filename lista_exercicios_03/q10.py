def area_quadrado(lado, exibir=False):
    area = lado**2
    if exibir:
        print(f"A área do quadrado de lado {lado} é: {area}")
    return area

def area_triangulo(base, altura, exibir=False):
    area = (base * altura) / 2
    if exibir:
        print(f"A área do triângulo de base {base} e altura {altura} é: {area}")
    return area
