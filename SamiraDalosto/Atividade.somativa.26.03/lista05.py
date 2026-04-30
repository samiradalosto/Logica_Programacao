#Termostato Inteligente: Peça a temperatura de um motor.
#Abaixo de 40°C: "Baixa carga".
#Entre 40°C e 70°C: "Normal".
#Acima de 70°C: "ALERTA: Resfriamento Ativado!".

print("Peça de termostrato")
temp = int(input("Qual é a temperatura do motor: \n"))
if temp <= 40:
    print("Normal")

elif temp <70:
    print("Normal")
else:
    print("Alerta : Tmperatura alta: resfrimeno ativado ")
    
    