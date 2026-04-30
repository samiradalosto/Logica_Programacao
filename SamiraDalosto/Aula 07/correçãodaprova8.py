#8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
#o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
#"Processo Otimizado".

print("Cálculo de Descarte")
total_pecas = int(input("Digite o total de peças produzidas..."))
total_defetuosas = int(input("Digite o total de peças defeituosas"))
descarte_percentual = (total_defetuosas / total_pecas) * 100
if descarte_percentual > 5:
    print("Revisar Processo")
else:
    print("Processo Otimizado")
    print(f"Descarte percentual: {descarte_percentual:, 2f}%")

