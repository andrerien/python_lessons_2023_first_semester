n = int(input("Insira o valor sorteado: "))

if n <= 0 or n > 10**6:
    print("Valor sorteado inválido.")
else:
    ho = "Ho " * (n-1) + "Ho!"
    print(ho)