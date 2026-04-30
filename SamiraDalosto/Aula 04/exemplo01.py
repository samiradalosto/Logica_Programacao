# Conteúdo sobre logica
# elif: "Senão, se" (usado para mutilas funções)
# elise: "Senão" (executa se nenhuma das anteriores for verdadeiras).
print ("Expressões lógicas")
idade = int (input("Digite sua idade \n"))

if idade >= 18: 
    print("Você é maior de idade \n")
    print("Pode tirar carta de motorista")
elif idade >=16:
    print("Você ainda não é maior de idade, mas já pode votar. ")
else:
    print("Você é menor de idade.")
