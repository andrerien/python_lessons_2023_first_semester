# Se se quer saber quantas horas tem em x segundos, divide-se x por 3600, pois 1h = 3600s. 
# O resto do cálculo está em horas, portanto, multiplica-se por 60 para saber o valor de minutos. 
# O resto do cálculo estará em minutos, portanto, multiplica-se por 60 para saber o valor de segundos.
# Não há 1,9 segundo, portanto para qualquer resto na menor unidade de medida (segundo, neste caso) arredonda-se para mais, a partir de 0,5 decimais.
segundos = int(input("Digite o número de segundos: "))

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
segundos = int(input("Digite o número de segundos: "))

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")