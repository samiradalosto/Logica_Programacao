#11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
#O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

print("Soma de Produção (Acumulador)")
peso_total = 0
while True:
    peso_caixa = float(input("Digite o peso da caixa(0para)"))
    if peso_caixa == 0 :
        break
    peso_total += peso_caixa
print(f"Peso total acumulando::{peso_total:.2f}")
