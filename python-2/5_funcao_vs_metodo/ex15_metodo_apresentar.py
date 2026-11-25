class Aluna:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Meu nome é {self.nome}")


aluna = Aluna("Maria")
aluna.apresentar()

print("Resposta: a função é solta e chamada pelo nome, já o método fica dentro da classe e é chamado pelo objeto.")
