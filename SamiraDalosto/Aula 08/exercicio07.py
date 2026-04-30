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