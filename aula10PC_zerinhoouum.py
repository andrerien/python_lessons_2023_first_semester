def calcular_vencedor(participantes, valores):
    if valores.count("1") == 3 or valores.count("0") == 3:
        return "Não há vencedor"
    else:
        for i in range(3):
            if valores.count(valores[i]) == 1:
                return participantes[i]

# Obter nomes dos participantes
participantes = []
for i in range(3):
    nome = input("Digite o nome do participante {}: ".format(i + 1))
    participantes.append(nome)

# Obter valores jogados
valores = input("Digite os valores jogados por cada participante (exemplo: 1 0 1): ").split()

# Verificar o vencedor
vencedor = calcular_vencedor(participantes, valores)

print("O vencedor é:", vencedor)