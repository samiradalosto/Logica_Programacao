#Termostato Inteligente: Peça a temperatura de um motor.
#● Abaixo de 40°C: "Baixa carga".
#● Entre 40°C e 70°C: "Normal".
#● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

print("Termostato Inteligente")
temperatura = float(input("Digite a temperatura do motor em °C..."))
if temperatura < 40:
    print("Baixa carga")
elif 40 <= temperatura <= 70:
    print("Normal")
else:
    print("Alerta: Resfriando Ativado!")

#Segundo exemplo:

print("Termotato Inteligente - Versão 2 ")
temperatura = float(input("digite a temperatura do motor em °C ..."))
if temperatura < 40:
    print("Baixa carga")
elif temperatura> 70:
    print("Alerta: Resfriamento Ativado !")
else:
    print("Normal")