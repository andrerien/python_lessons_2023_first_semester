# Tabela de preços dos produtos
produtos = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

# Variável para acumular o valor total da compra
total = 0.0

# Loop para inserção dos produtos
while True:
    # Entrada de dados
    t, q = map(int, input("Digite o tipo de produto (1001 a 1005) seguido de espaço e a quantidade do produto (1 a 500): ").split())
    # Verifica se o tipo de produto é válido
    if t not in produtos:
        print(f"Tipo de produto inválido: {t}")
        continue
    # Verifica se a quantidade de produtos é válida
    if q < 1 or q > 500:
        print(f"Quantidade de produtos inválida: {q}")
        continue
    # Calcula o valor total da compra
    total += q * produtos[t]
    # Pergunta ao usuário se deseja adicionar mais produtos
    resp = input("Deseja adicionar mais produtos? (S/N) ").strip().upper()
    if resp == "N":
        break

# Saída de dados
print(f"Valor total da compra: R$ {total:.2f}")