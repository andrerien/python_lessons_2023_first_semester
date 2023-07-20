import os 
import time

def limpar_tela():
    os.system('cls')

def aguarde(segundos=0):
    time.sleep(segundos)

def ler_inteiro(mensagem):
    while True:
        try:
            variavel = int(input(mensagem))
            return variavel
        except:
            print('Valor informado incorretamente!')

def ler_string(mensagem):
    while True:
        variavel = input(mensagem)
        if len(variavel) > 1:
            return variavel

while True:
    limpar_tela()
    print('''Hackday - Inscrições')
    (0) Sair'
    (1) Inscrição'
    (2) Lista de inscritos''')
    opcao = input()
    if opcao == '0':
        break
    elif opcao == '1':
        print( 'Informe os dados abaixo para uma nova inscrição:')
        nome = ler_string('Nome: ')
        ra = ler_inteiro('RA: ')
        arquivo = open('banco_dados.bd', 'a')
        arquivo.write(nome+'-'+str(ra)+'\n')
        arquivo.close()
        print('Dados salvos!')
        aguarde(1)
    elif opcao == '2':
        try:
            arquivo = open('banco_dados.bd', 'r')
            dados = arquivo.read()
            print(dados)
            arquivo.close()
            aguarde(1)
        except:
            print('Nenhum dado encontrado')
            arquivo = open('banco_dados.bd', 'w')
            arquivo.close()
            aguarde(1)
    else:
        print('Opção inválida!')
        aguarde(1)