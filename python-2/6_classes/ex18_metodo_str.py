class Aluna:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Aluna: {self.nome} ({self.idade} anos)"


aluna1 = Aluna("Maria", 18)
aluna2 = Aluna("Joana", 20)

print(aluna1)

lista = [aluna1, aluna2]
print(lista)

print("Diferença: sozinha o print usa o __str__, mas dentro da lista aparece o endereço do objeto.")
