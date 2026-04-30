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