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
