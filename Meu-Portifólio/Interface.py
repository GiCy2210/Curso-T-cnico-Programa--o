import customtkinter as ctk  
import tkinter.messagebox as messagebox

ctk.set_appearance_mode('dark') 

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'Giovane' and senha == 'Giovane0128':
        messagebox.showinfo('Login realizado com sucesso', 'Bem-Vindo')
    else:
        messagebox.showerror('Erro de login', 'Usuário ou senha incorreto')



#Aparencia
app = ctk.CTk() 
app.title('Sistema de Login')  
app.geometry('350x350') 

#Criação de campos
#Label = Subtítulo
label_usuario = ctk.CTkLabel(app, text= 'Usuário:')
label_usuario.pack(pady=10) 
#Entry = Campo de escrita
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)
#Label
label_senha = ctk.CTkLabel(app, text='Senha:')
label_senha.pack(pady=10)
#Entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

#Button = Botão
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)
#Criação das funções de funcionalidades

#Inicio da Aplicação
app.mainloop() 
