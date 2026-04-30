#Exercicio 6: Desligar o pc (comando para o Windows)
with open("desliga.bat", "w") as desligar:
    desligar.write("shutdown -s -t 3600 -c / Desligamento do programa para daqui a 1 hora, Salvar seu trabalho!\"")
#-s comando para desligar 
#-t tempo definido
#-a cancelar desligamento 
with open("desliga.bat", "r") as desligar:
    conteudo = desligar.read()
    print(conteudo)
    
