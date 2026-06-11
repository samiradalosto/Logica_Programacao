#Clean Code - Aula 8 
#Para que usar?
#Como usar?
print("Clean Code - Aula 8")
aula = 8 
print(f"Estamos na aula {aula} de Clean Code")

#Manipulação de arquivos de texto
texto = "Python"
print(texto.strip().upper()) #PHITHON
print(texto.strip().lower())
print(texto.strip().capitalize()) #Python
print(texto.strip().title())
print(texto.strip().replace("","_"))
print(texto.strip().split())

#Escrevendo 
with open("notas.txt", "w") as arquivo:
   arquivo.write("Estudae Python hoje!")
   arquivo.write("\n ler sobre Clean code.")

#Lendo 
with open("notas.txt", "r") as arquivo:
   conteudo = arquivo.red()
   print(conteudo)

 #Execução de comandos do sistema 
import os #immporta o módulo os para interagir com o sistemas operacional

#Onde estou?
print(os.getcwd())
#Listar arquivos na pasta 
print(os.listdir())

#Outros comandos úteis:
os.mkdir("nova_pasta")
# # Rename pasta 
os.rename("nova_pasta", "pasta_renomeada")
## Excluir pasta 
os.rmdir("pasta_renomeada")

#Exemplo de dicionario 
#Criar um dicionario com informações sobre uma pessoa e acessa um valor usando uma chave
pessoa = {
   "nome": "Alice",
   "idade": 30,
   "cidade": "São Paulo",
   "profissão" : "Engenheira"

}

pessoa2 = {
   "nome": "Samira",
   "idade": 16,
   "cidade": "São Paulo",
   "profissão": "Estudante",
}
print(pessoa["nome"], pessoa["idade"])

#------------------------------------------------------------------------------------#
#Exércicio 1:
#Crie um script que mostre o caminho da pasta atual.

import os 
print(os.getcwd())

#----------------------------------------------------------#

#Execicio 2
#Liste os arquivos da pasta atual 
import os
print(os.listdir())
#---------------------------------#

#Crie uam pasta chamada "projetos"e depois renomeie para 
#"meus_projetos".Por fim,exclua a pasta 

import os 
os.mkdir("nova_pasta")
os.rename("nova_pasta", "meus_projetos")
os.rmdir("meus_projetos")

#-------------------------------------------------#

#Exercicio 6: Desligar o pc (comando para o Windows)
with open("desliga.bat", "w") as desligar:
    desligar.write("shutdown -s -t 3600 -c / Desligamento do programa para daqui a 1 hora, Salvar seu trabalho!\"")
#-s comando para desligar 
#-t tempo definido
#-a cancelar desligamento 
with open("desliga.bat", "r") as desligar:
    conteudo = desligar.read()
    print(conteudo)
    
#----------------------------------------------------------------#
#Exercicio 7:
#Criar um arquivo de backup
#Escreva um script que crie um arquivo  "nota.txt" e escrever no novo arquivos

import os 
with open("notas.txt", "r") as notas:
     conteudo = notas.read()
with open("notas_backup.txt", "w") as backup:
    backup.write(conteudo)
print("arquivo de backup realizado")

#Exemplo 2: Criar um script de limpeza de arquivos 
#Escreva um script que liste os arquivos de uma pasta e exclua os arquivos
#com extensão ".tmp". Oscrip deve exibir uma mensagem para cada arquivo excluido.
pasta = os.listdir()
for arquivo in pasta:
    if arquivo.endswiht(".txt"):
        os.remove(arquivo)
        print(f"Arquivo {arquivo} excluido")
        print("Limpeza de arquivos concluida.")

#---------------------------------------------------------#

#Exercicio 8
#Criar um script de monetoramento de temperatura
#Escreva um script qie monitore a emperatura de um motor. O script
# monitore a temperatura de um motor.O script deve ler a temperatura de 
# um arquivo "temperatura.txt"e exibrir uma mensagem de alerta se a temperatura estiver acima de 70°C.

with open("temperatura.txt", "w") as motor:
   motor.write("Monitore a temperaturade um motor")
   motor.write("\n ler sobre Clean code.")

#----------------------------------------------------------#
