#Exxplicação de def: A palavra-chave "def" é usada para definir uma função em Python.
#Ums função é um bloco de código reutilizavel que realiza uma tarefa específica.
# Return: A palavra-chave "return" é usada para finalizar a execução 
# De  uma função e retonar um valor para o local onde a função foi chamada.
# O valor retornado pode ser usado porteriormente no código.

def nome ():
    nome = input("Digite o seu nome: \n")
    return nome
print(f"Olá, {nome()}")

def valores():
    print("Digite três valores:")
    a = int(input("Digite o primeiro valor:" ))
    b = int( input("Digite o segundo valor" ))
    c = int(input("Digite o terceiro valor " ))
    return a, b, c 
    
print(f"O maior valor é {max(valores())}!")
#Reutilizadando as funções 
nome()
valores()