import os
import time

def limpar_tela():
    os.system('cls')

# Note que na propria variavel segundos, =0, significa que, se no código for utilizado a 'função esperar_segundos()'
# ao invés de dar erro, por padrão, o sistema já considera como 0
def esperar_segundos(segundos=0):
    time.sleep(segundos)

def soma(numero1, numero2):
    soma = numero1 + numero2
    return soma

def conversorFC(fahrenheit):
    celsius = (fahrenheit - 32)/1.8
    return celsius

def mudar_cor(codecor):
    os.system('color '+str(codecor))

