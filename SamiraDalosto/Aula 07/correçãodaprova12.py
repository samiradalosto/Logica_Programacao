
print("Multiplas Leitura")
temperaturas = []
for i in range(1, 6):
    temp = float(input(f"Digite a temperatura do sensor {i} em °C ..."))
    temperaturas.append(temp)
print(f"Maior temperatuara lida: {max(temperaturas):.2f}°C")

