#1Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
#"Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
print("Registros de peradores")
operador = input("Digite seu nome....")
turno = input("Diite seu turno...")
print(f"Operador {operador} registro no Turno [turno]. Boa jornada!")

#--------------------------------------#
#2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
#exiba quantas peças serão produzidas em um turno de 8 horas.
print("Calculo de programação")
producao_hora = int(input("Digite a quantidade de peças produzidas em 1 hora..."))
producao_turno = producao_hora *8 
print(f" Quantidade e peças produzidas em um turno e 8 horas:{producao_turno}")

#-----------------------------------------------#
#3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
#≈ 14.5 PSI) e exiba com duas casas decimais.
print("Convenversor de Unidade")
pressao_bar = float(input("Digite a pressão em Bar..."))
pressao_psi = pressao_bar * 14.5
print(f"Pressão em PIS:{pressao_psi:.2f}")
print(f"Pressão em PIS: {pressao_psi}", round(pressao_psi, 2))
#------------------------------------#
#4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
#aritmética simples delas.
print("Inspeção de Peças")
nota1 = float(input("Digie a nota da inspeção 1 (0 a 10)"))
nota2 = float(input("Digie a nota da inspeção 1 (0 a 10)"))
nota3 = float(input("Digie a nota da inspeção 1 (0 a 10)"))
media = (nota1 + nota2 + nota3) / 3
print(f"Média de qualidade de peças: {media: .2f}")
print(f"Média de qualidade de peças:", round(media, 2))
#-------------------------------------#
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

#----------------------------------------------------#
#Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
#exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

print("Classificador de Lotes")
codigo_produto = input("Digite o código do produto ...")
if codigo_produto == "A":
    print("Alimeto")
elif codigo_produto("E"):
    print("Eletronicos")
else:
    print("Desconhecido")

#Segundo Exemplo 
print("Classificador de lotes")
codigo_produto == input("Digite o código do produto...")
if codigo_produto.startwitch("A"):
    print("Alimento")
elif codigo_produto.startswith("E"):
    print("Eletrónicos")
else:
    print("Desconhecido")

#----------------------------------------------------------#
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

#----------------------------------------------------------#
#8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
#o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
#"Processo Otimizado".

print("Cálculo de Descarte")
total_pecas = int(input("Digite o total de peças produzidas..."))
total_defetuosas = int(input("Digite o total de peças defeituosas"))
descarte_percentual = (total_defetuosas / total_pecas) * 100
if descarte_percentual > 5:
    print("Revisar Processo")
else:
    print("Processo Otimizado")
    print(f"Descarte percentual: {descarte_percentual:, 2f}%")

#----------------------------------------------------------#
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

#----------------------------------------------------------------#
#10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
#de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

print("Contagem Rgressiva")
for contagem in range(10, 0, -1):
    print(contagem)

#-----------------------------------------------------#
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
#---------------------------------------------------------------#

print("Multiplas Leitura")
temperaturas = []
for i in range(1, 6):
    temp = float(input(f"Digite a temperatura do sensor {i} em °C ..."))
    temperaturas.append(temp)
print(f"Maior temperatuara lida: {max(temperaturas):.2f}°C")

#-----------------------------------------------------#

print("Painel de Login")
senha_correta = "admin123"
tentativas = 3
while tentativas > 0:
    senha= input("Digite a senha do supervisor...")
    if senha == senha_correta:
        print("Acesso Permitido")
        break
    else:
        tentativas -= 1
        print(f"Acesso Negado, Tentativas restantes: {tentativas}")
if tentativas == 0:
    print("Painel blooqueado")

#-------------------------------------------------------#

print("Simulador de Estoque")
estoque = 100
while True:
    print("n\Menu:")
    print("1.Adicionar itens")
    print("2. Remover itens")
    print("3. Sair")
    escolha = input("Ecolha uam opção (1, 2 ou 3)....")

    if escolha == 1:
        quantidade = int(input("Digite a quantidade de itens a adicionar..."))
        estoque += quantidade
        print(f"Estoque atualizado: {estoque} itens")
    elif escolha == "2":
        quantidade = int(input("digite a quantidade de itens a remover...."))
        estoque -= quantidade
        print(f"Estoque atualizado: {estoque} itens")
        if estoque < 10:
            print("Estque Crítico ")
        elif escolha == "3":
            print("Saindo do simulador de estoque.")
            break
        else:
            print("Opção inválida: Tente novamente.")

#----------------------------------------------------------------#

print("Relatório de turno Completo")
total_pecas = 5
pecas_aprovadas = 0
for i in range (1, total_pecas + 1 ):
    diametro = float(input(f"Digite o diâmetro da peça {i} em mm..."))
    if 19.9 <= diametro <= 20.1:
        pecas_aprovadas += 1
        eficiencia = (pecas_aprovadas / total_pecas ) * 100
        print(f"Total de pecas aprovadas: {pecas_aprovadas}")
        print(f"Efici~encia do lote: {eficiencia:.2f}%")

#----------------------------------------------------------------#

