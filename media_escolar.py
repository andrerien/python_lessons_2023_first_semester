nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))
nota3 = float(input("Informe a terceira nota do aluno: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("O aluno foi aprovado com média:", media)
else:
    if media >= 4:
        print("O aluno está em exame com média:", media)
    else:
        print("O aluno foi reprovado com média:", media)