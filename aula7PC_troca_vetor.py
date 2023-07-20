# Troca em Vetor I

vetor = []

def trocar_elementos(vetor):
    tamanho = len(vetor)
    for i in range(tamanho // 2):
        vetor[i], vetor[tamanho - 1 - i] = vetor[tamanho - 1 - i], vetor[i]
# Leitura dos valores do usuário
for i in range(20):
    valor = int(input(f"Digite o valor para N[{i}]: "))
    vetor.append(valor)
# Troca dos elementos
trocar_elementos(vetor)
# Exibição do vetor modificado
for i, valor in enumerate(vetor):
    print(f"N[{i}] = {valor}")