# Gerador de Senha — CustomTkinter
# Gera uma senha aleatória de tamanho configurável (até 32 caracteres),
# com botões para gerar, copiar e limpar.

import customtkinter as ctk
from random import randint
from PIL import Image, ImageTk
import os
import sys

# Obtém o caminho absoluto para um recurso, funcionando tanto rodando o .py
# normalmente quanto depois de empacotado com PyInstaller.
def resource_path(relative_path):
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho nela
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class GeradorSenha:

    TAMANHO_MAXIMO = 32

    def __init__(self):
        ctk.set_appearance_mode("System")  # Modos: "System" (padrão), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Temas: "blue" (padrão), "green", "dark-blue"

        self.janela = ctk.CTk()
        self.janela.geometry("520x350")
        self.janela.title("Gerador de Senha")

        self.carregar_icone()
        self.criar_widgets()


    # Define o ícone da janela
    def carregar_icone(self):
        try:
            icon_image = Image.open(resource_path("senha1.ico"))
            self.icon_photo = ImageTk.PhotoImage(icon_image) # Guarda a referência
            self.janela.iconphoto(False, self.icon_photo)
        except Exception as erro:
            print(f"Não foi possível carregar o ícone: {erro}")

    def criar_widgets(self):
        self.criar_campo_tamanho()
        self.criar_campo_senha()
        self.criar_botoes()

    # Campo onde o úsuario escolhe quantos caracteres a senha deve ter
    def criar_campo_tamanho(self):
        frame_tamanho = ctk.CTkFrame(self.janela)
        frame_tamanho.pack(pady=20)

        ctk.CTkLabel(
            frame_tamanho,
            text=f"Quantos caracteres (Máximo {self.TAMANHO_MAXIMO})?",
            font=("Helvetica", 16),
        ).pack(pady=10)

        # Registrar() conecta validar_tamanho ao mecanismo de validação do Tkinter
        validacao = self.janela.register(self.validar_tamanho)
        self.entry_tamanho = ctk.CTkEntry(
            frame_tamanho,
            font=("Helvetica", 24),
            validate="key",
            validatecommand=(validacao, "%P"),
            width=80,
            justify="center",
        )
        self.entry_tamanho.pack(pady=10)

    # Campo onde a senha gerada será exibida
    def criar_campo_senha(self):
        self.entry_senha = ctk.CTkEntry(
            self.janela, font=("Helvetica", 24), justify="center", width=500
        )
        self.entry_senha.pack(pady=20)

    # Botões para gerar, copiar e limpar a senha
    def criar_botoes(self):
        frame_botoes = ctk.CTkFrame(self.janela)
        frame_botoes.pack(pady=20)

        icones = self.carregar_icones_botoes()

        ctk.CTkButton(
            frame_botoes,
            text="Gerar senha forte",
            command=self.gerar_senha,
            image=icones["criar"],
            compound="left",
            font=("Helvetica", 16),
            fg_color="#4CAF50",
            hover_color="#45A049",
        ).grid(row=0, column=0, padx=10)

        ctk.CTkButton(
            frame_botoes,
            text="Copiar",
            command=self.copiar_senha,
            image=icones["copiar"],
            compound="left",
            font=("Helvetica", 16),
        ).grid(row=0, column=1, padx=10)

        ctk.CTkButton(
            frame_botoes,
            text="Limpar",
            command=self.limpar_campos,
            image=icones["limpar"],
            compound="left",
            font=("Helvetica", 16),
            fg_color="#ff9800",
            hover_color="#f57c00"
        ).grid(row=0, column=2, padx=10)

    # Carrega os três ícones usados nos botões, tratando o caso de faltr algum
    def carregar_icones_botoes(self):
        nomes = {"criar": "create.png", "copiar": "copy.png", "limpar": "clear.png"}
        icones = {}

        for chave, nome_arquivo in nomes.items():
            try:
                imagem = Image.open(resource_path(nome_arquivo))
                icones[chave] = ctk.CTkImage(light_image=imagem, dark_image=imagem, size=(20, 20))
            except Exception as erro:
                print(f"Não foi possível carregar {nome_arquivo}: {erro}")
                icones[chave] = None

        return icones

    # Gera uma senha aleatória com caracteres ASCII imprimíveis (33 a 126)
    def gerar_senha(self):
        self.entry_senha.delete(0, ctk.END)
        tamanho = int(self.entry_tamanho.get()) if self.entry_tamanho.get() else 0

        senha = "".join(chr(randint(33, 126)) for _ in range(tamanho))

        self.entry_senha.insert(0, senha)
        self.entry_senha.configure(justify="center")  # Centraliza o texto

    # Copia a senha gerada para a área de transferência do sistema
    def copiar_senha(self):
        self.janela.clipboard_clear()
        self.janela.clipboard_append(self.entry_senha.get())

    # Limpa os dois campos
    def limpar_campos(self):
        self.entry_tamanho.delete(0, ctk.END)
        self.entry_senha.delete(0, ctk.END)

    # Só permite números de até 2 dígitos, no máximo TAMANHO_MAXIMO
    def validar_tamanho(self,texto):
        if texto == "":
            return True
        if texto.isdigit() and len(texto) <= 2:
            return int(texto) <= self.TAMANHO_MAXIMO
        return False

    def executar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = GeradorSenha()
    app.executar()
