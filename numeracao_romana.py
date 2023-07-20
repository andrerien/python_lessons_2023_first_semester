def converter_romano(n):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    romano = ''
    i = 0
    while n > 0:
        for _ in range(n // valores[i]):
            romano += simbolos[i]
            n -= valores[i]
        i += 1
    return romano

n = int(input("Digite um número inteiro entre 1 e 999: "))

if n < 1 or n > 1000:
    print("Número inválido. Digite um número entre 1 e 999.")
else:
    print(converter_romano(n))