#13.Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
#Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
#Se esgotar, exiba "Painel Bloqueado".
print("Painel de Login")
senha = 0
while True <3:
    senha = input("digitea senha")
    if senha == "sami23":
        print("aceite aprovado")
        senha -+ 1
        if senha == 3:
            print("bloquear")