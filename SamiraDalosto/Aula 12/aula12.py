#Tkinter
#Componetes Widegets
#tk:Tk() #Janela
#lb - label() #Rótulo
#bt - Button() #Botão 
#et - Entry()  #Caixa de texto 

import tkinter as tk
from tkinter import messagebox

# 1 - Criar a janela principal
janela = tk.Tk()
janela.title("Minha primeira janela Gui") # Título na jenela 
janela.configure(bg= "#FF69B4")
janela.geometry("400x200") #Largura e altura 

#2. Criar a função do botão (evento)
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão")

#3. Criar os componetes 
lbl_titulo = tk.Label(janela, text="Bem vindo a nossa aula de Tkinder",bg="#C71585", font=("Arial", 14, "bold"))
btn_clique = tk.Button(janela,text="Clique Aqui", font=("Arial", 11), bg="#FF1493", fg="white", command=mostrar_mensagem)
btn_close = tk.Button(janela, text="Fechar", font=("Arial", 14, "bold"), bg="#f74780", fg="white", command=mostrar_mensagem)
#4. Posicionar os componentes 
lbl_titulo.pack(pady=20)# 'pody' adiciona um espaçamento vertical 
btn_clique.pack(pady=10)
btn_close.pack(pady=10)

#5 - Rodar a loop interface
janela.mainloop()
