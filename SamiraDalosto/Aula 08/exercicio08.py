#Exercicio 8
#Criar um script de monetoramento de temperatura
#Escreva um script qie monitore a emperatura de um motor. O script
# monitore a temperatura de um motor.O script deve ler a temperatura de 
# um arquivo "temperatura.txt"e exibrir uma mensagem de alerta se a temperatura estiver acima de 70°C.

with open("temperatura.txt", "w") as motor:
   motor.write("Monitore a temperaturade um motor")
   motor.write("\n ler sobre Clean code.")

