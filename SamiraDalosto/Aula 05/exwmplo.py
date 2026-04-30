opção = ""

while opção !="sair":
    opção = input("Digite a leitura do sensor ou 'sair' par fechar:").lower()
    if opção != "sair":
        print(f"Dado '{opção}' registrado mo banco de dados")
print("Sistema encerrado.")    