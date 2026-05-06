#exemplo
import tkinter as tk

class CalculadoraSimples(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent, bg="#111")

        self.expressao = ""

        self.visor = tk.Entry(
            self,
            font=("Arial", 35),
            bd=0,
            bg="#111",
            fg="white",
            justify="right"
        )

        self.visor.pack(
            fill="x",
            padx=40,
            pady=30,
            ipady=20
        )

        frame_botoes = tk.Frame(self, bg="#111")
        frame_botoes.pack(expand=True)

        botoes = [
            ('7', 0, 0),
            ('8', 0, 1),
            ('9', 0, 2),
            ('/', 0, 3),

            ('4', 1, 0),
            ('5', 1, 1),
            ('6', 1, 2),
            ('*', 1, 3),

            ('1', 2, 0),
            ('2', 2, 1),
            ('3', 2, 2),
            ('-', 2, 3),

            ('0', 3, 0),
            ('.', 3, 1),
            ('=', 3, 2),
            ('+', 3, 3),
        ]

        for texto, linha, coluna in botoes:

            comando = (
                self.calcular
                if texto == "="
                else lambda x=texto: self.clicar(x)
            )

            cor = (
                "#f59e0b"
                if texto in ['/', '*', '-', '+', '=']
                else "#3f3f46"
            )

            botao = tk.Button(
                frame_botoes,
                text=texto,
                command=comando,
                font=("Arial", 25, "bold"),
                bg=cor,
                fg="white",
                width=5,
                height=2,
                relief="flat"
            )

            botao.grid(
                row=linha,
                column=coluna,
                padx=10,
                pady=10
            )

    def clicar(self, valor):

        self.expressao += str(valor)

        self.visor.delete(0, tk.END)

        self.visor.insert(tk.END, self.expressao)

    def calcular(self):

        try:
            resultado = str(eval(self.expressao))

            self.visor.delete(0, tk.END)

            self.visor.insert(tk.END, resultado)

            self.expressao = resultado

        except:
            self.visor.delete(0, tk.END)

            self.visor.insert(tk.END, "Erro")

            self.expressao = ""