#exercicio 1:
#Ercreva um programa que solicite ao usuario um número inteiro e calcule a média de uma lista de números 
#Oprograma deve tratar os seguintes erros:
#- ValueError:se o usuário digitar um valor que não seja um número interrior .

try:
    n1 = int(input('digite sua primeira nota \n'))
    n2 = int(input('Digite sua segunda  nota \n'))
    n3 = int (input('digite sua terceira nota \n'))
    s2 =(n1 + n2 + n3  )/3
    print("O resultado do calculo é: \n", s2)
except ValueError:
    print("Error:Entrada inválida. por favor, digite um número inteiro.") 

