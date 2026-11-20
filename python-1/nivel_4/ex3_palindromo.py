palavra = input("Digite uma palavra: ")

palavra_limpa = palavra.lower().replace(" ", "")

invertida = palavra_limpa[::-1]

if palavra_limpa == invertida:
    print(palavra, "é um palíndromo!")
else:
    print(palavra, "não é um palíndromo.")
