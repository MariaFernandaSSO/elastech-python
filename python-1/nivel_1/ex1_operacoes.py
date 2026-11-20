numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Soma:", numero1 + numero2)
print("Subtração:", numero1 - numero2)
print("Multiplicação:", numero1 * numero2)

if numero2 != 0:
    print("Divisão:", numero1 / numero2)
else:
    print("Divisão: não é possível dividir por zero")
