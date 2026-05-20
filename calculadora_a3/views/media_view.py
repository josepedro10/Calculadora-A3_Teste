import tkinter as tk
from tkinter import messagebox
from assets.style import create_title, create_button
from controllers.media_controller import MediaController

class MediaView:
    def __init__(self, parent, controller, colors):
        self.parent = parent
        self.main_controller = controller
        self.media_controller = MediaController()
        self.colors = colors
        self.frame = None
        self.notas_entries = []
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.parent, bg=self.colors['bg'])
        
        # Título
        title = create_title(self.frame, "Calculadora de Média", fg=self.colors['secondary'])
        title.configure(bg=self.colors['bg'])
        title.pack(pady=20)
        
        # Frame para notas
        self.notas_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        self.notas_frame.pack(pady=10)
        
        # Botões
        botoes_frame = tk.Frame(self.frame, bg=self.colors['bg'])
        botoes_frame.pack(pady=20)
        
        adicionar_btn = create_button(
            botoes_frame,
            "+ Adicionar Nota",
            self.adicionar_nota,
            bg=self.colors['secondary'],
            fg='white'
        )
        adicionar_btn.pack(side=tk.LEFT, padx=5)
        
        calcular_btn = create_button(
            botoes_frame,
            "Calcular Média",
            self.calcular_media,
            bg=self.colors['success'],
            fg='white'
        )
        calcular_btn.pack(side=tk.LEFT, padx=5)
        
        # Adicionar campos iniciais
        for _ in range(2):
            self.adicionar_nota()
    
    def adicionar_nota(self):
        entry_frame = tk.Frame(self.notas_frame, bg=self.colors['bg'])
        entry_frame.pack(pady=5)
        
        nota_entry = tk.Entry(
            entry_frame, 
            font=('Arial', 12), 
            width=15,
            bg=self.colors['entry_bg'],
            fg=self.colors['entry_fg'],
            insertbackground=self.colors['entry_fg']
        )
        nota_entry.pack(side=tk.LEFT, padx=5)
        
        def remover_nota():
            entry_frame.destroy()
            self.notas_entries.remove(nota_entry)
        
        remover_btn = tk.Button(
            entry_frame,
            text="❌",
            command=remover_nota,
            font=('Arial', 10),
            bg=self.colors['danger'],
            fg='white',
            relief=tk.RAISED
        )
        remover_btn.pack(side=tk.LEFT)
        
        self.notas_entries.append(nota_entry)
    
    def calcular_media(self):
        valores = [entry.get() for entry in self.notas_entries if entry.get()]
        success, resultado = self.media_controller.calcular_media(valores)
        
        if success:
            messagebox.showinfo("Resultado", resultado)
        else:
            messagebox.showerror("Erro", resultado)
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()