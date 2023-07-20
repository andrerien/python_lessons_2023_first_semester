def pode_formar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a != b and a != c and b != c:
        return "Escaleno"
    else:
        return "Isósceles"

def triangulo_retangulo(a, b, c):
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return "Retângulo"
    else:
        return "Não é retângulo"

a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))

if pode_formar_triangulo(a, b, c):
    print("Os valores inseridos podem formar um triângulo.")
    print("O triângulo é do tipo", tipo_triangulo(a, b, c))
    print("O triângulo é", triangulo_retangulo(a, b, c))
else:
    print("Os valores inseridos não podem formar um triângulo.")