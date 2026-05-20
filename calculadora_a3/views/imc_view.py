import tkinter as tk
from tkinter import messagebox
from assests.style import create_title, create_button
from controllers.imc_controller import IMCController

class IMCView:
    def __init__(self, parent, controller, colors):
        self.parent = parent
        self.main_controller = controller
        self.imc_controller = IMCController()
        self.colors = colors
        self.frame = None
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.parent, bg=self.colors['bg'])
        
        # Título
        title = create_title(self.frame, "Calculadora de IMC", fg=self.colors['secondary'])
        title.configure(bg=self.colors['bg'])
        title.pack(pady=20)
        
        # Frame de entrada
        input_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        input_frame.pack(pady=20)
        
        # Peso
        tk.Label(
            input_frame,
            text="Peso (kg):",
            font=('Arial', 12),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        ).grid(row=0, column=0, pady=10, sticky='w')
        
        self.peso_entry = tk.Entry(
            input_frame, 
            font=('Arial', 12), 
            width=20,
            bg=self.colors['entry_bg'],
            fg=self.colors['entry_fg'],
            insertbackground=self.colors['entry_fg']
        )
        self.peso_entry.grid(row=0, column=1, pady=10, padx=10)
        
        # Altura
        tk.Label(
            input_frame,
            text="Altura (m):",
            font=('Arial', 12),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        ).grid(row=1, column=0, pady=10, sticky='w')
        
        self.altura_entry = tk.Entry(
            input_frame, 
            font=('Arial', 12), 
            width=20,
            bg=self.colors['entry_bg'],
            fg=self.colors['entry_fg'],
            insertbackground=self.colors['entry_fg']
        )
        self.altura_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # Resultado
        self.resultado_label = tk.Label(
            input_frame,
            text="",
            font=('Arial', 12, 'bold'),
            bg=self.colors['bg']
        )
        self.resultado_label.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Botão calcular
        calcular_btn = create_button(
            input_frame,
            "Calcular IMC",
            self.calcular,
            bg=self.colors['success'],
            fg='white',
            padx=20,
            pady=10
        )
        calcular_btn.grid(row=3, column=0, columnspan=2, pady=20)
    
    def calcular(self):
        success, resultado, cor_tipo = self.imc_controller.calcular(
            self.peso_entry.get(),
            self.altura_entry.get()
        )
        
        if success:
            cores = {
                'warning': self.colors['warning'],
                'success': self.colors['success'],
                'danger': self.colors['danger']
            }
            cor = cores.get(cor_tipo, self.colors['primary'])
            self.resultado_label.config(text=resultado, fg=cor)
        else:
            messagebox.showerror("Erro", resultado)
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()