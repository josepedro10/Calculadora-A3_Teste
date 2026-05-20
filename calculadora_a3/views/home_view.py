import tkinter as tk
from utils.constants import FUNCIONALIDADES
from assets.style import create_title, create_card

class HomeView:
    def __init__(self, parent, controller, colors):
        self.parent = parent
        self.controller = controller
        self.colors = colors
        self.frame = None
        self.cards = []
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.parent, bg=self.colors['bg'])
        
        # Título
        title = create_title(self.frame, "Bem-vindo à Calculadora Multifuncional!")
        title.configure(bg=self.colors['bg'], fg=self.colors['primary'])
        title.pack(pady=20)
        
       # Subtítulo com duas linhas (usando \n para quebra de linha)
        subtitle = tk.Label(
            self.frame,
            text="Escolha uma das funcionalidades abaixo:\nClique no card acima para acessar",
            font=('Arial', 14),
            bg=self.colors['bg'],
            fg=self.colors['primary'],
            justify=tk.CENTER
        )
        subtitle.pack(pady=10)
        
        # Frame para os cards
        cards_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        cards_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
        
        # Configurar grid para 3 colunas (para centralizar melhor)
        # Para 5 cards, usar 3 colunas: Linha 1: 3 cards, Linha 2: 2 cards centralizados
        for i in range(3):
            cards_frame.grid_columnconfigure(i, weight=1)
        for i in range(2):
            cards_frame.grid_rowconfigure(i, weight=1)
        
        # Mapeamento de comandos
        commands = {
            'calculator': self.controller.show_calculator,
            'consumo': self.controller.show_consumo,
            'media': self.controller.show_media,
            'imc': self.controller.show_imc,
            'about': self.controller.show_about
        }
        
        # Criar cards com tamanho fixo e mesmo espaçamento
        for i, (titulo, desc, cmd_name) in enumerate(FUNCIONALIDADES):
            card = self.create_fixed_card(
                cards_frame,
                titulo,
                desc,
                commands[cmd_name]
            )
            
            # Posicionamento estratégico para centralizar o Sobre
            if cmd_name == 'about':  # Card Sobre
                row = 1  # Segunda linha
                col = 1  # Coluna do meio (centralizado)
            else:
                row = i // 3  # Primeira linha para os 3 primeiros
                col = i % 3   # Colunas 0, 1, 2
            
            card.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
            self.cards.append(card)
        
        # Ajustar tamanho mínimo dos cards
        for card in self.cards:
            card.grid_propagate(False)  # Impede que o card redimensione
            card.config(width=200, height=180)  # Tamanho fixo para todos
    
    def create_fixed_card(self, parent, title, description, command):
        """Cria um card com tamanho fixo e texto ajustado"""
        colors = self.colors
        
        card = tk.Frame(
            parent,
            bg=colors['card_bg'],
            relief=tk.RAISED,
            bd=2,
            width=200,
            height=180
        )
        card.pack_propagate(False)  # Mantém o tamanho fixo
        
        # Título do card
        tk.Label(
            card,
            text=title,
            font=('Arial', 14, 'bold'),
            bg=colors['card_bg'],
            fg=colors['secondary']
        ).pack(pady=(15, 5))
        
        # Descrição do card (com quebra de linha)
        tk.Label(
            card,
            text=description,
            font=('Arial', 10),
            bg=colors['card_bg'],
            fg=colors['primary'],
            justify=tk.CENTER,
            wraplength=160
        ).pack(pady=5, expand=True, fill=tk.BOTH)
        
        # Botão do card
        tk.Button(
            card,
            text="Acessar",
            command=command,
            bg=colors['success'],
            fg='white',
            relief=tk.RAISED,
            padx=20,
            pady=5
        ).pack(pady=(5, 15))
        
        return card
    
    def update_colors(self):
        """Atualiza as cores quando o tema muda"""
        if self.frame:
            self.frame.configure(bg=self.colors['bg'])
            
            for widget in self.frame.winfo_children():
                if isinstance(widget, tk.Label):
                    if widget.cget('text') == "Clique no card para acessar":
                        widget.configure(bg=self.colors['bg'], fg=self.colors['secondary'])
                    else:
                        widget.configure(bg=self.colors['bg'], fg=self.colors['primary'])
                elif isinstance(widget, tk.Frame):
                    widget.configure(bg=self.colors['bg'])
                    for card in widget.winfo_children():
                        if isinstance(card, tk.Frame):
                            card.configure(bg=self.colors['card_bg'])
                            for item in card.winfo_children():
                                if isinstance(item, tk.Label):
                                    if item.cget('text') != 'Acessar':
                                        item.configure(bg=self.colors['card_bg'], fg=self.colors['primary'])
                                elif isinstance(item, tk.Button):
                                    if item.cget('text') == 'Acessar':
                                        item.configure(bg=self.colors['success'])
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()