import tkinter as tk
from utils.constants import FUNCIONALIDADES
from assests.style import create_title, create_card

class HomeView:
    def __init__(self, parent, controller, colors):
        self.parent = parent
        self.controller = controller
        self.colors = colors
        self.frame = None
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.parent, bg=self.colors['bg'])
        
        # Título
        title = create_title(self.frame, "Bem-vindo à Calculadora Multifuncional!")
        title.configure(bg=self.colors['bg'], fg=self.colors['primary'])
        title.pack(pady=20)
        
        # Subtítulo
        subtitle = tk.Label(
            self.frame,
            text="Escolha uma das funcionalidades abaixo:",
            font=('Arial', 14),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        )
        subtitle.pack(pady=10)
        
        # Cards das funcionalidades
        cards_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        cards_frame.pack(pady=20)
        
        # Mapeamento de comandos
        commands = {
            'calculator': self.controller.show_calculator,
            'consumo': self.controller.show_consumo,
            'media': self.controller.show_media,
            'imc': self.controller.show_imc,
            'about': self.controller.show_about
        }
        
        for i, (titulo, desc, cmd_name) in enumerate(FUNCIONALIDADES):
            card = create_card(
                cards_frame,
                titulo,
                desc,
                commands[cmd_name],
                colors=self.colors
            )
            card.grid(row=i//2, column=i%2, padx=10, pady=10, sticky='nsew')
            
            # Aplicar tema ao card e seus filhos
            self.apply_card_theme(card)
        
        # Configurar grid
        cards_frame.grid_rowconfigure(0, weight=1)
        cards_frame.grid_rowconfigure(1, weight=1)
        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)
    
    def apply_card_theme(self, card):
        """Aplica o tema ao card"""
        for child in card.winfo_children():
            if isinstance(child, tk.Label):
                if child.cget('fg') != self.colors['success']:
                    child.configure(bg=self.colors['card_bg'], fg=self.colors['primary'])
            elif isinstance(child, tk.Button):
                if child.cget('bg') != self.colors['success']:
                    child.configure(bg=self.colors['button_bg'], fg=self.colors['button_fg'])
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()