#Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
#o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
#"Processo Otimizado".
print("Calculo de dercarte")
ps = int(input("digite o total de peças prontas; \n"))
paa = int(input("Digite qual é o total de peças defeituosas?; \n"))
defeituosas = ps/ paa* 0.05 /100
if paa > defeituosas:
     print("Revisar o processo")
else: 
     print("Processo otimizado ")