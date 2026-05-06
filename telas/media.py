import tkinter as tk
from tkinter import messagebox

class CalculadoraMedia(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent, bg="#dbeafe")

        titulo = tk.Label(
            self,
            text="Calculadora de Média",
            font=("Arial", 35, "bold"),
            bg="#dbeafe",
            fg="#1e3a8a"
        )

        titulo.pack(pady=30)

        self.n1 = tk.Entry(self, font=("Arial", 22))
        self.n1.pack(pady=15)

        self.n2 = tk.Entry(self, font=("Arial", 22))
        self.n2.pack(pady=15)

        self.n3 = tk.Entry(self, font=("Arial", 22))
        self.n3.pack(pady=15)

        botao = tk.Button(
            self,
            text="Calcular Média",
            command=self.calcular,
            font=("Arial", 22, "bold"),
            bg="#2563eb",
            fg="white"
        )

        botao.pack(pady=30)

        self.resultado = tk.Label(
            self,
            text="Média: 0",
            font=("Arial", 30, "bold"),
            bg="#dbeafe",
            fg="#1e3a8a"
        )

        self.resultado.pack(pady=30)

    def calcular(self):

        try:
            media = (
                float(self.n1.get()) +
                float(self.n2.get()) +
                float(self.n3.get())
            ) / 3

            self.resultado.config(
                text=f"Média: {media:.2f}"
            )

        except:
            messagebox.showerror(
                "Erro",
                "Digite valores válidos"
            )