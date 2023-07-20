import os

 #limpar tela
def limpar_tela():
    os.system('cls')
    
while True:
    desafiante = input("Desafiante: ")
    jogador = input("Jogador: ")
    palavra = input("Palavra: ").lower()
    dica1 = input("Digite a primeira dica: ")
    dica2 = input("Digite a segunda dica: ")
    dica3 = input("Digite a terceira dica: ")
    limpar_tela()

    # letras ocultas
    letras_escondidas = []
    for letra in palavra:
        letras_escondidas.append('*')

    # letras usadas
    def exibir_palavra(letras):
        print('Palavra: ', end='')
        for letra in letras:
            print(letra, end=' ')
        print()

    # dicas
    dicas = [dica1, dica2, dica3]
    dicas_usadas = []
    def exibir_dica():
        if dicas_usadas == dicas:
            print("Todas as dicas já foram usadas.")
        else:
            dica_atual = dicas[len(dicas_usadas)]
            print("Dica: ", dica_atual)
            dicas_usadas.append(dica_atual)

    # letras erradas
    letras_erradas = []
    def exibir_letras_erradas():
        if len(letras_erradas) > 0:
            print("Letras erradas: ", end='')
            for letra in letras_erradas:
                print(letra, end=' ')
            print()

    # Loop do jogo
    erros = 0
    while True:
        exibir_palavra(letras_escondidas)
        exibir_letras_erradas()

        jogada = input("Digite uma letra ou 'dica' para receber uma dica: ").lower()

        if jogada == 'dica':
            exibir_dica()
            continue

        if len(jogada) != 1 or not jogada.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if jogada in palavra:
            for i in range(len(palavra)):
                if palavra[i] == jogada:
                    letras_escondidas[i] = jogada
            if '*' not in letras_escondidas:
                print("Parabéns, você ganhou! A palavra era {}.".format(palavra))
                opcao = input("Deseja continuar jogando? (s/n) ").lower()
                vencedor = jogador if erros < 5 else desafiante
                arquivo = open('A.bd', 'a')
                arquivo.write(palavra+' '+desafiante+' '+vencedor+'\n')
                arquivo.close()
                if opcao == 's':
                    break
                else:
                    exit()
        else:
            erros += 1
            letras_erradas.append(jogada)
            print("Letra incorreta. Você tem mais {} tentativas.".format(5-erros))
            if erros == 5:
                opcao = input("Você perdeu. Deseja continuar jogando? (s/n) ").lower()
                vencedor = jogador if erros < 5 else desafiante
                arquivo = open('A.bd', 'a')
                arquivo.write(palavra+' '+desafiante+' '+vencedor+'\n')
                arquivo.close()
                if opcao == 's':
                    break
                else:
                    exit()