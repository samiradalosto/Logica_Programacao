#Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
#botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
#iniciar.
print("Segurança de Operação")
sensor_porta = input("Digite o status do sensor da porta (fehada/aberta...")
botao_emergencia = input("Digite o status do botão de emergencia (ligado/desligado)...")
if sensor_porta == "fechada" and botao_emergencia == "desligadp" :
    print("A máquina pode iniciar.")
else:
    print("A máquina não pode iniciar.")