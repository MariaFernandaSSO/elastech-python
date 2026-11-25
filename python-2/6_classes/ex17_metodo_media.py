class Aluna:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


aluna1 = Aluna("Maria", 18, [8.0, 9.0])
aluna2 = Aluna("Joana", 20, [])

print("Média da", aluna1.nome, ":", aluna1.media())
print("Média da", aluna2.nome, ":", aluna2.media())
