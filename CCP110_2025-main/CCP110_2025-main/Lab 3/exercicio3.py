question = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")

aresta = float(input("Digite o valor da aresta a em metros: "))

if question == "dodecaedro":
    result = ((15 + (7 * 2.2360679774)) / 4) * (aresta ** 3)
    print(f"O volume de um dodecaedro regular com {aresta:.2f} de aresta é: {result:.2f}")

elif question == "icosaedro":
    result1 = ((5 / 12) * (3 + 2.2360679774)) * (aresta ** 3)
    print(f"O volume de um icosaedro regular com {aresta:.2f} de aresta é: {result1:.2f}")