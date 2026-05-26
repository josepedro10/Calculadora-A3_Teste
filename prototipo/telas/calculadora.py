# -*- coding: utf-8 -*-
import tkinter as tk
from components.theme import ThemeConfig

class TelaCalculadora(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.expressao = "0"
        self.reiniciar_no_proximo_clique = False
        self.config_tela()

    def config_tela(self):
        cores = ThemeConfig.get_palette(self.controller.tema_atual)
        self.configure(bg=cores["bg_window"])

        for widget in self.winfo_children():
            widget.destroy()

        self.criar_header_navegacao(cores)

        calc_container = tk.Frame(self, bg=cores["bg_window"])
        calc_container.place(relx=0.5, rely=0.52, anchor="center", width=360, height=480)

        disp_borda = tk.Frame(calc_container, bg="#000000", padx=1, pady=1)
        disp_borda.pack(fill="x", pady=(10, 10))

        self.display_var = tk.StringVar(value=self.expressao)
        self.lbl_display = tk.Label(
            disp_borda,
            textvariable=self.display_var,
            font=("Consolas", 28, "bold"),
            bg=cores["bg_display"],
            fg=cores["fg_display"],
            anchor="e",
            padx=15,
            pady=12,
            height=1
        )
        self.lbl_display.pack(fill="x")

        grid_frame = tk.Frame(calc_container, bg=cores["bg_window"])
        grid_frame.pack(fill="both", expand=True)

        for c in range(4):
            grid_frame.columnconfigure(c, weight=1, minsize=75)
        for r in range(5):
            grid_frame.rowconfigure(r, weight=1, minsize=65)

        botoes = [
            ("AC", "gray", 0, 0, 1), ("+/-", "gray", 0, 1, 1), ("%", "gray", 0, 2, 1), ("÷", "orange", 0, 3, 1),
            ("7", "num", 1, 0, 1), ("8", "num", 1, 1, 1), ("9", "num", 1, 2, 1), ("x", "orange", 1, 3, 1),
            ("4", "num", 2, 0, 1), ("5", "num", 2, 1, 1), ("6", "num", 2, 2, 1), ("-", "orange", 2, 3, 1),
            ("1", "num", 3, 0, 1), ("2", "num", 3, 1, 1), ("3", "num", 3, 2, 1), ("+", "orange", 3, 3, 1),
            ("0", "num", 4, 0, 2), (",", "num", 4, 2, 1), ("=", "orange", 4, 3, 1)
        ]

        for texto, tipo, row, col, span in botoes:
            if tipo == "num":
                bg_cor = cores["bg_btn_num"]
                fg_cor = cores["fg_btn_num"]
            elif tipo == "gray":
                bg_cor = cores["bg_btn_gray"]
                fg_cor = cores["fg_btn_gray"]
            else:
                bg_cor = cores["bg_btn_orange"]
                fg_cor = cores["fg_btn_orange"]

            btn_borda = tk.Frame(grid_frame, bg="#000000", padx=1, pady=1)
            btn_borda.grid(row=row, column=col, columnspan=span, padx=4, pady=4, sticky="nsew")

            btn = tk.Button(
                btn_borda,
                text=texto,
                font=("Georgia" if tipo in ["num", "orange"] else "Helvetica", 16, "bold"),
                bg=bg_cor,
                fg=fg_cor,
                activebackground=bg_cor,
                activeforeground=fg_cor,
                bd=0,
                cursor="hand2",
                command=lambda t=texto: self.clique_botao(t)
            )
            btn.pack(fill="both", expand=True)

        self.criar_botao_home(cores)

    def criar_header_navegacao(self, cores):
        header_frame = tk.Frame(self, bg=cores["bg_window"])
        header_frame.pack(fill="x", padx=30, pady=(20, 0))

        abas = [
            ("Calculadora", "CALCULATOR"),
            ("Consumo", "ENERGY"),
            ("Média", "AVERAGE"),
            ("IMC", "IMC")
        ]

        for nome, chave in abas:
            esta_ativa = (chave == "CALCULATOR")
            cor_link = cores["text_main"] if esta_ativa else cores["text_muted"]
            fonte_aba = ("Georgia", 11, "bold" if esta_ativa else "normal")

            btn_aba = tk.Button(
                header_frame,
                text=nome,
                font=fonte_aba,
                fg=cor_link,
                bg=cores["bg_window"],
                activeforeground=cores["text_main"],
                activebackground=cores["bg_window"],
                bd=0,
                cursor="hand2",
                command=lambda k=chave: self.controller.mostrar_tela(k)
            )
            btn_aba.pack(side="left", expand=True, fill="x", padx=5)

    def criar_botao_home(self, cores):
        home_borda = tk.Frame(self, bg="#000000", padx=1, pady=1)
        home_borda.place(relx=0.05, rely=0.95, anchor="sw")
        
        btn_home = tk.Button(
            home_borda,
            text=" ⌂ ",
            font=("Helvetica", 14, "bold"),
            bg=cores["bg_btn_num"],
            fg=cores["fg_btn_num"],
            activebackground=cores["bg_btn_num"],
            activeforeground=cores["fg_btn_num"],
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            command=lambda: self.controller.mostrar_tela("WELCOME")
        )
        btn_home.pack()

    def clique_botao(self, valor):
        if valor == "AC":
            self.expressao = "0"
            self.reiniciar_no_proximo_clique = False
        elif valor == "+/-":
            if self.expressao != "0":
                if self.expressao.startswith("-"):
                    self.expressao = self.expressao[1:]
                else:
                    self.expressao = "-" + self.expressao
        elif valor == "%":
            try:
                expr_interna = self.expressao.replace(",", ".")
                res = float(eval(expr_interna)) / 100.0
                self.expressao = str(res).replace(".", ",")
            except Exception:
                self.expressao = "Erro"
        elif valor == "=":
            self.calcular_resultado()
            self.reiniciar_no_proximo_clique = True
            return
        elif valor in ["+", "-", "x", "÷"]:
            if self.reiniciar_no_proximo_clique:
                self.reiniciar_no_proximo_clique = False
                
            ultimo_char = self.expressao[-1] if self.expressao else ""
            if ultimo_char in [" + ", " - ", " * ", " / "]:
                self.expressao = self.expressao[:-3]
                
            if valor == "+":
                self.expressao += " + "
            elif valor == "-":
                self.expressao += " - "
            elif valor == "x":
                self.expressao += " * "
            elif valor == "÷":
                self.expressao += " / "
        else:
            if self.expressao == "0" or self.reiniciar_no_proximo_clique:
                if valor == ",":
                    self.expressao = "0,"
                else:
                    self.expressao = valor
                self.reiniciar_no_proximo_clique = False
            else:
                self.expressao += valor
                
        self.atualizar_display()

    def calcular_resultado(self):
        try:
            expr_eval = self.expressao.replace(",", ".").replace(" ", "")
            resultado = eval(expr_eval, {"__builtins__": None}, {})
            
            if isinstance(resultado, float):
                if resultado.is_integer():
                    resultado = int(resultado)
                else:
                    resultado = round(resultado, 5)
                    
            self.expressao = str(resultado).replace(".", ",")
        except Exception:
            self.expressao = "Erro"
        self.atualizar_display()

    def atualizar_display(self):
        texto_curto = self.expressao
        if len(texto_curto) > 14:
            texto_curto = texto_curto[:13] + "…"
        self.display_var.set(texto_curto)