taxa = float(input("Digite o valor da hora de trabalho: "))
horas = int(input("Digite a quantidade de horas trabalhadas: "))

print()

salario_bruto = taxa * horas
print("+ Salário Bruto: R$ %.2f" % salario_bruto)

imposto_renda = salario_bruto * (11/100)
print("- IR (11%%): R$ %.2f" % imposto_renda)

inss = salario_bruto * (8 / 100)
print("- INSS (11%%): R$ %.2f" % inss)

sindicato = salario_bruto * (5/100)
print("- Sindicato (5%%): R$ %.2f" % sindicato)

salario_liquido = salario_bruto - imposto_renda - inss - sindicato
print("= Salário Líquido: R$ %.2f" % salario_liquido)

