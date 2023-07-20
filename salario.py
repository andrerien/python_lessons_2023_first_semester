nome = input ('Nome: ')
salario_fixo = float(input('Salário Fixo R$: '))
total_vendas = float(input('Total de vendas no mês R$: '))
comissao = total_vendas*0.15
salario_final = salario_fixo + comissao
print ("Salário final (salário fixo + comissão) = R$:", salario_final)