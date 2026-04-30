#Exercios 4 
#soma de cargas de Energia (for)
#Uma fabrica tem 5 máquinas. Peça ao usuário (via input dentro do loop)
#o consumo em kWh de cada uma das 5 máquinas.Ao final do loop, o programa
# deve exibir o consumo total da fábrica.
total = 0
print("fábrica de carga de energia, \n")
for maquina in range(1,6):
    print(f"{maquina} °maquina")
    consumo = int(input("Digeite a qantiade de kWh de consumo, \n"))
    total += consumo
print("consumo total da fábrica", total )
