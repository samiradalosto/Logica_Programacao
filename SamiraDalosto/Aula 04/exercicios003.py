#Exercios 3 
#Criar um algoritmo para aplicação de desconto para produtos como sapatos aplicar 10%, para produtos como roupas 5% e perfumes 2%
print("Algoritmo de desconto")
print("1 - sapatos")
print("2 - roupas")
print("3 - perfumes")
s1 = int (input("Digite sua escolha: \n"))
if s1 == 1:
    print("sapato aplicar 10%,")
    a1 = int(input("Digite o valor: \n"))
    s2 =  print( input("Quanto produtos você ira querer"))
    print("o desconto: \n", a1 * 10 / 100)
    print("O valor total da conta: \n", a1 -(a1 * 10 / 100))
elif s1 == 2:
     print("roupas aplicar 5%,") 
     a1 = int(input("Digite o valor: \n"))
     s2 =  print( input("Quanto produtos você ira querer"))
     print("o desconto: \n", a1 * 5 / 100)
     print("O valor total da conta: \n", a1 -(a1 * 5 / 100))
elif s1 == 3:
    print("perfumes aplicar 2%,")
    a1 = int(input("Digite o valor: \n"))
    s2 =  print( input("Quanto produtos você ira querer"))
    print("o desconto: \n", a1 * 2 / 100)
    print("O valor total da conta: \n", a1 -(a1 * 2 / 100))
    




print("Obrigado por comprar em nossa loja")

    

