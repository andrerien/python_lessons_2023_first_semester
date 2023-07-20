# Note que o valor na lista está como "valor+1", isso porque a lista exclui o último elemento
valor = int(input("Digite um valor inteiro positivo: "))

for i in range(1, valor+1):
    if i % 4 == 0:
        print("PUM")
    else:
        print(i)