import tkinter as tk
from tkinter import messagebox

class CalculadoraIMC(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent, bg="#f3f3f3")

        titulo = tk.Label(
            self,
            text="Calculadora IMC",
            font=("Arial", 35, "bold"),
            bg="#f3f3f3",
            fg="#9333ea"
        )

        titulo.pack(pady=30)

        self.peso = tk.Entry(self, font=("Arial", 22))
        self.peso.pack(pady=15)

        self.peso.insert(0, "Peso")

        self.altura = tk.Entry(self, font=("Arial", 22))
        self.altura.pack(pady=15)

        self.altura.insert(0, "Altura")

        botao = tk.Button(
            self,
            text="Calcular",
            command=self.calcular,
            font=("Arial", 22, "bold"),
            bg="#0d8aa0",
            fg="white"
        )

        botao.pack(pady=30)

        self.resultado = tk.Label(
            self,
            text="Seu IMC: 0",
            font=("Arial", 30, "bold"),
            bg="#f3f3f3",
            fg="#9333ea"
        )

        self.resultado.pack(pady=30)

    def calcular(self):

        try:
            peso = float(self.peso.get())
            altura = float(self.altura.get())

            if altura > 3:
                altura /= 100

            imc = peso / (altura ** 2)

            self.resultado.config(
                text=f"Seu IMC: {imc:.2f}"
            )

        except:
            messagebox.showerror(
                "Erro",
                "Digite valores válidos"
            )