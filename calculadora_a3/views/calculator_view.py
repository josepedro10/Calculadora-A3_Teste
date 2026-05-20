import tkinter as tk
from assets.style import create_title
from controllers.calculator_controller import CalculatorController

class CalculatorView:
    def __init__(self, parent, controller, colors):
        self.parent = parent
        self.main_controller = controller
        self.calc_controller = CalculatorController()
        self.colors = colors
        self.frame = None
        self.display_var = None
        self.buttons = []
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.parent, bg=self.colors['bg'])
        
        # Título
        title = create_title(self.frame, "Calculadora", fg=self.colors['secondary'])
        title.configure(bg=self.colors['bg'])
        title.pack(pady=10)
        
        # Display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        display = tk.Entry(
            self.frame,
            textvariable=self.display_var,
            font=('Arial', 20, 'bold'),
            justify=tk.RIGHT,
            bd=10,
            relief=tk.SUNKEN,
            state='readonly',
            bg=self.colors['display_bg'],
            fg=self.colors['display_fg'],
            readonlybackground=self.colors['display_bg']
        )
        display.pack(fill=tk.X, padx=20, pady=10)
        
        # Botões
        buttons_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        buttons_frame.pack(pady=10)
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0), ('AC', 4, 1), ('%', 4, 2), ('√', 4, 3)
        ]
        
        for text, row, col in buttons:
            # Determinar cor do botão
            if text in ['+', '-', '*', '/', '=', '√', '%']:
                bg_color = self.colors['secondary']
                fg_color = 'white'
            else:
                bg_color = self.colors['white']
                fg_color = self.colors['primary']
            
            btn = tk.Button(
                buttons_frame,
                text=text,
                command=lambda t=text: self.button_click(t),
                font=('Arial', 14, 'bold'),
                width=5,
                height=2,
                bg=bg_color,
                fg=fg_color,
                relief=tk.RAISED
            )
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)
    
    def update_theme(self):
        """Atualiza as cores dos botões quando o tema muda"""
        for btn in self.buttons:
            text = btn.cget('text')
            if text in ['+', '-', '*', '/', '=', '√', '%']:
                btn.configure(bg=self.colors['secondary'], fg='white')
            else:
                btn.configure(bg=self.colors['white'], fg=self.colors['primary'])
    
    def button_click(self, value):
        current = self.display_var.get()
        result = self.calc_controller.process_button(value, current)
        self.display_var.set(result)
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.update_theme()
    
    def hide(self):
        self.frame.pack_forget()