#Exercício 6 - uma balança industrial está pensando em um lote de 6 
#saco de isumos.o peso idealde cada saco é 5kg, mas o sistema aceita variações 
total = 0
for sacos in range(1,7):
    print(f"{sacos}° saco de isumo:")
    pesos = int(input("Digite a quantidade de kg dp saco, pouco acima de 50kg: \n"))
    total += pesos 
print("O valor total de kg dos 6 é igual a", total)