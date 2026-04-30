materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
for peca in materiais:
    if peca != "metal":
        print(f"Aviso:Peça de {peca} dectada. Desviando  para descarte...")
        continue # Pula p restante do código abaixo vai para a próximo peça
    #Esta código só roda se a peça for de matel
    print(f"Processando peça de {peca}. Furando e polido...")
    print("fim do lote de produção.")