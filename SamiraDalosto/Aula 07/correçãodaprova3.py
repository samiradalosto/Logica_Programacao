#3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
#≈ 14.5 PSI) e exiba com duas casas decimais.
print("Convenversor de Unidade")
pressao_bar = float(input("Digite a pressão em Bar..."))
pressao_psi = pressao_bar * 14.5
print(f"Pressão em PIS:{pressao_psi:.2f}")
print(f"Pressão em PIS: {pressao_psi}", round(pressao_psi, 2))