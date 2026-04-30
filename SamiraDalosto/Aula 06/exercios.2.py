#Execício 2
#Simule um semafaro com parada cada cor. 
#Determine um tempo que deseja para que qunado mudar para tal cor ele represente uma pausa
print("simular de semafaro")
print("1 - vermelho")
print("2 - amarelo")
print("3 - verde")
cores = int(input("escolha a cor desejada: \n "))
for i in range(1,6):
    from time import sleep
if cores == 1:
    print (" vermelha")
    sleep(2.0)
for i in range(1,6):
    if cores == 2:
        print("verde")
    sleep(2.0)
for i in range(1,6):
    if cores == 3:
        print("amarelo")
    sleep(2.0)
else:
    print("Somente essas cores!")
    sleep(2.0)

        