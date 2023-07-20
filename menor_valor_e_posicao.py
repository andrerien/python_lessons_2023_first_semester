n = int(input('Insira o número de valores a serem inseridos: '))
valores = list(map(int, input('Insira, espaçadamente, os valores: ').split()))

menor_valor = valores[0]
posicao = 0

for i in range(1, n):
    if valores[i] < menor_valor:
        menor_valor = valores[i]
        posicao = i

print(menor_valor)
print(posicao)