for i in range(1, 11):
    print (f"\nTabuada do {i}:")
    for j in range(1, 11):
        print (f"{i} x {j} = {i *j}")


#------------------------------------------------------------------------------#
#lista detemperaturas lidas pelo sensor por minuto
leituras = [70 ,75, 82, 98, 110, 85, 80]

for temp in leituras:
    if temp > 100:
        print(f"CRITÌCO: {temp} °C detectado! Acionando parada de emergência.")
        break # o loop para aqui e NÃo l~e os proximos valores (85 e 80)
    print(f"temperatura está em {temp}°C. operação normal.")


print("Sistema desligado. Aguaradando manutenção.")
#------------------------------------------------------------------------------#
materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
for peca in materiais:
    if peca != "metal":
        print(f"Aviso:Peça de {peca} dectada. Desviando  para descarte...")
        continue # Pula p restante do código abaixo vai para a próximo peça
    #Esta código só roda se a peça for de matel
    print(f"Processando peça de {peca}. Furando e polido...")
    print("fim do lote de produção.")
 #-------------------------------------------------------------------#
 #Exemplo
from time import sleep
for i in range(1,11):
    if i == 5:
        print(f"Falha ao ler o n° {i}")
        sleep(1.8)
        print("acabou")
#-----------------------------------------------------------------#
#Exercio 1 
# Tente criar um código que conte de 1 a 10, mas use o continue 
#para não imprimir o número 5 (simulando uma falha de sensor especiica no item 5).
print("simulador")
numéros = ["1","2","3","4","5","6","7","8","9","10"]
for mun in numéros:
    if mun!= "5":
        print(mun)

#-------------------------------------------#
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

  #-------------------------------------------------------#      
#Exercios 3
#soma de cargas de Energia (for)
#Uma fabrica tem 5 máquinas. Peça ao usuário (via input dentro do loop)
#o consumo em kWh de cada uma das 5 máquinas.Ao final do loop, o programa
# deve exibir o consumo total da fábrica.
total = 0
print("fábrica de carga de energia, \n")
for maquina in range(1,6):
    print(f"{maquina} °maquina")
    consumo = int(input("Digeite a qantiade de kWh de consumo, \n"))
    total += consumo
print("consumo total da fábrica", total )
#------------------------------------------------------------------------#
#indentficar de peças Defeitosas (for + if)
#percorra uma lista de medidas de peças:
#medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# o padrão de  quantidade aceita apenas peças com exatamente 50.0 ou mais 
#use um for paar ler a lista e , para cada peça , diga se ela está "Aprovado"ou "Reijeitado"

medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
for med2 in medidas:
    if med2 >= 50.0:
        print(f"Aprovado {med2}")
    if med2 <= 50.0:
        print(f"Rejeitado {med2}")
print("acabou")

#--------------------------------------------------------------------------#

#Exercício 6 - uma balança industrial está pensando em um lote de 6 
#saco de isumos.o peso idealde cada saco é 5kg, mas o sistema aceita variações 
total = 0
for sacos in range(1,7):
    print(f"{sacos}° saco de isumo:")
    pesos = int(input("Digite a quantidade de kg dp saco, pouco acima de 50kg: \n"))
    total += pesos 
print("O valor total de kg dos 6 é igual a", total)
#-------------------------------------------------------------#
#Exercios 7: Sisteas inteligente de Manutenção 
#Crie um programa que receba 2 dados: a pressões atual (float) e as horas de uso acumoladas (int) de uma tubina 
# o programa deve classificar o etadoda de máquina segundo esta hirarquia:
# crítico (Prioridade 1): se a pressão for maior que 100 ou as horas de uso forem maoir que 10.000
#Mensagem; Parada imedita:ricos de falha catastrofiaca.
#Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive).
#Mensage:Manutençaõ Agendada: pessão acima do ideal.
#Monitoramento (Ptioridade) : se as horas de uso forem entre 8.000 e 10.000
#Mensagem: aviso : maquina aproximando - se da revisão de 10k horas .
#normal1: Para qualquer outro caso que não se encaixe nos acima 
# mensagens : sistema operacional : todos os paramentros dentro da nosmalidade


