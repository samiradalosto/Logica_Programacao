#Exercicos 4
#Criar um algoritimo para calcular a média com base em notas, podemso inserir duas notas e apresente a média 
#porém a nota 0 a 100 para ser aprovadpo será acima de 70 e mennor que 50 essse valor será reprovado 
#porém vamos acrescetar uma nova condição que entre 50 a 70 resuperação 
print("Algoritimo pera calcular a média ")
n1 = int(input("Digite a primeira nota :\n"))
n2 = int(input("Digite a segundo nota :\n"))
md = (n1 + n2) /2
if  md > 70:
    print("aprovado")
elif md >=50:
     print("Reuperação")
elif md <= 50:
     print("reprovado")
