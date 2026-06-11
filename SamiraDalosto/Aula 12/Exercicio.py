#Exercicio; Crie uma interace gráfica que cacule a média de três notas digitadas pelo usuário.
#A interface deve conter campos para noats digitadas pelo usuario inserir as notas e um botão
#para calcular a média, Ao clicar no botão, a média deve ser exibida e, uma mensagem 
import tkinter as tk
from tkinter import messagebox

def calcular_media():
    try:
        # Pegando as notas dos campos de texto
        nota1 = float(ent_nota1.get())
        nota2 = float(ent_nota2.get())
        nota3 = float(ent_nota3.get())
        
        # Calculando a média
        media = (nota1 + nota2 + nota3) / 3
        
        # Verificando a situação
        if media >= 7.0:
            status = "Aprovado! 😘 "
            cor_status = "green"
        else:
            status = "Reprovado. 😱"
            cor_status = "red"
            
        # Atualizando a tela com as informações e as cores dinâmicas
        label_resultado.config(text=f"Média: {media:.2f}") 
        label_mensagem.config(text=f"Status: {status}", fg=cor_status) 
        
    except ValueError:
        # Caso o usuário digite letras ou deixe em branco, exibe um aviso
        messagebox.showerror("Erro de Digitação", "Por favor, digite apenas números válidos usando pontos (ex: 7.5).")

# Criando a janela principal
janela = tk.Tk()
janela.title("Média Escolar")
janela.geometry("350x400") # Aumentei um pouco para caber os elementos confortavelmente

# Campo da 1ª Nota
label_nota1 = tk.Label(janela, text="Digite a 1ª Nota:", font=("Arial", 10), bg="#FF80DD")
label_nota1.pack(pady=5)
ent_nota1 = tk.Entry(janela, font=("Arial", 10))
ent_nota1.pack()

# Campo da 2ª Nota
label_nota2 = tk.Label(janela, text="Digite a 2ª Nota:", font=("Arial", 10), bg="#FF84C6")
label_nota2.pack(pady=5)
ent_nota2 = tk.Entry(janela, font=("Arial", 10))
ent_nota2.pack()

# Campo da 3ª Nota
label_nota3 = tk.Label(janela, text="Digite a 3ª Nota:", font=("Arial", 10), bg="#FF58AE")
label_nota3.pack(pady=5)
ent_nota3 = tk.Entry(janela, font=("Arial", 10))
ent_nota3.pack()

# Botão de Calcular
botao_calcular = tk.Button(janela, text="Calcular Média", font=("Arial", 11, "bold"), bg="#FF2C97", command=calcular_media)
botao_calcular.pack(pady=15)

# Labels de Resultado
label_resultado = tk.Label(janela, text="Média: --", font=("Arial", 12, "bold"), bg="#EF007E")
label_resultado.pack(pady=5)

label_mensagem = tk.Label(janela, text="Resultado: --", font=("Arial", 12, "bold"), bg="#F2F5F7")
label_mensagem.pack(pady=10) # CORRIGIDO: Agora empacota o label_mensagem correto

# Mantém a janela aberta
janela.mainloop()