#lista detemperaturas lidas pelo sensor por minuto
leituras = [70 ,75, 82, 98, 110, 85, 80]

for temp in leituras:
    if temp > 100:
        print(f"CRITÌCO: {temp} °C detectado! Acionando parada de emergência.")
        break # o loop para aqui e NÃo l~e os proximos valores (85 e 80)
    print(f"temperatura está em {temp}°C. operação normal.")


print("Sistema desligado. Aguaradando manutenção.")