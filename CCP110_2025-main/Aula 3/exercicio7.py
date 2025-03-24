distancia = float(input("Quantos km você deseja percorrer: "))

if distancia <= 200:
    distancia = distancia * 0.5
    print("seu custo é de R$ %.2f" % distancia)

elif distancia > 200:
    distancia = distancia * 0.45
    print("seu custo é de R$ %.2f" % distancia)