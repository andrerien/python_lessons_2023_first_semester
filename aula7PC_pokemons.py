# Batalha de pokemons

def calcular_valor_golpe(ataque, defesa, bonus):
    return ataque + defesa / 2 + bonus

def calcular_vencedor(nome_combatente1, nome_combatente2, num_batalhas):
    for _ in range(num_batalhas):
        bonus = int(input("Digite o valor do bônus: "))
        ataque1, defesa1, level1 = map(int, input(f"Digite, espaçadamente, osvalores de Ataque, Defesa e Level para {nome_combatente1}: ").split())
        ataque2, defesa2, level2 = map(int, input(f"Digite, espaçadamente, os valores de Ataque, Defesa e Level para {nome_combatente2}: ").split())

        if level1 % 2 == 0:
            bonus1 = bonus
        else:
            bonus1 = 0

        if level2 % 2 == 0:
            bonus2 = bonus
        else:
            bonus2 = 0

        valor_golpe1 = calcular_valor_golpe(ataque1, defesa1, bonus1)
        valor_golpe2 = calcular_valor_golpe(ataque2, defesa2, bonus2)

        if valor_golpe1 > valor_golpe2:
            print(f"Vencedor: {nome_combatente1}")
        elif valor_golpe1 < valor_golpe2:
            print(f"Vencedor: {nome_combatente2}")
        else:
            print("Empate")

nome_combatente1 = input("Digite o nome do combatente 1: ")
nome_combatente2 = input("Digite o nome do combatente 2: ")
num_batalhas = int(input("Digite o número de batalhas: "))

calcular_vencedor(nome_combatente1, nome_combatente2, num_batalhas)