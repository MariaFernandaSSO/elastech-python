soma = 0
quantidade = 0

numero = float(input("Digite um número (0 para parar): "))

while numero != 0:
    soma = soma + numero
    quantidade = quantidade + 1
    numero = float(input("Digite um número (0 para parar): "))

print("Soma:", soma)

if quantidade > 0:
    print("Média:", soma / quantidade)
else:
    print("Nenhum número foi digitado.")
