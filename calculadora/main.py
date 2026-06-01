# -*- coding: utf-8 -*-
import tkinter as tk

from theme import ThemeConfig
from telas.home import TelaHome
from telas.calculadora import TelaCalculadora
from telas.consumo import TelaConsumo
from telas.media import TelaMedia
from telas.imc import TelaIMC
from telas.sobre import TelaSobre


class AppCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculadora Multifuncional")
        self.geometry("640x620")
        self.minsize(580, 600)
        
        self.tema_atual = "DARK"
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.telas = {}
        
        # Dicionário com as telas disponíveis
        self.telas_disponiveis = {
            "HOME": TelaHome,
            "CALCULADORA": TelaCalculadora,
            "CONSUMO": TelaConsumo,
            "MEDIA": TelaMedia,
            "IMC": TelaIMC,
            "SOBRE": TelaSobre
        }
        
        self.mostrar_tela("HOME")

    def mostrar_tela(self, nome_tela):
        print(f"Tentando abrir: {nome_tela}")  # Debug
        
        if nome_tela not in self.telas:
            classe = self.telas_disponiveis[nome_tela]
            frame = classe(parent=self.container, controller=self)
            self.telas[nome_tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Traz a tela para frente
        self.telas[nome_tela].tkraise()

    def alternar_tema(self):
        if self.tema_atual == "DARK":
            self.tema_atual = "LIGHT"
        else:
            self.tema_atual = "DARK"
        
        # Recria todas as telas para aplicar o novo tema
        for nome, tela in self.telas.items():
            tela.destroy()
        self.telas = {}
        self.mostrar_tela("HOME")


if __name__ == "__main__":
    app = AppCalculadora()
    app.mainloop()