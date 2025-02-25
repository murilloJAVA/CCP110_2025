from math import ceil

PI = 3.1415

#Capturar os dados dos usuarios
altura = float(input("Altura: "))
raio = float(input("Raio: "))

#Calcular a area da base
area_base = PI * (raio ** 2)
# print(f"a área da base é: {area_base}")

#Calcular a area lateral
area_lateral = 2 * PI * raio * altura
# print(f"a área lateral é: {area_lateral}")

#Calcula a area total a ser pintada
area_total = 1 * area_base + area_lateral
print (f"a área a ser pintada: {area_total:.2f} m²")

litros = area_total / 3 
print(f"Quantidade de litros necessários: {litros:.2f}")

latas = (litros / 5)
print(f"Quantidade de latas: {latas:.2f}")


