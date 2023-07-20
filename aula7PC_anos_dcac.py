# Há muito, muito tempo atrás

# Número de casos de teste
N = int(input("Digite a quantidade de anos transcorridos a ser inserida: "))

anos_transcorridos = []

def calcular_ano(evento):
    if evento < 2015:
        return 2014 - evento + 1, 'D.C.'
    elif evento > 2015:
        return evento - 2014, 'A.C.'
    else:
        return 1, 'A.C.'
for _ in range(N):
    T = int(input("Digite o número de anos transcorridos: "))
    anos_transcorridos.append(T)
# Calcular e exibir os anos correspondentes
for T in anos_transcorridos:
    ano, era = calcular_ano(T)
    print(f"{ano} {era}")