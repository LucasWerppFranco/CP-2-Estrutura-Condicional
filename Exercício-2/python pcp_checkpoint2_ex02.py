def tipo_triangulo(a, b, c):
    lados = sorted([a, b, c], reverse=True)
    A, B, C = lados[0], lados[1], lados[2]

    if A >= B + C:
        return "NAO FORMA TRIANGULO"

    if A**2 == B**2 + C**2:
        return "TRIANGULO RETANGULO"
    elif A**2 > B**2 + C**2:
        return "TRIANGULO OBTUSANGULO"
    elif A**2 < B**2 + C**2:
        return "TRIANGULO ACUTANGULO"

    if A == B == C:
        return "TRIANGULO EQUILATERO"
    elif A == B or A == C or B == C:
        return "TRIANGULO ISOSCELES"

    return "TRIANGULO ESCALENO"


a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

resultado = tipo_triangulo(a, b, c)
print(resultado)

