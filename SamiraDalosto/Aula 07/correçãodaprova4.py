#4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
#aritmética simples delas.
print("Inspeção de Peças")
nota1 = float(input("Digie a nota da inspeção 1 (0 a 10)"))
nota2 = float(input("Digie a nota da inspeção 1 (0 a 10)"))
nota3 = float(input("Digie a nota da inspeção 1 (0 a 10)"))
media = (nota1 + nota2 + nota3) / 3
print(f"Média de qualidade de peças: {media: .2f}")
print(f"Média de qualidade de peças:", round(media, 2))
