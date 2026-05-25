import tkinter as tk
from assets.style import create_title

class AboutView:
    def __init__(self, parent, controller, colors):
        self.parent = parent
        self.controller = controller
        self.colors = colors
        self.frame = None
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.parent, bg=self.colors['bg'])
        
        # Título
        title = create_title(self.frame, "Sobre o Projeto", fg=self.colors['primary'])
        title.configure(bg=self.colors['bg'])
        title.pack(pady=20)
        
        # Frame principal com scrollbar
        main_container = tk.Frame(self.frame, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Criar canvas e scrollbar para rolagem
        canvas = tk.Canvas(main_container, bg=self.colors['bg'], highlightthickness=0)
        scrollbar = tk.Scrollbar(main_container, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=canvas.winfo_reqwidth())
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Configurar para expandir
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # ========== CONTEÚDO DA PÁGINA SOBRE ==========
        
        # Card 1: Título do Projeto
        card1 = tk.Frame(
            scrollable_frame,
            bg=self.colors['card_bg'],
            relief=tk.RAISED,
            bd=2
        )
        card1.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            card1,
            text="📱 Calculadora Multifuncional",
            font=('Arial', 16, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['secondary']
        ).pack(pady=(15, 5), padx=15)
        
        tk.Label(
            card1,
            text="Projeto desenvolvido com Python e Tkinter",
            font=('Arial', 11),
            bg=self.colors['card_bg'],
            fg=self.colors['primary']
        ).pack(pady=(0, 15), padx=15)
        
        # Card 2: Integrantes
        card2 = tk.Frame(
            scrollable_frame,
            bg=self.colors['card_bg'],
            relief=tk.RAISED,
            bd=2
        )
        card2.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            card2,
            text="👥 Integrantes",
            font=('Arial', 14, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['secondary']
        ).pack(pady=(15, 5), padx=15, anchor='w')
        
        tk.Label(
            card2,
            text="Equipe de Desenvolvimento:",
            font=('Arial', 11, 'italic'),
            bg=self.colors['card_bg'],
            fg=self.colors['primary']
        ).pack(pady=(5, 5), padx=15, anchor='w')
        
        # Lista de integrantes
        integrantes_frame = tk.Frame(card2, bg=self.colors['card_bg'])
        integrantes_frame.pack(pady=(5, 15), padx=15, anchor='w')
        
        integrantes = [
            "  • João Silva - Desenvolvedor Backend",
            "  • Maria Santos - Desenvolvedora Frontend",
            "  • Pedro Oliveira - Designer UI/UX",
            "  • Ana Costa - Testadora QA"
        ]
        
        for integrante in integrantes:
            tk.Label(
                integrantes_frame,
                text=integrante,
                font=('Arial', 10),
                bg=self.colors['card_bg'],
                fg=self.colors['primary']
            ).pack(anchor='w', pady=2)
        
        # Card 3: Tecnologias
        card3 = tk.Frame(
            scrollable_frame,
            bg=self.colors['card_bg'],
            relief=tk.RAISED,
            bd=2
        )
        card3.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            card3,
            text="🛠️ Tecnologias Utilizadas",
            font=('Arial', 14, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['secondary']
        ).pack(pady=(15, 10), padx=15, anchor='w')
        
        tecnologias_frame = tk.Frame(card3, bg=self.colors['card_bg'])
        tecnologias_frame.pack(pady=(5, 15), padx=15, anchor='w')
        
        tecnologias = [
            "  • Python 3.x",
            "  • Tkinter (GUI)",
            "  • Math Library"
        ]
        
        for tech in tecnologias:
            tk.Label(
                tecnologias_frame,
                text=tech,
                font=('Arial', 10),
                bg=self.colors['card_bg'],
                fg=self.colors['primary']
            ).pack(anchor='w', pady=2)
        
        # Card 4: Funcionalidades
        card4 = tk.Frame(
            scrollable_frame,
            bg=self.colors['card_bg'],
            relief=tk.RAISED,
            bd=2
        )
        card4.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            card4,
            text="⚙️ Funcionalidades",
            font=('Arial', 14, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['secondary']
        ).pack(pady=(15, 10), padx=15, anchor='w')
        
        funcionalidades_frame = tk.Frame(card4, bg=self.colors['card_bg'])
        funcionalidades_frame.pack(pady=(5, 15), padx=15, anchor='w')
        
        funcionalidades = [
            "  • Calculadora básica",
            "  • Cálculo de consumo de energia",
            "  • Cálculo de média",
            "  • Cálculo de IMC",
            "  • Modo claro/escuro",
            "  • Interface com navegação entre telas"
        ]
        
        for func in funcionalidades:
            tk.Label(
                funcionalidades_frame,
                text=func,
                font=('Arial', 10),
                bg=self.colors['card_bg'],
                fg=self.colors['primary']
            ).pack(anchor='w', pady=2)
        
        # Card 5: Objetivo
        card5 = tk.Frame(
            scrollable_frame,
            bg=self.colors['card_bg'],
            relief=tk.RAISED,
            bd=2
        )
        card5.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            card5,
            text="🎯 Objetivo",
            font=('Arial', 14, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['secondary']
        ).pack(pady=(15, 10), padx=15, anchor='w')
        
        tk.Label(
            card5,
            text="Desenvolver uma aplicação prática que ofereça múltiplas\n"
                 "ferramentas de cálculo em uma interface amigável e intuitiva.",
            font=('Arial', 11),
            bg=self.colors['card_bg'],
            fg=self.colors['primary'],
            justify=tk.LEFT
        ).pack(pady=(0, 15), padx=15, anchor='w')
        
        # Card 6: Versão e Data
        card6 = tk.Frame(
            scrollable_frame,
            bg=self.colors['card_bg'],
            relief=tk.RAISED,
            bd=2
        )
        card6.pack(fill=tk.X, padx=10, pady=10)
        
        info_frame = tk.Frame(card6, bg=self.colors['card_bg'])
        info_frame.pack(fill=tk.X, pady=15, padx=15)
        
        tk.Label(
            info_frame,
            text="📅 Versão: 2.0",
            font=('Arial', 10, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['primary']
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Label(
            info_frame,
            text="📝 Desenvolvido em: 2024",
            font=('Arial', 10, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['primary']
        ).pack(side=tk.RIGHT, padx=10)
        
        # Espaço extra no final
        tk.Frame(scrollable_frame, height=20, bg=self.colors['bg']).pack()
        
        # Configurar largura mínima do canvas
        def configure_canvas_width(event):
            canvas.itemconfig(1, width=event.width)
        
        canvas.bind('<Configure>', configure_canvas_width)
    
    def update_colors(self):
        """Atualiza as cores quando o tema muda"""
        if self.frame:
            self.frame.configure(bg=self.colors['bg'])
            
            # Atualizar todos os widgets recursivamente
            for widget in self.frame.winfo_children():
                self.update_widget_colors(widget)
    
    def update_widget_colors(self, widget):
        """Atualiza as cores de um widget e seus filhos"""
        try:
            if isinstance(widget, tk.Frame):
                widget.configure(bg=self.colors['bg'])
            elif isinstance(widget, tk.Label):
                current_fg = widget.cget('fg')
                if current_fg not in [self.colors['danger'], self.colors['success'], self.colors['warning']]:
                    widget.configure(bg=self.colors['bg'], fg=self.colors['primary'])
            elif isinstance(widget, tk.Button):
                widget.configure(bg=self.colors['button_bg'], fg=self.colors['button_fg'])
            elif isinstance(widget, tk.Canvas):
                widget.configure(bg=self.colors['bg'])
        except:
            pass
        
        for child in widget.winfo_children():
            self.update_widget_colors(child)
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()