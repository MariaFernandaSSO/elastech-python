frase = "       python é legal         "

print("Tamanho antes:", len(frase))

frase_limpa = frase.strip()
print("Frase sem espaços:", frase_limpa)
print("Tamanho depois:", len(frase_limpa))

nova_frase = frase_limpa.replace("python", "Java")
print("Frase trocada:", nova_frase)
