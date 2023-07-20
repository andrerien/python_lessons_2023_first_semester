x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

soma = 0
i = 0

if x % 2 == 0: # se X é par, soma-se 1 para torná-lo ímpar
    x += 1

while i < y: # repetir Y vezes
    soma += x # adicionar o valor atual de X à soma
    x += 2 # avançar para o próximo número ímpar
    i += 1 # incrementar o contador

print("A soma dos", y, "números ímpares consecutivos a partir do valor de X é", soma)