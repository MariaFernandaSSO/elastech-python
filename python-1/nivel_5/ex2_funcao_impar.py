def eh_impar(n):
    return n % 2 != 0

print("Números ímpares de 1 a 100:")
for numero in range(1, 101):
    if eh_impar(numero):
        print(numero)

print("Números pares de 1 a 100:")
for numero in range(1, 101):
    if not eh_impar(numero):
        print(numero)
