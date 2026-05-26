# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from components.theme import ThemeConfig
from utils.calculations import calcular_imc_status

class TelaIMC(tk.Frame):
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

        self.val_peso = tk.StringVar()
        self.val_altura = tk.StringVar()

        lbl1 = tk.Label(main_container, text="Peso (kg)", font=ThemeConfig.FONT_LABEL, bg=cores["bg_window"], fg=cores["text_main"], anchor="w")
        lbl1.pack(fill="x", pady=(15, 3))
        
        input1_frame = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        input1_frame.pack(fill="x", pady=(0, 15))
        
        entry1 = tk.Entry(
            input1_frame, 
            textvariable=self.val_peso, 
            font=ThemeConfig.FONT_SUBTITLE, 
            bg=cores["bg_input"], 
            fg=cores["fg_input"],
            bd=0, 
            insertbackground=cores["fg_input"],
            justify="center"
        )
        entry1.pack(fill="x", ipady=8)

        lbl2 = tk.Label(main_container, text="Altura (m)", font=ThemeConfig.FONT_LABEL, bg=cores["bg_window"], fg=cores["text_main"], anchor="w")
        lbl2.pack(fill="x", pady=(5, 3))
        
        input2_frame = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        input2_frame.pack(fill="x", pady=(0, 20))
        
        entry2 = tk.Entry(
            input2_frame, 
            textvariable=self.val_altura, 
            font=ThemeConfig.FONT_SUBTITLE, 
            bg=cores["bg_input"], 
            fg=cores["fg_input"], 
            bd=0,
            insertbackground=cores["fg_input"],
            justify="center"
        )
        entry2.pack(fill="x", ipady=8)

        btn_calc_borda = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        btn_calc_borda.pack(pady=(5, 20))

        btn_calc = tk.Button(
            btn_calc_borda,
            text="Calcular IMC",
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

        self.imc_resultado_var = tk.StringVar(value="00.00")
        self.imc_status_var = tk.StringVar(value="Peso Ideal")
        
        res_display_borda = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        res_display_borda.pack(fill="x")

        res_grid = tk.Frame(res_display_borda, bg=cores["bg_display"], pady=12)
        res_grid.pack(fill="x")

        lbl_res_desc = tk.Label(res_grid, text="Seu IMC é:", font=("Helvetica", 8, "bold"), bg=cores["bg_display"], fg=cores["fg_display"])
        lbl_res_desc.pack()

        self.lbl_res_val = tk.Label(res_grid, textvariable=self.imc_resultado_var, font=("Georgia", 28, "bold"), bg=cores["bg_display"], fg=cores["fg_display"])
        self.lbl_res_val.pack()

        self.lbl_res_status = tk.Label(res_grid, textvariable=self.imc_status_var, font=("Georgia", 10, "bold"), bg=cores["bg_display"], fg=cores["fg_display"])
        self.lbl_res_status.pack()

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
            esta_ativa = (chave == "IMC")
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

    def calcular(self):
        try:
            peso_str = self.val_peso.get().strip()
            alt_str = self.val_altura.get().strip()

            if peso_str == "" or alt_str == "":
                raise ValueError("Por favor, preencha os valores de peso e altura!")

            peso = float(peso_str.replace(",", "."))
            altura = float(alt_str.replace(",", "."))

            imc_resultado, status_texto = calcular_imc_status(peso, altura)
            imc_formatado = f"{imc_resultado:.2f}".replace(".", ",")
            
            self.imc_resultado_var.set(imc_formatado)
            self.imc_status_var.set(status_texto)
        except ValueError as e:
            self.imc_resultado_var.set("00.00")
            self.imc_status_var.set("Peso Ideal")
            messagebox.showerror("Erro de Validação", str(e))
        except Exception:
            self.imc_resultado_var.set("00.00")
            self.imc_status_var.set("Peso Ideal")
            messagebox.showerror("Erro de Execução", "Valores inseridos são inválidos.")