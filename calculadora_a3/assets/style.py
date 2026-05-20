import tkinter as tk
from tkinter import ttk

class StyleManager:
    def __init__(self, theme_manager):
        self.theme_manager = theme_manager
        self.style = ttk.Style()
        self.style.theme_use('clam')
    
    def update_theme(self):
        """Atualiza o estilo baseado no tema atual"""
        colors = self.theme_manager.get_colors()
        
        self.style.configure('TButton', 
                            background=colors['button_bg'],
                            foreground=colors['button_fg'],
                            font=('Arial', 10))
        
        self.style.configure('TLabelframe', 
                            background=colors['bg'],
                            foreground=colors['primary'])
        
        self.style.configure('TLabelframe.Label', 
                            background=colors['bg'],
                            foreground=colors['primary'])
    
    def apply_theme_to_widget(self, widget, colors):
        """Aplica o tema a um widget e seus filhos recursivamente"""
        try:
            if isinstance(widget, (tk.Frame, tk.LabelFrame)):
                widget.configure(bg=colors['bg'])
            elif isinstance(widget, tk.Label):
                current_fg = widget.cget('fg')
                if current_fg not in [colors['danger'], colors['success'], colors['warning']]:
                    widget.configure(bg=colors['bg'], fg=colors['primary'])
            elif isinstance(widget, tk.Button):
                bg = widget.cget('bg')
                text = widget.cget('text')
                # Botões de navegação sempre pretos
                if text in ['🏠 Home', '📊 Calculadora', '⚡ Consumo', '📈 Média', '⚖️ IMC', 'ℹ️ Sobre']:
                    widget.configure(bg='#000000', fg='white')
                elif bg not in [colors['danger'], colors['success'], colors['warning']]:
                    widget.configure(bg=colors['button_bg'], fg=colors['button_fg'])
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=colors['entry_bg'], fg=colors['entry_fg'],
                               insertbackground=colors['entry_fg'])
        except:
            pass
        
        for child in widget.winfo_children():
            self.apply_theme_to_widget(child, colors)
    
    def apply_theme_to_app(self, root, content_frame, nav_frame, colors):
        """Aplica o tema à aplicação inteira"""
        root.configure(bg=colors['bg'])
        content_frame.configure(bg=colors['bg'])
        nav_frame.configure(bg=colors['bg'])
        self.apply_theme_to_widget(root, colors)

def create_button(parent, text, command, **kwargs):
    """Cria um botão padronizado"""
    default_kwargs = {
        'font': ('Arial', 10),
        'relief': tk.RAISED,
        'padx': 10,
        'pady': 5
    }
    default_kwargs.update(kwargs)
    return tk.Button(parent, text=text, command=command, **default_kwargs)

def create_title(parent, text, **kwargs):
    """Cria um título padronizado"""
    default_kwargs = {
        'font': ('Arial', 20, 'bold'),
    }
    default_kwargs.update(kwargs)
    return tk.Label(parent, text=text, **default_kwargs)

def create_card(parent, title, description, command, colors=None, **kwargs):
    """Cria um card padronizado"""
    if colors is None:
        colors = {
            'card_bg': '#ffffff',
            'secondary': '#3498db',
            'primary': '#2c3e50',
            'success': '#27ae60'
        }
    
    card = tk.Frame(
        parent,
        bg=colors['card_bg'],
        relief=tk.RAISED,
        bd=2
    )
    
    tk.Label(
        card,
        text=title,
        font=('Arial', 14, 'bold'),
        bg=colors['card_bg'],
        fg=colors['secondary']
    ).pack(pady=10)
    
    tk.Label(
        card,
        text=description,
        font=('Arial', 10),
        bg=colors['card_bg'],
        fg=colors['primary'],
        justify=tk.CENTER
    ).pack(pady=5)
    
    tk.Button(
        card,
        text="Acessar",
        command=command,
        bg=colors['success'],
        fg='white',
        relief=tk.RAISED,
        padx=20,
        pady=5
    ).pack(pady=10)
    
    return card