salario = float(input("Insira seu salário: "))

if salario > 1250:
    novo_salario = salario * 1.1

else:
    novo_salario = salario * 1.15

print("seu novo salário é de R$ %.2f" % novo_salario)