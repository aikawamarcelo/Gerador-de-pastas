
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
#root.geometry("500x540+0+0")
root.title("Gerador de Pastas")
root.configure(background="lightgray")
#root.resizable(False, False)
root.resizable(True, False)

import tkinter as tk

def center_window(window, width, height):
    # Obtém a largura e altura da tela
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcula a posição X e Y para centralização
    # (largura/altura da tela - largura/altura da janela) / 2
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Define a geometria da janela (largura x altura + posição X + posição Y)
    window.geometry(f'{width}x{height}+{x}+{y}')

# --- Exemplo de uso ---


# Define as dimensões desejadas para a janela
window_width = 500
window_height = 540

# Centraliza a janela
center_window(root, window_width, window_height)

imagem = Image.open("pasta.ico")  # Substitua "icone.png" pelo caminho da sua imagem
photo_image = ImageTk.PhotoImage(imagem)

root.iconphoto(True, photo_image)

def Gerar_Pasta():
    import os

    # Define o número de pastas a serem criadas

    numero_de_pastas = (entry2.get())

    # Define o nome base da pasta

    nome_base = entry1.get()

    if (entry2.get() == "" or entry2.get() == "0"):
        messagebox.showwarning("Warning", "Digite um número para as pastas!")
        #print("Digite um número para as pastas")

    elif(entry2.get().isnumeric()):
    # Cria as pastas em um loop
     if int(numero_de_pastas) >= 1:
        for i in range(1, int(numero_de_pastas) + 1):

          # Constrói o nome completo da pasta

            nome_da_pasta = f"Pastas Criadas/ {nome_base} {i}"

        # Verifica se a pasta já existe e a cria se não existir

            if not os.path.exists(nome_da_pasta):

                  os.makedirs(nome_da_pasta)
                  #print(f"Pasta '{nome_da_pasta}' criada.")


            else:
                      messagebox.showwarning("Warning", f"Pasta {nome_base} {i} já existe!")
                      #print(f"Pasta '{nome_da_pasta}' já existe")
     


label3 = Label( text="Gerador de Pastas", font=("verdana", 30, "bold"), bg='lightgray')
label3.place(relx=0.07, rely=0.02,relwidth=0.85, relheight=0.1)

botao1 = Button( text="Gerar Pasta", bg='gray35', fg="white", font=("verdana", 12, "bold"),command=Gerar_Pasta)
botao1.place(relx=0.32, rely=0.80, relwidth=0.30, relheight=0.15)

label1 = Label( text="Nome da Pasta:", font=("verdana", 11, "bold"), bg='gray70')
label1.place(relx=0.33, rely=0.16,relwidth=0.30, relheight=0.1)

entry1=Entry( font=('verdana', 11, 'bold'))
entry1.place(relx=0.19, rely=0.33,relwidth=0.60, relheight=0.1)

label2 = Label( text="Número da Pasta:", font=("verdana", 11, "bold"), bg='gray70')
label2.place(relx=0.32, rely=0.49,relwidth=0.32, relheight=0.1)

entry2=Entry( font=('verdana', 11, 'bold'))
entry2.place(relx=0.40, rely=0.65,relwidth=0.15, relheight=0.1)


#Frame Button Label Entry pack grid place



root.mainloop()

