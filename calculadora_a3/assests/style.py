import tkinter as tk
from tkinter import ttk
from utils.constants import THEME_ICONS

class StyleManager:
    def __init__(self, theme_manager):
        self.theme_manager = theme_manager
        self.style = ttk.Style()
        self.style.theme_use('clam')
    
    def update_theme(self):
        """Atualiza o estilo baseado no tema atual"""
        colors = self.theme_manager.get_colors()
        
        # Configurar estilo para botões ttk
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
                # Não mudar a cor se for específica (ex: mensagens de erro)
                if current_fg not in [colors['danger'], colors['success'], colors['warning']]:
                    widget.configure(bg=colors['bg'], fg=colors['primary'])
            elif isinstance(widget, tk.Button):
                bg = widget.cget('bg')
                # Botões especiais mantêm suas cores
                if bg not in [colors['danger'], colors['success'], colors['warning']]:
                    widget.configure(bg=colors['button_bg'], fg=colors['button_fg'])
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=colors['entry_bg'], fg=colors['entry_fg'],
                               insertbackground=colors['entry_fg'])
            elif isinstance(widget, tk.Text):
                widget.configure(bg=colors['entry_bg'], fg=colors['entry_fg'])
            elif isinstance(widget, tk.Listbox):
                widget.configure(bg=colors['entry_bg'], fg=colors['entry_fg'])
        except:
            pass
        
        # Aplicar aos filhos
        for child in widget.winfo_children():
            self.apply_theme_to_widget(child, colors)
    
    def apply_theme_to_app(self, root, content_frame, nav_frame, colors):
        """Aplica o tema à aplicação inteira"""
        root.configure(bg=colors['bg'])
        content_frame.configure(bg=colors['bg'])
        nav_frame.configure(bg=colors['bg'])
        
        # Aplicar a todos os widgets
        self.apply_theme_to_widget(root, colors)

def create_button(parent, text, command, **kwargs):
    """Cria um botão padronizado"""
    from utils.constants import THEMES
    colors = THEMES['light']['colors']  # Será atualizado dinamicamente
    
    default_kwargs = {
        'font': ('Arial', 10),
        'relief': tk.RAISED,
        'padx': 10,
        'pady': 5
    }
    default_kwargs.update(kwargs)
    
    # Se não especificou bg e fg, usa as cores do tema
    if 'bg' not in kwargs:
        default_kwargs['bg'] = colors['button_bg']
    if 'fg' not in kwargs:
        default_kwargs['fg'] = colors['button_fg']
    
    return tk.Button(parent, text=text, command=command, **default_kwargs)

def create_title(parent, text, **kwargs):
    """Cria um título padronizado"""
    from utils.constants import THEMES
    colors = THEMES['light']['colors']
    
    default_kwargs = {
        'font': ('Arial', 20, 'bold'),
        'bg': colors['bg']
    }
    default_kwargs.update(kwargs)
    
    if 'fg' not in kwargs:
        default_kwargs['fg'] = colors['primary']
    
    return tk.Label(parent, text=text, **default_kwargs)

def create_card(parent, title, description, command, colors=None, **kwargs):
    """Cria um card padronizado"""
    if colors is None:
        from utils.constants import THEMES
        colors = THEMES['light']['colors']
    
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