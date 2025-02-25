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
print(f"Quantidade de latas: {latas:.0f}")

#verificar custo unitario
if latas == 1:
    custo = 50
if latas == 2:
    custo = 48
if latas == 3:
    custo = 46
if latas > 3:
    custo = 45


print(f"Preço unitário: R$ {custo:.2f}")
print(f"Custo total: R$ {latas * custo:.2f}")


