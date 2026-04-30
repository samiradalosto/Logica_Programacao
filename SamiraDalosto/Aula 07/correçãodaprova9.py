#9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
#diga se está dentro da tolerância, acima ou abaixo.

print("Validação da medida")
medida = float(input("digite a medi da peça em mm..."))
if medida <9.8:
  print("Apeças está abaixo da tolerância.")
elif medida > 10.2:
  print("Apeça está acima da toleância.")
else:
  print("A peça está dentro da tolerância")
