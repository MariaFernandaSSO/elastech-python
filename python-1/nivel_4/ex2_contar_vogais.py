texto = input("Digite uma frase: ")

vogais = "aeiouáéíóúâêôãõà"
contador = 0

for letra in texto.lower():
    if letra in vogais:
        contador = contador + 1

print("Quantidade de vogais:", contador)
