#Exercicios 04 
#Cie um arquivo chamado "log.txt" e escreva a mensagem "log0de atividade".Depois, leia o conteúdo do arquivo e exiba na tela 
with open("log.txt", "W") as arquivo:
    arquivo.write("Log de atividades")
with open("log.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
