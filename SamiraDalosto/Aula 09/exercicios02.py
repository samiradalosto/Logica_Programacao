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