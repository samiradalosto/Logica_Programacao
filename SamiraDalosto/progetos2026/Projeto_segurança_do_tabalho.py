#Critérios de Avaliação
# Capacidades Técnicas
# 1. Utilizar tomada de decisão para elaboração do algoritmo
# 2. Utilizar estruturas condicionais para executar instruções com base em uma
# condição
# 3. Criar estruturas de repetição para executar um conjunto de instruções várias
# vezes
# 4. Aplicar operadores lógicos para avaliar e combinar condições booleanas
# 5. Utilizar lógica de programação para a resolução de problemas
# Situação de Aprendizagem – Atividade Individual

# Projeto Brigada: Sistema de Gestão de Segurança do Trabalho (SESMT)

# Contexto
# O Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho
# (SESMT) precisa automatizar o controle de treinamentos obrigatórios (como CIPA,
# Brigada de Incêndio e NR-35) e a entrega de Equipamentos de Proteção Individual (EPIs).
# Objetivo
# Desenvolva um programa em Python que gerencie o status de conformidade dos
# funcionários de uma empresa.
# Requisitos do Programa
# 1. Cadastro de Funcionários:
# ○ Armazene o nome, setor e o status dos treinamentos (NR-10, NR-35 e
# Brigada).

# 2. Verificação de EPI (NR-6):
# ○ O sistema deve receber o setor do funcionário.
# ○ Se o setor for "Elétrica", liste a obrigatoriedade de luvas de alta tensão e
# botas dielétricas.
# ○ Se o setor for "Trabalho em Altura", liste o cinturão de segurança e
# talabarte.
# 3. Alerta de Reciclagem:
# ○ Crie uma função que receba o ano do último treinamento da Brigada de
# Incêndio.
# ○ Se o treinamento tiver mais de 2 anos, exiba a mensagem: "Treinamento
# Vencido! Encaminhar para reciclagem."
# ○ Caso contrário, exiba: "Treinamento Válido."

# # Projeto Brigada: Sistema de Gestão de Segurança do Trabalho (SESMT)
#print("Projeto brigada de segurança ")


# def verificar_reciclagem(ano_treinamento):
#     ano_atual = 2026
#     tempo_decorrido = ano_atual - ano_treinamento
    
#     print("Alerta brigada para reciclagem")
#     if tempo_decorrido > 2:
#         print(" Treinamento Vencido! Encaminhar para reciclagem.")
#     else:
#         print(" Treinamento Válido.")

# # Loop principal para Cadastro de Funcionários (Requisito 1)
# while True:
#     print("\n" + "="*30)
#     print("Novo cadastro")
#     print("="*30)
    
#     nome = input("Digite o nome do funcionário (ou 'sair' para encerrar): \n")
    
#     # Condição de parada do programa
#     if nome.lower() == 'sair':
#         print("\nSistema encerrado. Obrigado!")
#         break
        
#     # Apresentando as opções de setores de forma organizada
#     print("\nSelecione o setor do funcionário:")
#     print("1 - Desenvolvimento de sistemas")
#     print("2 - Logística")
#     print("3 - Elétrica")
#     print("4 - Trabalho em Altura")
    
#     setor_opcao = input("Digite o número correspondente ao setor: \n")
   
#     print("Verificação de IPI ")
    
#     if setor_opcao == "1":
#         print("Setor: Desenvolvimento de Sistemas")
#         print("EPIs Obrigatórios: Utilizar apenas EPIs básicos do ambiente de escritório.")
        
#     elif setor_opcao == "2":
#         print("Setor: Logística")
#         print("EPIs Obrigatórios: Bota com biqueira de aço e colete refletivo.")
        
#     elif setor_opcao == "3":
#         print("Setor: Elétrica")
#         print("EPIs Obrigatórios: Luvas de alta tensão e botas dielétricas.")
        
#     elif setor_opcao == "4":
#         print("Setor: Trabalho em Altura")
#         print("EPIs Obrigatórios: Cinturão de segurança e talabarte.")
        
#     else:
#         print("Opção de setor inválida! Verifique os EPIs padrão da empresa.")

