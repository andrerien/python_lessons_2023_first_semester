n = int(input('Insira um valor: '))
if n <= 0 or n >= 9999999999:
    print("O valor deve estar entre 0 e 9999999999")
else:
    n_str = str(n)
    n_invertido = n_str[::-1]
    print(int(n_invertido))

# Para inverter o número, utilizamos o conceito de slicing em strings do Python. O slice "[::-1]" indica que 
# queremos acessar toda a string "n_str", 
# mas de trás para frente, com um passo de -1 (ou seja, percorrendo a string de trás para frente). 
# O resultado desse slicing é armazenado em uma nova string chamada "n_invertido".