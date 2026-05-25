# -*- coding: utf-8 -*-
"""
Tela Inicial (Welcome Screen) da Calculadora Figma.
Contém: Título estilizado estilo outline, botão 'Entrar' e o controle de tema.
"""
import tkinter as tk
from calculadora.componentes.theme import ThemeConfig

class TelaHome(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config_tela()

    def config_tela(self):
        """Monta o design da tela inicial de acordo com as cores do tema ativo."""
        cores = ThemeConfig.get_palette(self.controller.tema_atual)
        self.configure(bg=cores["bg_window"])
        
        for widget in self.winfo_children():
            widget.destroy()

        card_largura = 500
        card_altura = 350
        
        borda_frame = tk.Frame(
            self, 
            bg="#000000", 
            padx=3, 
            pady=3
        )
        borda_frame.place(relx=0.5, rely=0.5, anchor="center", width=card_largura, height=card_altura)

        card_conteudo = tk.Frame(
            borda_frame, 
            bg=cores["bg_card"]
        )
        card_conteudo.pack(fill="both", expand=True)

        canvas_titulo = tk.Canvas(
            card_conteudo, 
            bg=cores["bg_card"], 
            highlightthickness=0,
            height=120
        )
        canvas_titulo.pack(pady=(60, 20), fill="x")

        texto = "CALCULADORA"
        outline_cor = "#000000"
        texto_cor = "#FFFFFF" if self.controller.tema_atual == "DARK" else "#000000"
        fonte_titulo_canvas = ("Georgia", 32, "bold")

        def desenhar_texto_com_outline(canvas, text, x, y):
            deslocamentos = [(-2, -2), (-2, 0), (-2, 2), (0, -2), (0, 2), (2, -2), (2, 0), (2, 2)]
            for dx, dy in deslocamentos:
                canvas.create_text(x + dx, y + dy, text=text, font=fonte_titulo_canvas, fill=outline_cor, anchor="center")
            canvas.create_text(x, y, text=text, font=fonte_titulo_canvas, fill=texto_cor, anchor="center")

        largura_aproximada = card_largura // 2
        desenhar_texto_com_outline(canvas_titulo, texto, largura_aproximada - 8, 60)

        btn_borda = tk.Frame(card_conteudo, bg="#000000", padx=1, pady=1)
        btn_borda.pack(pady=20)

        btn_entrar = tk.Button(
            btn_borda,
            text="Entrar",
            font=("Georgia", 16, "bold"),
            bg=cores["bg_btn_primary"],
            fg=cores["fg_btn_primary"],
            activebackground=cores["bg_btn_primary"],
            activeforeground=cores["fg_btn_primary"],
            bd=0,
            padx=35,
            pady=8,
            cursor="hand2",
            command=self.ir_para_calculadora
        )
        btn_entrar.pack()

        btn_badge_borda = tk.Frame(card_conteudo, bg="#000000", padx=1, pady=1)
        btn_badge_borda.pack(side="left", padx=15, pady=(0, 15))

        texto_badge = " Tema Claro" if self.controller.tema_atual == "DARK" else " Tema Escuro"
        icone_badge = "☀" if self.controller.tema_atual == "DARK" else "🌙"

        btn_badge = tk.Button(
            btn_badge_borda,
            text=f"{icone_badge}{texto_badge}",
            font=("Helvetica", 9, "bold"),
            bg=cores["bg_badge"],
            fg=cores["fg_badge"],
            activebackground=cores["bg_badge"],
            activeforeground=cores["fg_badge"],
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            command=self.controller.alternar_tema
        )
        btn_badge.pack()

    def ir_para_calculadora(self):
        self.controller.mostrar_tela("CALCULATOR")
