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
        
        # Informações
        info_frame = tk.Frame(self.frame, bg=self.colors['card_bg'], relief=tk.RAISED, bd=2)
        info_frame.pack(pady=20, padx=20, fill=tk.BOTH)
        
        informacoes = [
            ("📱 Calculadora Multifuncional", "Projeto desenvolvido com Python e Tkinter"),
            ("👥 Integrantes:", "Equipe de Desenvolvimento"),
            ("   • João Silva - Desenvolvedor Backend", ""),
            ("   • Maria Santos - Desenvolvedora Frontend", ""),
            ("   • Pedro Oliveira - Designer UI/UX", ""),
            ("   • Ana Costa - Testadora QA", ""),
            ("", ""),
            ("🛠️ Tecnologias Utilizadas:", ""),
            ("   • Python 3.x", ""),
            ("   • Tkinter (GUI)", ""),
            ("   • Math Library", ""),
            ("", ""),
            ("⚙️ Funcionalidades:", ""),
            ("   • Calculadora básica", ""),
            ("   • Cálculo de consumo de energia", ""),
            ("   • Cálculo de média", ""),
            ("   • Cálculo de IMC", ""),
            ("   • Modo claro/escuro", ""),
            ("", ""),
            ("🎯 Objetivo:", ""),
            ("   Desenvolver uma aplicação prática que"),
            ("   ofereça múltiplas ferramentas de cálculo"),
            ("   em uma interface amigável e intuitiva."),
            ("", ""),
            ("🎨 Temas:", ""),
            ("   • Modo Claro 🌞", ""),
            ("   • Modo Escuro 🌙", ""),
            ("", ""),
            ("📅 Versão: 2.0", ""),
            ("📝 Desenvolvido em: 2024", "")
        ]
        
        for texto, subtexto in informacoes:
            if subtexto:
                tk.Label(
                    info_frame,
                    text=texto,
                    font=('Arial', 12, 'bold'),
                    bg=self.colors['card_bg'],
                    fg=self.colors['primary'],
                    justify=tk.LEFT
                ).pack(anchor='w', padx=20, pady=(10, 0))
                
                if subtexto:
                    tk.Label(
                        info_frame,
                        text=subtexto,
                        font=('Arial', 10),
                        bg=self.colors['card_bg'],
                        fg=self.colors['primary'],
                        justify=tk.LEFT
                    ).pack(anchor='w', padx=40, pady=(0, 5))
            else:
                tk.Label(
                    info_frame,
                    text=texto,
                    font=('Arial', 11),
                    bg=self.colors['card_bg'],
                    fg=self.colors['primary'],
                    justify=tk.LEFT
                ).pack(anchor='w', padx=20, pady=2)
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()