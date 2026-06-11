# Revisão Tkinter 

import tkinter as tk
from tkinter import messagebox, ttk

# 0 - Etapa Janela
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("400x400")
janela.configure(bg="#FFB6C1")

#1- Etapa componentes
#print = Label
#imput = Entry

#DEf funções em bloco 
def cadastrar_usario():
    #get
    nome_usuario = ent_nome_usuario.get()
    curso_usuario = ent_digite_seu_curso.get()
    nome_escola = cmb_nome_escola.get()

    if nome_usuario =="" and curso_usuario == "" and nome_escola == "":
        messagebox.showinfo("Bem-Vindo", "Digite seu nome, seu curso e escolha sua escola ")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}! seu curso é {curso_usuario} e sua escolha é {nome_escola}")

lbl_nome_usuario = tk.Label(janela, text="Digite seu nome.:", font=("Arial", 14), fg="pink")
lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)
#Entrys = Caixa de texto antigo 
ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), width=10)
ent_nome_usuario.grid(row=0, column=1, pady=10, padx=10)

lbl_digite_seu_curso = tk.Label(janela, text= "Digite seu curso.:", font=("Arial", 14), fg="pink")
lbl_digite_seu_curso.grid(row=1, column=0, pady=10, padx=10)
ent_digite_seu_curso = tk.Entry(janela, font=("Arial", 14), width=10)
ent_digite_seu_curso.grid(row=1, column=1, pady=10, padx=10)

#ComboBox = Caixa de seleção 
lbl_escolha_sua_escola = tk.Label(janela, text= "Esolha sua escola.:", font=("Arial", 14), fg="pink")
lbl_escolha_sua_escola.grid(row=2, column=0, pady=10, padx=10) 
cmb_nome_escola = ttk.Combobox(janela, values=("SESI400","SESI5"))
cmb_nome_escola.grid(row=2, column=1, pady=10,padx=10)
#Botão
btn_realizar_cadastro = tk.Button(janela, text = "Cadastrar", font =("Arial", 14), fg ="pink", command=cadastrar_usario)
btn_realizar_cadastro.grid(row= 3, column=1, pady=10, padx=10)
btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), fg="pink", command=janela.destroy)
btn_fechar_janela.grid(row=6, column=1, pady=10, padx=10)
#4-Etapa Componente 
janela.mainloop()