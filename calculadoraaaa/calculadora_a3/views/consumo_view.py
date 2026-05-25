import tkinter as tk
from tkinter import messagebox
from assets.style import create_title, create_button
from controllers.consumo_controller import ConsumoController

class ConsumoView:
    def __init__(self, parent, controller, colors):
        self.parent = parent
        self.main_controller = controller
        self.consumo_controller = ConsumoController()
        self.colors = colors
        self.frame = None
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.parent, bg=self.colors['bg'])
        
        # Título
        title = create_title(self.frame, "Calculadora de Consumo de Energia", fg=self.colors['secondary'])
        title.configure(bg=self.colors['bg'])
        title.pack(pady=20)
        
        # Frame de entrada
        input_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        input_frame.pack(pady=20)
        
        # Potência
        tk.Label(
            input_frame,
            text="Potência do aparelho (W):",
            font=('Arial', 12),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        ).grid(row=0, column=0, pady=10, sticky='w')
        
        self.potencia_entry = tk.Entry(
            input_frame, 
            font=('Arial', 12), 
            width=20,
            bg=self.colors['entry_bg'],
            fg=self.colors['entry_fg'],
            insertbackground=self.colors['entry_fg']
        )
        self.potencia_entry.grid(row=0, column=1, pady=10, padx=10)
        
        # Horas por dia
        tk.Label(
            input_frame,
            text="Horas de uso por dia:",
            font=('Arial', 12),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        ).grid(row=1, column=0, pady=10, sticky='w')
        
        self.horas_entry = tk.Entry(
            input_frame, 
            font=('Arial', 12), 
            width=20,
            bg=self.colors['entry_bg'],
            fg=self.colors['entry_fg'],
            insertbackground=self.colors['entry_fg']
        )
        self.horas_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # Dias por mês
        tk.Label(
            input_frame,
            text="Dias de uso por mês:",
            font=('Arial', 12),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        ).grid(row=2, column=0, pady=10, sticky='w')
        
        self.dias_entry = tk.Entry(
            input_frame, 
            font=('Arial', 12), 
            width=20,
            bg=self.colors['entry_bg'],
            fg=self.colors['entry_fg'],
            insertbackground=self.colors['entry_fg']
        )
        self.dias_entry.grid(row=2, column=1, pady=10, padx=10)
        
        # Preço do kWh
        tk.Label(
            input_frame,
            text="Preço do kWh (R$):",
            font=('Arial', 12),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        ).grid(row=3, column=0, pady=10, sticky='w')
        
        self.preco_entry = tk.Entry(
            input_frame, 
            font=('Arial', 12), 
            width=20,
            bg=self.colors['entry_bg'],
            fg=self.colors['entry_fg'],
            insertbackground=self.colors['entry_fg']
        )
        self.preco_entry.insert(0, "0.75")
        self.preco_entry.grid(row=3, column=1, pady=10, padx=10)
        
        # Botão calcular
        calcular_btn = create_button(
            input_frame,
            "Calcular Consumo",
            self.calcular,
            bg=self.colors['success'],
            fg='white',
            padx=20,
            pady=10
        )
        calcular_btn.grid(row=4, column=0, columnspan=2, pady=20)
    
    def calcular(self):
        success, result = self.consumo_controller.calcular(
            self.potencia_entry.get(),
            self.horas_entry.get(),
            self.dias_entry.get(),
            self.preco_entry.get()
        )
        
        if success:
            consumo_kwh, custo_total, custo_diario = result
            mensagem = f"""
            Consumo mensal: {consumo_kwh:.2f} kWh
            Custo mensal: R$ {custo_total:.2f}
            Custo diário: R$ {custo_diario:.2f}
            """
            messagebox.showinfo("Resultado", mensagem)
        else:
            messagebox.showerror("Erro", result)
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()