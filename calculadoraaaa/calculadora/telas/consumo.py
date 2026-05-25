# -*- coding: utf-8 -*-
"""
Tela de Calculadora de Consumo de Energia da Aplicação Figma.
Contém: Inputs para Potência, Tempo de uso e Dias por mês, mais botão de cálculo e display para kWh/mês.
"""
import tkinter as tk
from tkinter import messagebox
from calculadora.componentes.theme import ThemeConfig
from calculadora.utils.calculations import calcular_consumo_energia

class TelaConsumo(tk.Frame):
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

        self.val_potencia = tk.StringVar(value="Ex: 100")
        self.val_tempo = tk.StringVar(value="Ex: 5")
        self.val_dias = tk.StringVar(value="Ex: 30")

        lbl1 = tk.Label(main_container, text="Potência do aparelho (W)", font=ThemeConfig.FONT_LABEL, bg=cores["bg_window"], fg=cores["text_main"], anchor="w")
        lbl1.pack(fill="x", pady=(5, 3))
        
        self.input1_frame = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        self.input1_frame.pack(fill="x", pady=(0, 10))
        
        self.entry1 = tk.Entry(
            self.input1_frame, 
            textvariable=self.val_potencia, 
            font=ThemeConfig.FONT_SUBTITLE, 
            bg=cores["bg_input"], 
            fg=cores["fg_input"] if self.val_potencia.get() != "Ex: 100" else "#7F7F7F",
            bd=0, 
            insertbackground=cores["fg_input"],
            justify="center"
        )
        self.entry1.pack(fill="x", ipady=8)
        
        lbl1_suf = tk.Label(self.input1_frame, text="Watts ", font=("Helvetica", 8, "bold"), bg=cores["bg_input"], fg="#7F7F7F")
        lbl1_suf.place(relx=0.97, rely=0.5, anchor="e")

        lbl2 = tk.Label(main_container, text="Tempo de uso diário (h)", font=ThemeConfig.FONT_LABEL, bg=cores["bg_window"], fg=cores["text_main"], anchor="w")
        lbl2.pack(fill="x", pady=(5, 3))
        
        self.input2_frame = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        self.input2_frame.pack(fill="x", pady=(0, 10))
        
        self.entry2 = tk.Entry(
            self.input2_frame, 
            textvariable=self.val_tempo, 
            font=ThemeConfig.FONT_SUBTITLE, 
            bg=cores["bg_input"], 
            fg=cores["fg_input"] if self.val_tempo.get() != "Ex: 5" else "#7F7F7F", 
            bd=0,
            insertbackground=cores["fg_input"],
            justify="center"
        )
        self.entry2.pack(fill="x", ipady=8)
        
        lbl2_suf = tk.Label(self.input2_frame, text="horas ", font=("Helvetica", 8, "bold"), bg=cores["bg_input"], fg="#7F7F7F")
        lbl2_suf.place(relx=0.97, rely=0.5, anchor="e")

        lbl3 = tk.Label(main_container, text="Quantidade de dias por mês", font=ThemeConfig.FONT_LABEL, bg=cores["bg_window"], fg=cores["text_main"], anchor="w")
        lbl3.pack(fill="x", pady=(5, 3))
        
        self.input3_frame = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        self.input3_frame.pack(fill="x", pady=(0, 15))
        
        self.entry3 = tk.Entry(
            self.input3_frame, 
            textvariable=self.val_dias, 
            font=ThemeConfig.FONT_SUBTITLE, 
            bg=cores["bg_input"], 
            fg=cores["fg_input"] if self.val_dias.get() != "Ex: 30" else "#7F7F7F",
            bd=0,
            insertbackground=cores["fg_input"],
            justify="center"
        )
        self.entry3.pack(fill="x", ipady=8)
        
        lbl3_suf = tk.Label(self.input3_frame, text="dias ", font=("Helvetica", 8, "bold"), bg=cores["bg_input"], fg="#7F7F7F")
        lbl3_suf.place(relx=0.97, rely=0.5, anchor="e")

        self.setup_placeholder(self.entry1, self.val_potencia, "Ex: 100", cores)
        self.setup_placeholder(self.entry2, self.val_tempo, "Ex: 5", cores)
        self.setup_placeholder(self.entry3, self.val_dias, "Ex: 30", cores)

        btn_calc_borda = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        btn_calc_borda.pack(pady=(5, 15))

        btn_calc = tk.Button(
            btn_calc_borda,
            text="Calcular Consumo",
            font=("Georgia", 11, "bold"),
            bg=cores["bg_btn_action"],
            fg=cores["fg_btn_action"],
            activebackground=cores["bg_btn_action"],
            activeforeground=cores["fg_btn_action"],
            bd=0,
            padx=25,
            pady=6,
            cursor="hand2",
            command=self.calcular
        )
        btn_calc.pack()

        self.resultado_var = tk.StringVar(value="00.00 kWh/mês")
        
        res_display_borda = tk.Frame(main_container, bg="#000000", padx=1, pady=1)
        res_display_borda.pack(fill="x")

        res_grid = tk.Frame(res_display_borda, bg=cores["bg_display"], pady=12)
        res_grid.pack(fill="x")

        lbl_res_desc = tk.Label(res_grid, text="Seu consumo estimado é:", font=("Helvetica", 8, "bold"), bg=cores["bg_display"], fg=cores["fg_display"])
        lbl_res_desc.pack()

        self.lbl_res_val = tk.Label(res_grid, textvariable=self.resultado_var, font=("Georgia", 22, "bold"), bg=cores["bg_display"], fg=cores["fg_display"])
        self.lbl_res_val.pack()

        self.criar_botao_home(cores)

    def setup_placeholder(self, entry, text_var, placeholder, cores):
        def focus_in(event):
            if text_var.get() == placeholder:
                text_var.set("")
                entry.configure(fg=cores["fg_input"])
                
        def focus_out(event):
            if text_var.get().strip() == "":
                text_var.set(placeholder)
                entry.configure(fg="#7F7F7F")

        entry.bind("<FocusIn>", focus_in)
        entry.bind("<FocusOut>", focus_out)

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
            esta_ativa = (chave == "ENERGY")
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
        home_borda.place(x=20, y=self.winfo_height() - 60 if self.winfo_height() > 100 else 440)

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
            pot = self.val_potencia.get().strip()
            temp = self.val_tempo.get().strip()
            dias = self.val_dias.get().strip()

            if pot in ["", "Ex: 100"] or temp in ["", "Ex: 5"] or dias in ["", "Ex: 30"]:
                raise ValueError("Preencha todos os campos do cálculo!")

            float_pot = float(pot.replace(",", "."))
            float_temp = float(temp.replace(",", "."))
            int_dias = int(dias)

            resultado = calcular_consumo_energia(float_pot, float_temp, int_dias)
            resultado_br = f"{resultado:.2f}".replace(".", ",")
            
            self.resultado_var.set(f"{resultado_br} kWh/mês")
        except ValueError as e:
            self.resultado_var.set("Erro")
            messagebox.showerror("Erro de Validação", str(e))
        except Exception:
            self.resultado_var.set("Erro")
            messagebox.showerror("Erro de Execução", "Valores digitados inválidos.")
