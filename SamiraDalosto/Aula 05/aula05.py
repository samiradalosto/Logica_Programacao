#Use o Laço "for" (Repitiçaõ Determinadas)
#Use o "for " quando você sabe extamente 
#Quantas vazes algo deve 
#Acontecer (como ler 10 sensores ou processar uma lista de peças )
#Exemplo: Relatório de produção Diária 
#imagene que você tem uma meta de produzir 5 lote se quer numerar cada um

#Exercio
for lote in range(1,6):
    print(f"Processo lote numéro {lote}...")
    print("Quantidade verficada. [Ok]")
    print("Produção do dia finalizada!")

#Imagine que você queira armazenar 10 carros 
for carros in range(10):
    print(f"Quantidade de carros {carros}")


    #Exemplo 2
    for i in range(5):
        print(i)

    #Exemplo 3 
    peças = {"Engrenagem", "Eixo", "Rolamento", "Parafuso"}
    maquinas = ["Máquina 1", "Máquina 2"]

    for item in peças :
        print(F"Item em estoque: {item}")
        for maq in maquinas:
            print(f"Máquinas que temos {maq}")
            