#     # Pergunta o ano para a função de reciclagem
#     try:
#         ano_ultimo_treinamento = int(input("\nDigite o ano do último treinamento da Brigada: \n"))
#        
#         verificar_reciclagem(ano_ultimo_treinamento)
#     except ValueError:
#         print(" Ano inválido! Digite um número com 4 dígitos (ex: 2024).")

#-----------------------------------------------------#
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 

def processar_sesmt():
    nome = entry_nome.get().strip()
    setor = combo_setor.get()
    ano_texto = entry_ano.get().strip()
    
  
    if not nome or not setor or not ano_texto:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos antes de calcular!")
        return
        
    try:
        ano_treinamento = int(ano_texto)
    except ValueError:
        messagebox.showerror("Erro de Digitação", "Por favor, digite um ano válido com 4 dígitos (ex: 2024).")
        return


    if setor == "Elétrica":
        epis = "• Luvas de alta tensão\n• Botas dielétricas"
    elif setor == "lógistica":
        epis = "• Utilizar apenas EPIs básicos do ambiente."
    elif setor == "Mecânica":
        epis = "• Óculos de proteção\n• Luvas de raspa"
    else: setor == "Desenvolvimento de sistemas"
    epis = "• Utilizar apenas EPIs básicos do ambiente."

   
    ano_atual = 2026
    tempo_decorrido = ano_atual - ano_treinamento
    
    if tempo_decorrido > 2:
        status_reciclagem = "Treinamento Vencido! Encaminhar para reciclagem."
        cor_reciclagem = "#9C33FF" # roxo para alerta
    else:
        status_reciclagem = "✅ Treinamento Válido."
        cor_reciclagem = "#5BE3F5" # azul escuro para válido


    lbl_resultado_nome.config(text=f"Funcionário: {nome}")
    lbl_resultado_epi.config(text=f"EPIs Obrigatórios:\n{epis}")
    lbl_resultado_reciclagem.config(text=status_reciclagem, fg=cor_reciclagem)

janela = tk.Tk()
janela.title("Gestão de Segurança do Trabalho")
janela.configure(bg="#FF69B4") 
janela.geometry("450x550")


lbl_titulo = tk.Label(janela, text="Projeto Brigada -", bg="#C71585", fg="white", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=15, fill="x")


lbl_nome = tk.Label(janela, text="Nome do Funcionário:", bg="#FF69B4", fg="black", font=("Arial", 11, "bold"))
lbl_nome.pack(pady=2)
entry_nome = tk.Entry(janela, font=("Arial", 11), width=30)
entry_nome.pack(pady=5)


lbl_setor = tk.Label(janela, text="Setor do Funcionário:", bg="#FF69B4", fg="black", font=("Arial", 11, "bold"))
lbl_setor.pack(pady=2)
combo_setor = ttk.Combobox(janela, font=("Arial", 10), state="readonly", width=28)
combo_setor['values'] = ("Desenvolvimento de Sistemas", "Logística", "Elétrica", "Mecânica", "Trabalho em alutura" )
combo_setor.pack(pady=5)

lbl_ano = tk.Label(janela, text="Ano do último treinamento da Brigada:", bg="#FF69B4", fg="black", font=("Arial", 11, "bold"))
lbl_ano.pack(pady=2)
entry_ano = tk.Entry(janela, font=("Arial", 11), width=10)
entry_ano.pack(pady=5)

btn_calcular = tk.Button(janela, text="Verificar Conformidade", font=("Arial", 12, "bold"), bg="#FF1493", fg="white", command=processar_sesmt)
btn_calcular.pack(pady=15)


lbl_resultado_nome = tk.Label(janela, text="", bg="#FF69B4", font=("Arial", 11, "bold"))
lbl_resultado_nome.pack(pady=2)

lbl_resultado_epi = tk.Label(janela, text="", bg="#FF69B4", font=("Arial", 11))
lbl_resultado_epi.pack(pady=5)

lbl_resultado_reciclagem = tk.Label(janela, text="", bg="#FF69B4", font=("Arial", 11, "bold"))
lbl_resultado_reciclagem.pack(pady=5)

btn_close = tk.Button(janela, text="Fechar Sistema", font=("Arial", 11, "bold"), bg="#f74780", fg="white", command=janela.quit)
btn_close.pack(side="bottom", pady=15)
def mostrar_mensagem():
    messagebox.showinfo("lista de funcionário de treinamento válido")
janela.mainloop()