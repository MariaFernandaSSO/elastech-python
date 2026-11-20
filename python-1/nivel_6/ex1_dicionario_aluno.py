aluno = {
    "nome": "Maria",
    "notas": [8.0, 7.5, 9.0]
}

media = sum(aluno["notas"]) / len(aluno["notas"])

print("Aluno:", aluno["nome"])
print("Notas:", aluno["notas"])
print("Média:", round(media, 2))
