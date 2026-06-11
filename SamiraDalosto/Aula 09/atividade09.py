#Tratamento de erros com python
#Erros comuns:
#-ZeroDivisionError:divisão por zero
#-IndexError:acesso a índice fora do limite 
#-KeyError:acesso a vhave inexistente em dicionário

#Exemplo de tratamento de erros 
#print("Exemplo de tratamento de erros")
try:
    num1 = int(input("Digite o primeiro número, \n"))
    num2 = int(input("Digite o segundo número, \n"))
    resultado = num1 /num2 
    print(f"O resultado da divisão é: {resultado: .2f}")

except  ZeroDivisionError:
    print("Error:Não é porrivel dividir por zero.")   


except ValueError:
    print("Error:Entratada inválida. por favor, digite um número inteiro.") 

except Exception as e:
    print(f"Ocorreu um error inesperado: {e}")
# #............................................................................#

if num1 > 100:
    print("O número digitado é maior que 100 ")
    for i in range(1, 6):
        print(f"{num1} x {i} = {num1 * i}")
        if num1 * i > 1000:
            print("Oresultado da multiplicação é maior que 1000.")
            try:
                pass
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
            else:
                print("O número digitado é menor ou igual a 100.")

#-------------------------------------------------------------------------------------------------#

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
#---------------------------------------------------#
#Exercicios 2:
#Escreva um programa que solicite ao usuário uma lista de palavras e conte quantas vezes cada palavra aparece na lista 
#O programa deve tratar os seguinte erros:
# - valueError: se o usuário digitar um valor que não seja um string
# try:

#     for i in range(5):
#         lista = 0 
#         entrada = input(f"Digite {i+1}° palavra, \n")

# except ValueError:
#     print("ValueError: Você digitou aluguma palavra errada.")
try:
    palavras = input("Digite uma lista de palavras separadas por espaço, \n").split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
             contagem[palavra] += 1 
        else:
            contagem[palavra] = 1 
    print("Contagem de palavra:")
    for palavra, contagem in contagem.items():
        print(f"{palavra}: {contagem}")
except ValueError:
    print("Error: Entrada invalida. por favor, digite uma lista de palavras separadas posr espaço")

#---------------------------------------------------------#
#Exercicio 3:
# Escrever um programa mais simples com testes de tratamento de erros
# como exemplo, solicitar ao usuario um número. O programa deve tratar os seguintes erros 
# - Valuerror:se o usuário digitar um valor que não seja um número.
# - ZeroDivisionError: se o usuário digitar zero como divisor.
