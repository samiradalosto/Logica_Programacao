# indentficar de peças Defeitosas (for + if)
#percorra uma lista de medidas de peças:
#medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# o padrão de  quantidade aceita apenas peças com exatamente 50.0 ou mais 
#use um for paar ler a lista e , para cada peça , diga se ela está "Aprovado"ou "Reijeitado"

medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
for med2 in medidas:
    if med2 >= 50.0:
        print(f"Aprovado {med2}")
    if med2 <= 50.0:
        print(f"Rejeitado {med2}")
print("acabou")