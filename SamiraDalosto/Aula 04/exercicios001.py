#exercio 1
#Criar um algoritmo para calcular a mídia e com base em notas, podemos inserir duas notas e apresente a media porém  
# a nota base da 50 é aprovado e menor que essse valor será reprovado 
nota1 = int(input("digite a primeira nota: \n"))
nota2 = int(input("digite a primeira nota: \n"))
média = nota1 + nota2 / 2

if média >= 50:
    print ("Aprovado")
else:
    print("Reprovado")
    