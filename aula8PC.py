while True:
    try:
        numero = int(input('Número: '))
        print(numero)
        break
    except:
        print("Número inválido")

print('Continuando programa')