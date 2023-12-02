a, b, c = sorted(map(float, input("Digite três valores de ponto flutuante separados por espaço: ").split()), reverse=True)

if a >= b + c:
    tipo_tri = "NAO FORMA TRIANGULO"
elif a**2 == b**2 + c**2:
    tipo_tri = "TRIANGULO RETANGULO"
elif a**2 > b**2 + c**2:
    tipo_tri = "TRIANGULO OBTUSANGULO"
elif a**2 < b**2 + c**2:
    tipo_tri = "TRIANGULO ACUTANGULO"

if a == b == c:
    tipo_lado = "TRIANGULO EQUILATERO"
elif a == b or b == c or a == c:
    tipo_lado = "TRIANGULO ISOSCELES"
else:
    tipo_lado = ""

print(tipo_tri)
if tipo_lado:
    print(tipo_lado)
