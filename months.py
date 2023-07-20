# Solicita ao usuário um número de 1 a 12
num = int(input("Insira o número do mês: "))

# Verifica se o número está dentro do intervalo válido
if num < 1 or num > 12:
    print("Número inválido. Insira um valor entre 1 e 12.")
else:
    # Cria uma lista com o nome dos meses em inglês
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    # Obtém o nome do mês correspondente ao número inserido
    month_name = months[num-1]
    
    # Imprime o nome do mês
    print(month_name)