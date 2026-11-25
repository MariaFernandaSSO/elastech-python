notas = {
    "Ana": 8.5,
    "Beatriz": 7.0,
    "Carla": 9.5
}

try:
    print(notas["Julia"])
except KeyError as erro:
    print("Deu erro! A chave não existe:", erro)

print("Nota da Julia com get:", notas.get("Julia", "aluna não encontrada"))

notas["Daniela"] = 6.5
print("Depois de adicionar a Daniela:", notas)

notas["Beatriz"] = 8.0
print("Depois de alterar a nota da Beatriz:", notas)
