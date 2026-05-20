import tkinter as tk
import sys
import os

# Adiciona o diretório pai ao path para imports absolutos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from views.home_view import HomeView
from views.calculator_view import CalculatorView
from views.consumo_view import ConsumoView
from views.media_view import MediaView
from views.imc_view import IMCView
from views.about_view import AboutView
from utils.constants import WINDOW_CONFIG, THEME_ICONS
from utils.theme import ThemeManager
from assets.style import StyleManager

class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_CONFIG['title'])
        self.root.geometry(f"{WINDOW_CONFIG['width']}x{WINDOW_CONFIG['height']}")
        self.root.resizable(True, True)
        
        # Gerenciadores de tema
        self.theme_manager = ThemeManager()
        self.style_manager = StyleManager(self.theme_manager)
        self.colors = self.theme_manager.get_colors()
        
        self.root.configure(bg=self.colors['bg'])
        
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        self.title_label = tk.Label(
            self.main_frame,
            text="CALCULADORA",
            font=('Arial', 24, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        )
        self.title_label.pack(pady=10)
        
        # Barra de navegação (com botão de tema)
        self.create_navigation_bar()
        
        # Frame de conteúdo
        self.content_frame = tk.Frame(self.main_frame, bg=self.colors['bg'])
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Dicionário de views
        self.views = {}
        self.current_view = None
        
        # Inicializar views
        self.init_views()
        
        # Mostrar home
        self.show_home()
    
    def create_navigation_bar(self):
        """Cria a barra de navegação com botões pretos e botão de tema preto"""
        self.nav_frame = tk.Frame(self.main_frame, bg=self.colors['bg'])
        self.nav_frame.pack(fill=tk.X, pady=5)
        
        # Frame para centralizar os botões
        center_frame = tk.Frame(self.nav_frame, bg=self.colors['bg'])
        center_frame.pack(expand=True)
        
        # Lista de botões
        nav_buttons = [
            ("🏠 Home", self.show_home),
            ("📊 Calculadora", self.show_calculator),
            ("⚡ Consumo", self.show_consumo),
            ("📈 Média", self.show_media),
            ("⚖️ IMC", self.show_imc),
            ("ℹ️ Sobre", self.show_about),
        ]
        
        # Criar botões de navegação (todos pretos)
        for text, command in nav_buttons:
            btn = tk.Button(
                center_frame,
                text=text,
                command=command,
                font=('Arial', 10, 'bold'),
                bg='#000000',  # PRETO
                fg='white',     # Texto branco
                relief=tk.RAISED,
                padx=12,
                pady=6,
                activebackground='#333333',
                activeforeground='white'
            )
            btn.pack(side=tk.LEFT, padx=3)
        
        # Botão de tema (TAMBÉM PRETO, igual aos outros)
        self.theme_button = tk.Button(
            center_frame,
            text=f"{THEME_ICONS['light']} Tema",
            command=self.toggle_theme,
            font=('Arial', 10, 'bold'),
            bg='#000000',  # PRETO (igual aos outros)
            fg='white',     # Texto branco
            relief=tk.RAISED,
            padx=12,
            pady=6,
            activebackground='#333333',
            activeforeground='white'
        )
        self.theme_button.pack(side=tk.LEFT, padx=3)
    
    def toggle_theme(self):
        """Alterna entre tema claro e escuro"""
        self.colors = self.theme_manager.toggle_theme()
        theme_name = self.theme_manager.get_theme_name()
        icon = THEME_ICONS['dark'] if theme_name == 'Escuro' else THEME_ICONS['light']
        
        # Atualizar botão de tema (mantém preto)
        self.theme_button.config(text=f"{icon} Tema", bg='#000000', fg='white')
        
        # Atualizar cores principais
        self.root.configure(bg=self.colors['bg'])
        self.main_frame.configure(bg=self.colors['bg'])
        self.title_label.configure(bg=self.colors['bg'], fg=self.colors['primary'])
        self.nav_frame.configure(bg=self.colors['bg'])
        self.content_frame.configure(bg=self.colors['bg'])
        
        # Manter TODOS os botões da navegação PRETOS
        for widget in self.nav_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg=self.colors['bg'])
                for btn in widget.winfo_children():
                    if isinstance(btn, tk.Button):
                        btn.configure(bg='#000000', fg='white')
        
        # Atualizar cores das views
        self.update_views_colors()
        
        # Recriar views
        self.recreate_views()
    
    def update_views_colors(self):
        """Atualiza as cores de todas as views"""
        for view in self.views.values():
            if hasattr(view, 'update_colors'):
                view.update_colors()
    
    def recreate_views(self):
        """Recria todas as views com o novo tema"""
        current = self.current_view
        
        # Limpar views existentes
        for view in self.views.values():
            if hasattr(view, 'frame') and view.frame:
                view.frame.destroy()
        
        # Recriar views
        self.init_views()
        
        # Mostrar a view atual
        if current:
            self.show_view(current)
    
    def init_views(self):
        """Inicializa todas as views"""
        self.views['home'] = HomeView(self.content_frame, self, self.colors)
        self.views['calculator'] = CalculatorView(self.content_frame, self, self.colors)
        self.views['consumo'] = ConsumoView(self.content_frame, self, self.colors)
        self.views['media'] = MediaView(self.content_frame, self, self.colors)
        self.views['imc'] = IMCView(self.content_frame, self, self.colors)
        self.views['about'] = AboutView(self.content_frame, self, self.colors)
    
    def show_view(self, view_name):
        """Mostra uma view específica"""
        if self.current_view and self.current_view in self.views:
            self.views[self.current_view].hide()
        
        self.current_view = view_name
        self.views[view_name].show()
    
    def show_home(self):
        self.show_view('home')
    
    def show_calculator(self):
        self.show_view('calculator')
    
    def show_consumo(self):
        self.show_view('consumo')
    
    def show_media(self):
        self.show_view('media')
    
    def show_imc(self):
        self.show_view('imc')
    
    def show_about(self):
        self.show_view('about')
    
    def run(self):
        """Inicia a aplicação"""
        self.root.mainloop()