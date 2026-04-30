#Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
#exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

print("Classiicaodr de Lotes")
l1 = input("Digite o códdigo de produto:\n")
if l1 == "A":
    print("Alimentos")
elif l1 == "E":
   print("Eletronicos")
else:
   print("Desconhecido")