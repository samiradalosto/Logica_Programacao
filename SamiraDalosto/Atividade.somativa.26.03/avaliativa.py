#1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
#"Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
print("Registros de peradores")
operador = input("Digite seu nome....")
turno = input("Diite seu turno...")
print(f"Operador {operador} registro no Turno [turno]. Boa jornada!")

#.........................................................................#
#2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
#exiba quantas peças serão produzidas em um turno de 8 horas.

print("Calculo de prdução")
print(input("Qual foi a quantidade de peças produzidas 1 hora:"))
print("exiba quantas peças serão produzidas em um turno de 8 horas")
total = 3 * 8
print('O seu resultado é: \n', total )
print("o valor foi : poduzido em uma hora * produzida em 8 horas ")

#............................................................................#
#3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
#≈ 14.5 PSI) e exiba com duas casas decimais.

print("O sistema de um bar PSI")
i = int(input("Escolha a pressão o bar PSI \n"))
psi = 14.5
total = i * psi 
print("valor da pressão:", i * psi )
#...........................................................................#
#4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
#aritmética simples delas.
nota1 = int(input("digite a primeira nota: \n"))
nota2 = int(input("digite a primeira nota: \n"))
nota3 = int(input("digie a primeira nota: \n ")) 
média = (nota1 + nota2 + nota3) /3 
print("A média foi de:", média )
#..............................................................................#
#5. Termostato Inteligente: Peça a temperatura de um motor.
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
#.............................................................................#
#Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
#exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

print("Classiicaodr de Lotes")
l1 = input("Digite o códdigo de produto:\n")
if l1 == "A":
    print("Alimentos")
elif l1 == "E":
   print("Eletronicos")
else:
   print("Desconhecido")
#....................................................................................#
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
 #....................................................................#
#8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
#o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
#"Processo Otimizado".
print("Calculo de dercarte")
ps = int(input("digite o total de peças prontas; \n"))
paa = int(input("Digite qual é o total de peças defeituosas?; \n"))
defeituosas = ps/ paa* 0.05 /100
if paa > defeituosas:
     print("Revisar o processo")
else: 
     print("Processo otimizado ")
 #...........................................................................#
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
#.......................................................................#
#10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
#de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".
for i in range(10, 0 ,-1 ):
    print(1)
    print("Prensa Ativada")
#.......................................................................#
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
#.................................................................................#
#12.Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
#Ao final, mostre qual foi a maior temperatura lida.
print("Multiplas Leitura")
temperaturas = []
for i in range(1, 6):
    temp = float(input(f"Digite a temperatura do sensor {i} em °C ..."))
    temperaturas.append(temp)
print(f"Maior temperatuara lida: {max(temperaturas):.2f}°C")

#13. Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
#Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
#Se esgotar, exiba "Painel Bloqueado".
print("Painel de Login")
senha = 0
while True <3:
    senha = input("digitea senha")
    if senha == "sami23":
        print("aceite aprovado")
        senha -+ 1
        if senha == 3:
            print("bloquear")
#....................................................................#