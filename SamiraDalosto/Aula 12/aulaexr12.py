import tkinter as tk 
from tkinter import messagebox
def saudar_usuario():
    #_get() serve para busacr o texto que vamos digitar
    nome = campo_nome.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Por favor, dgitar seu nome! ")
    else:
        messagebox.showinfo("Saudades Alunos", f"Olá , {nome}! Sejá bem vindo, ao mundo das interfaces gráficas")

#Configurações da janela 
app = tk.Tk()
app.title("Exemplo 1")
app.geometry("350x200")

#componetes da janela 
lbl_instrucao = tk.Label(app, text="Digite seu nome abaixo: \n" )
lbl_instrucao.pack(pady=10)

campo_nome = tk.Entry(app,font=("Arial", 12,))
campo_nome.pack(pady=5)

btn_enviar = tk.Button(app, text="Enviar", command=saudar_usuario)
btn_enviar.pack(pady=15)

app.mainloop()