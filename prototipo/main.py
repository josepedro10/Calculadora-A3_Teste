# -*- coding: utf-8 -*-
"""
Calculadora Figma - Arquivo Principal (Main entrypoint).
"""
import sys
import os
import tkinter as tk

# Adiciona o diretório atual ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from components.theme import ThemeConfig
from telas.home import TelaHome
from telas.calculadora import TelaCalculadora
from telas.consumo import TelaConsumo
from telas.media import TelaMedia
from telas.imc import TelaIMC

class AplicativoCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculadora Figma Multi-telas")
        self.geometry("640x580")
        self.minsize(580, 560)
        
        self.tema_atual = "DARK"
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.classes_telas = {
            "WELCOME": TelaHome,
            "CALCULATOR": TelaCalculadora,
            "ENERGY": TelaConsumo,
            "AVERAGE": TelaMedia,
            "IMC": TelaIMC
        }
        
        self.mostrar_tela("WELCOME")

    def mostrar_tela(self, chave_tela: str):
        if chave_tela not in self.frames:
            classe_frame = self.classes_telas[chave_tela]
            frame_instancia = classe_frame(parent=self.container, controller=self)
            self.frames[chave_tela] = frame_instancia
            frame_instancia.grid(row=0, column=0, sticky="nsew")
        else:
            self.frames[chave_tela].config_tela()

        frame_visivel = self.frames[chave_tela]
        frame_visivel.tkraise()

    def alternar_tema(self):
        self.tema_atual = "LIGHT" if self.tema_atual == "DARK" else "DARK"
        
        for chave, frame in self.frames.items():
            frame.config_tela()

        cores = ThemeConfig.get_palette(self.tema_atual)
        self.configure(bg=cores["bg_window"])

if __name__ == "__main__":
    app = AplicativoCalculadora()
    app.mainloop()