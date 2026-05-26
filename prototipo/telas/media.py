# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from components.theme import ThemeConfig
from utils.calculations import calcular_media_tres_valores

class TelaMedia(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config_tela()

    def config_tela(self):
        cores = ThemeConfig.get_palette(self.controller.tema_atual)
        self.configure(bg=cores["bg_window"])

        for widget in self.winfo_children():
            widget.destroy()

        self.criar_header_navegacao(cores)

        main_container = tk.Frame(self, bg=cores["bg_window"])
        main_container.place(relx=0.5, rely=0.52, anchor="center", width=380, height=450)

        self.val1 = tk.StringVar()
        self.val2 = tk.StringVar()
        self.val3 = tk.StringVar()

        lbl1 = tk.Label(main_container, text="Valor 1", font=ThemeConfig.FONT_LABEL, bg=cores["bg_window"], fg=cores["text_main"], anchor="w")
        lbl1.pack(fill="x", pady=(5, 3))
        
        input1_frame = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        input1_frame.pack(fill="x", pady=(0, 10))
        
        entry1 = tk.Entry(
            input1_frame, 
            textvariable=self.val1, 
            font=ThemeConfig.FONT_SUBTITLE, 
            bg=cores["bg_input"], 
            fg=cores["fg_input"],
            bd=0, 
            insertbackground=cores["fg_input"],
            justify="center"
        )
        entry1.pack(fill="x", ipady=8)

        lbl2 = tk.Label(main_container, text="Valor 2", font=ThemeConfig.FONT_LABEL, bg=cores["bg_window"], fg=cores["text_main"], anchor="w")
        lbl2.pack(fill="x", pady=(5, 3))
        
        input2_frame = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        input2_frame.pack(fill="x", pady=(0, 10))
        
        entry2 = tk.Entry(
            input2_frame, 
            textvariable=self.val2, 
            font=ThemeConfig.FONT_SUBTITLE, 
            bg=cores["bg_input"], 
            fg=cores["fg_input"], 
            bd=0,
            insertbackground=cores["fg_input"],
            justify="center"
        )
        entry2.pack(fill="x", ipady=8)

        lbl3 = tk.Label(main_container, text="Valor 3", font=ThemeConfig.FONT_LABEL, bg=cores["bg_window"], fg=cores["text_main"], anchor="w")
        lbl3.pack(fill="x", pady=(5, 3))
        
        input3_linha = tk.Frame(main_container, bg=cores["bg_window"])
        input3_linha.pack(fill="x", pady=(0, 15))
        
        input3_frame = tk.Frame(input3_linha, bg="#000000", padx=1, pady=1)
        input3_frame.pack(fill="left", expand=True)
        
        entry3 = tk.Entry(
            input3_frame, 
            textvariable=self.val3, 
            font=ThemeConfig.FONT_SUBTITLE, 
            bg=cores["bg_input"], 
            fg=cores["fg_input"],
            bd=0,
            insertbackground=cores["fg_input"],
            justify="center"
        )
        entry3.pack(fill="x", ipady=8)
        
        btn_lixeira_borda = tk.Frame(input3_linha, bg="#000000", padx=1, pady=1)
        btn_lixeira_borda.pack(side="right", padx=(10, 0))
        
        btn_lixeira = tk.Button(
            btn_lixeira_borda,
            text=" 🗑 ",
            font=("Helvetica", 11, "bold"),
            bg="#C0392B",
            fg="#FFFFFF",
            activebackground="#E74C3C",
            activeforeground="#FFFFFF",
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            command=self.limpar_campos
        )
        btn_lixeira.pack()

        btn_calc_borda = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        btn_calc_borda.pack(pady=(5, 15))

        btn_calc = tk.Button(
            btn_calc_borda,
            text="Calcular Média",
            font=("Georgia", 11, "bold"),
            bg=cores["bg_btn_action"],
            fg=cores["fg_btn_action"],
            activebackground=cores["bg_btn_action"],
            activeforeground=cores["fg_btn_action"],
            bd=0,
            padx=35,
            pady=6,
            cursor="hand2",
            command=self.calcular
        )
        btn_calc.pack()

        self.resultado_var = tk.StringVar(value="00.00")
        
        res_display_borda = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        res_display_borda.pack(fill="x")

        res_grid = tk.Frame(res_display_borda, bg=cores["bg_display"], pady=12)
        res_grid.pack(fill="x")

        lbl_res_desc = tk.Label(res_grid, text="Sua média é:", font=("Helvetica", 8, "bold"), bg=cores["bg_display"], fg=cores["fg_display"])
        lbl_res_desc.pack()

        self.lbl_res_val = tk.Label(res_grid, textvariable=self.resultado_var, font=("Georgia", 26, "bold"), bg=cores["bg_display"], fg=cores["fg_display"])
        self.lbl_res_val.pack()

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
            esta_ativa = (chave == "AVERAGE")
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

    def limpar_campos(self):
        self.val1.set("")
        self.val2.set("")
        self.val3.set("")
        self.resultado_var.set("00.00")

    def calcular(self):
        try:
            v1_str = self.val1.get().strip()
            v2_str = self.val2.get().strip()
            v3_str = self.val3.get().strip()

            if v1_str == "" or v2_str == "" or v3_str == "":
                raise ValueError("Por favor, preencha todos os três campos de valor.")

            n1 = float(v1_str.replace(",", "."))
            n2 = float(v2_str.replace(",", "."))
            n3 = float(v3_str.replace(",", "."))

            resultado = calcular_media_tres_valores(n1, n2, n3)
            resultado_br = f"{resultado:.2f}".replace(".", ",")
            
            self.resultado_var.set(resultado_br)
        except ValueError as e:
            self.resultado_var.set("00.00")
            messagebox.showerror("Erro de Validação", str(e))
        except Exception:
            self.resultado_var.set("00.00")
            messagebox.showerror("Erro de Execução", "Valores digitados inválidos.")