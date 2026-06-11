#Use o Laço "for" (Repitiçaõ Determinadas)
#Use o "for " quando você sabe extamente 
#Quantas vazes algo deve 
#Acontecer (como ler 10 sensores ou processar uma lista de peças )
#Exemplo: Relatório de produção Diária 
#imagene que você tem uma meta de produzir 5 lote se quer numerar cada um

#Exercio
for lote in range(1,6):
    print(f"Processo lote numéro {lote}...")
    print("Quantidade verficada. [Ok]")
    print("Produção do dia finalizada!")

#Imagine que você queira armazenar 10 carros 
for carros in range(10):
    print(f"Quantidade de carros {carros}")


    #Exemplo 2
    for i in range(5):
        print(i)

    #Exemplo 3 
    peças = {"Engrenagem", "Eixo", "Rolamento", "Parafuso"}
    maquinas = ["Máquina 1", "Máquina 2"]

    for item in peças :
        print(F"Item em estoque: {item}")
        for maq in maquinas:
            print(f"Máquinas que temos {maq}")
            

#--------------------------------------------------#
#Exercicios 1
#1. Contador de produção {for}
#Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e,
#imprima :"Peça nº X processada com sucesso". No final,
#exiba "Ciclo de produção concluido"

for item in range(1, 11):
    print(f"Peça nº {item} processada com sucesso")
    
    print("Ciclo de produção concluido")
#----------------------------------------------#

#Exercício 2
# imagine a produção de frutas em uma feira; Desejo apresetar as 
#frutas banana, manga malancia, abacaxi com uma quantidade de 10 bananas, 5 mangas,
# 10 melancias e 13 abacaxi

frutas = ("banana 10", "manga 5", "malancia 10", "abacaxi 13")
for f in frutas:
    print(F"frutas: {f}")
for f in frutas:
    print(f"soma das frutas: {f}")
    total= 10 + 10 + 13+ 5
    print (total)


#--------------------------------------------------#

#Exercicios 3 
#Montar uam tabuada inicialmente pode ser usado por um valor fixo e deposi usar a pergunta

for t in range(1 , 11):
    print(f'2 * {t} =', 2 * t)
    

  
t2 = int(input("digete seu valor: \n"))
for numero in range(1,11):
    print(f"{t2} * {numero} = ", t2 * numero)


#----------------------------------------#

#Execicio04
#Repete enquanto a temperatura estiver seguro
#Inicio
temperatura = 25 
while temperatura < 48:
    print(f"temparatura atual: {temperatura}""C. Sistema operando...") 
    temperatura += 3 #simulando o aqucimento da máquina 
    print('ALERTA! temperatura atingiu o limte. desligando motor...')
    

#------------------------------#
#Exercicio 4
#Criar um menu de opções com 4 itens ex: Eseolher Series apresente sua escolha 
# de sertes das outras três.
#Qualquer opçaõ diferente sair do menu

opção = ""

while opção !="sair":
    opção = input("Digite a leitura do sensor ou 'sair' par fechar:").lower()
    if opção != "sair":
        print(f"Dado '{opção}' registrado mo banco de dados")
print("Sistema encerrado.")  


#-----------------------------#

