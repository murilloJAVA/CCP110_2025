somatoria = 0 

while True:
    entrada = int(input("Digite um número a somar ou 0 para sair: "))
    if entrada == 0:
        break
    else:
        somatoria = somatoria + entrada

print("Somatoria: ", somatoria)
