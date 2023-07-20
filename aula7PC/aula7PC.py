# Aqui temos 2 bibliotecas: 'os' e 'time'

from funcoes import limpar_tela, esperar_segundos, soma, conversorFC, mudar_cor
import os
import time

def limpar_tela():
    os.system('cls')

limpar_tela()
print('Seja bem-vindo ao sistema')
esperar_segundos(1)
while True:
    limpar_tela()
    print('(0) Sair')
    print('(1) Conversão em Cº')
    print('(2) Conversão em Fº')
    opcao = input()
    if opcao == '0':
        break
    elif opcao == '1':
        print('Convertendo Fº para Cº')
        fahrenheit = int(input('Fahrenheit: '))
        print('Em Celsius é,', conversorFC(fahrenheit))
        input('press enter to continue')
    elif opcao == '2':
        codecor = int(input('Informe o código da cor: '))
        mudar_cor(codecor)
        input('press enter to continue')
    elif opcao == '3':
        os.system('calc')
    elif opcao == '3':
        n1 = int(input("Numero1: "))
        n2 = int(input('Numero2: '))
        esperar_segundos(2)
    else:
        print('Opção inválida')
        esperar_segundos(2)

print('Volte sempre')