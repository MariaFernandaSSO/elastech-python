numeros = []

for i in range(5):
    numero = float(input("Digite o número " + str(i + 1) + ": "))
    numeros.append(numero)

print("Lista:", numeros)
print("Maior:", max(numeros))
print("Menor:", min(numeros))
print("Média:", sum(numeros) / len(numeros))
