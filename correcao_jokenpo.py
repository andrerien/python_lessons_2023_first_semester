# Função que corrige o resultado do jogo
def corrigir_jogo_jokenpo(jogador1, jogador2):
    # Verifica se algum jogador trapaceou
    if jogador1 == jogador2:
        return "Empate"
    elif jogador1 not in ["pedra", "papel", "tesoura"] or jogador2 not in ["pedra", "papel", "tesoura"]:
        return "Trapaceou"
    
    # Verifica quem ganhou
    if jogador1 == "pedra":
        if jogador2 == "tesoura":
            return "Jogador 1 venceu"
        else:
            return "Jogador 2 venceu"
    elif jogador1 == "papel":
        if jogador2 == "pedra":
            return "Jogador 1 venceu"
        else:
            return "Jogador 2 venceu"
    elif jogador1 == "tesoura":
        if jogador2 == "papel":
            return "Jogador 1 venceu"
        else:
            return "Jogador 2 venceu"

# Solicita as opções escolhidas pelos jogadores
jogador1 = input("Jogada do jogador 1: ")
jogador2 = input("Jogada do jogador 2: ")

# Corrige o resultado do jogo e imprime o resultado
resultado = corrigir_jogo_jokenpo(jogador1, jogador2)
print('Resultado do jogo: ', resultado)