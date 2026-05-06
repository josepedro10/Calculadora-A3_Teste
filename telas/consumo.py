import tkinter as tk
from tkinter import messagebox

class CalculadoraConsumo(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent, bg="#162447")

        titulo = tk.Label(
            self,
            text="⚡ Consumo de Energia",
            font=("Arial", 35, "bold"),
            bg="#162447",
            fg="#facc15"
        )

        titulo.pack(pady=30)

        self.potencia = tk.Entry(self, font=("Arial", 22))
        self.potencia.pack(pady=15)

        self.horas = tk.Entry(self, font=("Arial", 22))
        self.horas.pack(pady=15)

        self.dias = tk.Entry(self, font=("Arial", 22))
        self.dias.pack(pady=15)

        botao = tk.Button(
            self,
            text="Calcular",
            command=self.calcular,
            font=("Arial", 22, "bold"),
            bg="#16a34a",
            fg="white"
        )

        botao.pack(pady=30)

        self.resultado = tk.Label(
            self,
            text="Consumo: 0 kWh",
            font=("Arial", 30, "bold"),
            bg="#162447",
            fg="white"
        )

        self.resultado.pack(pady=30)

    def calcular(self):

        try:
            consumo = (
                float(self.potencia.get()) *
                float(self.horas.get()) *
                float(self.dias.get())
            ) / 1000

            self.resultado.config(
                text=f"Consumo: {consumo:.2f} kWh"
            )

        except:
            messagebox.showerror(
                "Erro",
                "Digite valores válidos"
            )