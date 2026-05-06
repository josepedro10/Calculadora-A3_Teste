import tkinter as tk

class Home(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent, bg="#b076b0")

        titulo = tk.Label(
            self,
            text="CALCULADORA\nESTENDIDA",
            font=("Arial", 45, "bold"),
            bg="#b076b0",
            fg="#49206d"
        )

        titulo.pack(expand=True)