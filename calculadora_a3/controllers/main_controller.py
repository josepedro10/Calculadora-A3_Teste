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
from assets.style import StyleManager, create_button

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
        
        # === USAR grid para organizar melhor ===
        self.root.grid_rowconfigure(0, weight=0)  # Header
        self.root.grid_rowconfigure(1, weight=1)  # Conteúdo
        self.root.grid_rowconfigure(2, weight=0)  # Footer
        self.root.grid_columnconfigure(0, weight=1)
        
        # === TOPO (Cabeçalho) ===
        self.header_frame = tk.Frame(self.root, bg=self.colors['bg'], height=80)
        self.header_frame.grid(row=0, column=0, sticky="ew", pady=(10, 0))
        self.header_frame.grid_propagate(False)
        
        # Título (centralizado no topo)
        self.title_label = tk.Label(
            self.header_frame,
            text="CALCULADORA",
            font=('Arial', 24, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['primary']
        )
        self.title_label.pack(expand=True, fill=tk.BOTH)
        
        # === MEIO (Navegação + Conteúdo) ===
        self.middle_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.middle_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        # Configurar grid do middle_frame
        self.middle_frame.grid_rowconfigure(0, weight=0)  # Navegação
        self.middle_frame.grid_rowconfigure(1, weight=1)  # Conteúdo
        self.middle_frame.grid_columnconfigure(0, weight=1)
        
        # Barra de navegação
        self.create_navigation_bar()
        
        # Frame de conteúdo
        self.content_frame = tk.Frame(self.middle_frame, bg=self.colors['bg'])
        self.content_frame.grid(row=1, column=0, sticky="nsew", pady=10)
        
        # === RODAPÉ (Botão de tema) ===
        self.footer_frame = tk.Frame(self.root, bg=self.colors['bg'], height=60)
        self.footer_frame.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        self.footer_frame.grid_propagate(False)
        
        # Botão de tema no canto inferior esquerdo
        self.theme_button = tk.Button(
            self.footer_frame,
            text=f"{THEME_ICONS['light']} Alternar Tema",
            command=self.toggle_theme,
            font=('Arial', 10, 'bold'),
            bg=self.colors['secondary'],
            fg='white',
            relief=tk.RAISED,
            padx=20,
            pady=10
        )
        self.theme_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Teste: Adicionar um label para verificar se o footer está visível
        test_label = tk.Label(
            self.footer_frame,
            text="✓ Tema",
            font=('Arial', 8),
            bg=self.colors['bg'],
            fg=self.colors['success']
        )
        test_label.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Dicionário de views
        self.views = {}
        self.current_view = None
        
        # Inicializar views
        self.init_views()
        
        # Mostrar home
        self.show_home()
    
    def toggle_theme(self):
        """Alterna entre tema claro e escuro"""
        print("Botão de tema clicado!")  # Debug para verificar se o botão funciona
        
        self.colors = self.theme_manager.toggle_theme()
        theme_name = self.theme_manager.get_theme_name()
        icon = THEME_ICONS['dark'] if theme_name == 'Escuro' else THEME_ICONS['light']
        
        # Atualizar botão de tema
        self.theme_button.config(text=f"{icon} Alternar Tema")
        
        # Atualizar cores da interface
        self.root.configure(bg=self.colors['bg'])
        self.header_frame.configure(bg=self.colors['bg'])
        self.title_label.configure(bg=self.colors['bg'], fg=self.colors['primary'])
        self.middle_frame.configure(bg=self.colors['bg'])
        self.content_frame.configure(bg=self.colors['bg'])
        self.footer_frame.configure(bg=self.colors['bg'])
        
        # Atualizar barra de navegação
        for widget in self.nav_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                for btn in widget.winfo_children():
                    if isinstance(btn, tk.Button):
                        btn.configure(bg=self.colors['button_bg'], fg=self.colors['button_fg'])
        
        # Recriar views com novo tema
        self.recreate_views()
    
    def recreate_views(self):
        """Recria todas as views com o novo tema"""
        # Limpar views existentes
        for view in self.views.values():
            if hasattr(view, 'frame') and view.frame:
                view.frame.destroy()
        
        # Recriar views
        self.init_views()
        
        # Mostrar a view atual
        if self.current_view:
            self.show_view(self.current_view)
    
    def create_navigation_bar(self):
        """Cria a barra de navegação"""
        self.nav_frame = tk.Frame(self.middle_frame, bg=self.colors['bg'])
        self.nav_frame.grid(row=0, column=0, sticky="ew", pady=5)
        
        # Frame para centralizar os botões
        center_frame = tk.Frame(self.nav_frame, bg=self.colors['bg'])
        center_frame.pack(expand=True)
        
        nav_buttons = [
            ("🏠 Home", self.show_home),
            ("📊 Calculadora", self.show_calculator),
            ("⚡ Consumo", self.show_consumo),
            ("📈 Média", self.show_media),
            ("⚖️ IMC", self.show_imc),
            ("ℹ️ Sobre", self.show_about)
        ]
        
        for text, command in nav_buttons:
            btn = tk.Button(
                center_frame,
                text=text,
                command=command,
                font=('Arial', 10, 'bold'),
                bg=self.colors['button_bg'],
                fg=self.colors['button_fg'],
                relief=tk.RAISED,
                padx=12,
                pady=6
            )
            btn.pack(side=tk.LEFT, padx=3)
    
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