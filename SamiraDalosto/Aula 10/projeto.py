#projeto Cancela Automática
#Criar um algoritimo que congiga gerenciar entrada e saída de veículos
#Inserindo valores por hora permanecida
#A forma de entreda e saída deve ser específicada e permitir o usuário
#Inserir os dados necessarios para registrode vículos
 
#Passos 
#1 - pressionar o botão, imprimiu um ticket
#Calcular o tempo de permanecia 
#Pagar o ticket 
#Devolver ticket na saída
#Liberar e fechar cancela

#2 - Acesso por TAGs (Sem parar, connect Car...)
#Calcular tempo de permanecia 
#Gerar pagamento em fatura 
#Liberar e fechar cancela 

#3 - Erros 
#Verificar sinal de transmissão da TAG 
#Verifiacar acesso por ticket ou tag ao mesmo tempo 
#Perdeu ticket (levantar irformações )
#Problemas com cancela 

print("Bem vindo ao Meu Shoopping da Samira ")
print("1 - acesso com o ticket")
print("2 - acesso por TAG")
forma_acesso = input("Digite a forma de acesso - TAG ou Ticket? \n")
ct = "Cancela está com problema"
pt = "Perdeu o ticket"
if forma_acesso == "1":  
    print("Imprimir o ticket")

    he = float(input("Horario de entrada, \n"))
    hs = i= float(input("Horario de saída, \n"))
    tempo = hs - he
    print("A contagem de horas foi", hs - he )
    print( tempo * 10)
    print("Total a pagar \n",round(tempo,2) * 10)
    print("Devolver o ticket na saída")
    print("Liberar e fechar a cancela")
    if pt == "Perdeu o ticket":
        pt = input("perdeu o ticket? \n")
        print("perdeu ticket", pt )
        print("procurar informações da placa ")
        print(str(input("nome \n")))
        print(str(input("placa do carro \n")))
        print(str(input("CPF \n")))
        print(str("informações concluídas"))
        print("Pagar, multa de 50 reais")
        print("Tenha uma boa viagem, até logo")

    else:
          print("Não perdeu continue o processo")
          print("Tenha uma boa viagem")
elif forma_acesso == "2":
        print("Entrada com TAG")
        print("Liberar e fechar a cancela ")
        he = int(input("Horario de entrada, \n"))
        hs = int(input("Horario de saída, \n"))
        tempo = hs - he
        print("A contagem de horas foi", hs - he )
        print( tempo * 10)
        print("Total a pagar \n",tempo * 10)
        print("Liberar e fechar a cancela")
        print("Tenha uma boa viagem, até logo")
elif ct == "cancela não está funcionano":
        ct = ("Cancela está com problema")
        print("problema com cancela")


