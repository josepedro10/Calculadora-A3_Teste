# -*- coding: utf-8 -*-
import tkinter as tk
from theme import ThemeConfig


class TelaHome(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.criar_interface()

    def criar_interface(self):
        cores = ThemeConfig.pegar_paleta(self.controller.tema_atual)
        self.configure(bg=cores["bg_janela"])
        
        for widget in self.winfo_children():
            widget.destroy()

        # Card centralizado
        card_largura = 400
        card_altura = 350
        
        moldura = tk.Frame(self, bg="#000000", padx=3, pady=3)
        moldura.place(relx=0.5, rely=0.5, anchor="center", width=card_largura, height=card_altura)

        card = tk.Frame(moldura, bg=cores["bg_card"])
        card.pack(fill="both", expand=True)

        # Título "CALCULADORA"
        tk.Label(card, text="CALCULADORA", 
                font=("Georgia", 28, "bold"),
                bg=cores["bg_card"], fg=cores["texto_principal"]).pack(pady=(50, 30))

        # Botão Entrar
        btn_entrar_borda = tk.Frame(card, bg="#000000", padx=1, pady=1)
        btn_entrar_borda.pack(pady=20)
        
        btn_entrar = tk.Button(btn_entrar_borda, text="Entrar", 
                              font=("Georgia", 16, "bold"),
                              bg=cores["bg_botao_primario"], 
                              fg=cores["texto_botao_primario"],
                              bd=0, padx=40, pady=8, cursor="hand2",
                              command=lambda: self.controller.mostrar_tela("CALCULADORA"))
        btn_entrar.pack()

        # Botão de tema (canto inferior esquerdo)
        btn_tema_borda = tk.Frame(card, bg="#000000", padx=1, pady=1)
        btn_tema_borda.pack(side="left", padx=15, pady=(0, 15))
        
        if self.controller.tema_atual == "DARK":
            texto_tema = "☀️ Tema Claro"
        else:
            texto_tema = "🌙 Tema Escuro"

        btn_tema = tk.Button(btn_tema_borda, text=texto_tema,
                            font=("Helvetica", 9, "bold"),
                            bg=cores["bg_botao_primario"],
                            fg=cores["texto_botao_primario"],
                            bd=0, padx=10, pady=4, cursor="hand2",
                            command=self.controller.alternar_tema)
        btn_tema.pack()

    def atualizar_tela(self):
        self.criar_interface()