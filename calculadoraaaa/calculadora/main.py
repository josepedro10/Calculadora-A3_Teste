# -*- coding: utf-8 -*-
"""
Calculadora Figma - Arquivo Principal (Main entrypoint).
Este arquivo integra as telas e componentes utilizando a biblioteca Tkinter,
administra a troca de telas (sem abrir novas janelas) e a troca dinâmica do tema (Claro / Escuro).
"""
import sys
import os
import tkinter as tk

# Adiciona o diretório atual ao path para importação correta dos submódulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calculadora.componentes.theme import ThemeConfig
from calculadora.telas.home import TelaHome
from calculadora.telas.calculadora import TelaCalculadora
from calculadora.telas.consumo import TelaConsumo
from calculadora.telas.media import TelaMedia
from calculadora.telas.imc import TelaIMC

class AplicativoCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configuração da janela principal
        self.title("Calculadora Figma Multi-telas")
        self.geometry("640x580")  # Resoluções responsivas e harmônicas
        self.minsize(580, 560)    # Impeço tamanhos muito esmagados que quebrem os botões
        
        # Estado Global
        self.tema_atual = "DARK"  # Inicializa em Modo Escuro de acordo com Figma Desktop-1
        
        # Contêiner base onde as telas (frames) serão montadas empilhadas
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Mapeamento e Cache das Telas do Projeto
        self.frames = {}
        self.classes_telas = {
            "WELCOME": TelaHome,
            "CALCULATOR": TelaCalculadora,
            "ENERGY": TelaConsumo,
            "AVERAGE": TelaMedia,
            "IMC": TelaIMC
        }
        
        # Carrega a tela de Boas-Vindas inicialmente
        self.mostrar_tela("WELCOME")

    def mostrar_tela(self, chave_tela: str):
        """Alterna a visualização para a tela correspondente de forma reativa."""
        # Se a tela ainda não foi instanciada, criamos ela agora de forma 'lazy'
        if chave_tela not in self.frames:
            classe_frame = self.classes_telas[chave_tela]
            frame_instancia = classe_frame(parent=self.container, controller=self)
            self.frames[chave_tela] = frame_instancia
            frame_instancia.grid(row=0, column=0, sticky="nsew")
        else:
            # Caso já exista, atualiza as cores com base no tema ativo corrente
            self.frames[chave_tela].config_tela()

        # Eleva a tela ao topo do empilhamento do Tkinter para torná-la visível
        frame_visivel = self.frames[chave_tela]
        frame_visivel.tkraise()

    def alternar_tema(self):
        """Inverte o tema global da aplicação de forma dinâmica e re-renderiza a tela atual."""
        self.tema_atual = "LIGHT" if self.tema_atual == "DARK" else "DARK"
        
        # Força as telas instanciadas em cache a aplicarem o novo tema
        for chave, frame in self.frames.items():
            frame.config_tela()

        # Configura as próprias bordas da janela raiz do Tkinter
        cores = ThemeConfig.get_palette(self.tema_atual)
        self.configure(bg=cores["bg_window"])

if __name__ == "__main__":
    # Inicializa o loop de execução do Tkinter
    app = AplicativoCalculadora()
    app.mainloop()
