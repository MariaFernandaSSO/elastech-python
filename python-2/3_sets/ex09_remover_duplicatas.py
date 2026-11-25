numeros = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print("Lista com repetidos:", numeros)

sem_repetidos = list(set(numeros))
print("Lista sem repetidos:", sem_repetidos)

meu_set = set(numeros)

try:
    print(meu_set[0])
except TypeError as erro:
    print("Deu erro! Set não tem índice:", erro)
