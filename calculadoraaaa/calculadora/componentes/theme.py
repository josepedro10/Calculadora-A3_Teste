# -*- coding: utf-8 -*-
"""
Gerenciamento de Cores e Estilos (Temas) para o Tkinter.
Centraliza as configurações visuais para Modo Claro e Modo Escuro.
"""

class ThemeConfig:
    # Fontes
    FONT_SERIF_BOLD = ("Georgia", 24, "bold")
    FONT_SERIF_SMALL = ("Georgia", 12, "bold")
    FONT_TITLE = ("Helvetica", 16, "bold")
    FONT_SUBTITLE = ("Helvetica", 11)
    FONT_MONO_LARGE = ("Consolas", 32, "bold")
    FONT_MONO_MEDIUM = ("Consolas", 14, "bold")
    FONT_DEFAULT = ("Helvetica", 10)
    FONT_LABEL = ("Helvetica", 10, "bold")
    
    # ======== TEMA ESCURO (Dark Mode) - Top Row Figma ========
    DARK_PALETTE = {
        "bg_window": "#363636",         # Cor do fundo principal
        "bg_card": "#454545",           # Fundo do card central da Home
        "text_main": "#FFFFFF",         # Texto geral em branco
        "text_muted": "#A5A5A5",        # Texto de menu inativo
        "text_dark": "#000000",         # Texto escuro para contrastes
        
        # Elementos de Input/Display
        "bg_input": "#EAEAEA",          # Campos de entrada cinza claro
        "fg_input": "#000000",          # Cor de digitação
        "bg_display": "#FFFFFF",        # Janela de resultado de calculadora
        "fg_display": "#000000",        # Texto do display
        
        # Botões calculadora
        "bg_btn_num": "#FFFFFF",        # Botões de números (brancos)
        "fg_btn_num": "#000000",        # Texto de números (pretos)
        "bg_btn_gray": "#A5A5A5",       # AC, +/-, % (cinza)
        "fg_btn_gray": "#000000",
        "bg_btn_orange": "#E67E22",     # Operadores (laranja)
        "fg_btn_orange": "#FFFFFF",
        
        # Botões principais
        "bg_btn_primary": "#FFFFFF",    # "Entrar" na Home
        "fg_btn_primary": "#000000",
        "bg_btn_action": "#D35400",     # "Calcular ..." (laranja escuro)
        "fg_btn_action": "#FFFFFF",
        
        # Badge de Tema (Tema Claro)
        "bg_badge": "#FFFFFF",
        "fg_badge": "#000000"
    }
    
    # ======== TEMA CLARO (Light Mode) - Bottom Row Figma ========
    LIGHT_PALETTE = {
        "bg_window": "#EAEAEA",         # Cor de fundo clara
        "bg_card": "#D8D8D8",           # Fundo do card central da Home
        "text_main": "#000000",         # Texto geral em preto
        "text_muted": "#666666",        # Texto de menu inativo
        "text_dark": "#FFFFFF",         # Texto claro para contrastes
        
        # Elementos de Input/Display
        "bg_input": "#4C4C4C",          # Campos de entrada cinza escuro
        "fg_input": "#FFFFFF",          # Cor de digitação
        "bg_display": "#FFFFFF",        # Janela de resultado de calculadora
        "fg_display": "#000000",        # Texto do display
        
        # Botões calculadora
        "bg_btn_num": "#4C4C4C",        # Botões de números (cinza escuro)
        "fg_btn_num": "#FFFFFF",        # Texto de números (brancos)
        "bg_btn_gray": "#A5A5A5",       # AC, +/-, % (cinza)
        "fg_btn_gray": "#000000",
        "bg_btn_orange": "#E67E22",     # Operadores (laranja)
        "fg_btn_orange": "#FFFFFF",
        
        # Botões principais
        "bg_btn_primary": "#4C4C4C",    # "Entrar" na Home
        "fg_btn_primary": "#FFFFFF",
        "bg_btn_action": "#D35400",     # "Calcular ..." (laranja escuro)
        "fg_btn_action": "#FFFFFF",
        
        # Badge de Tema (Tema Escuro)
        "bg_badge": "#4C4C4C",
        "fg_badge": "#FFFFFF"
    }

    @classmethod
    def get_palette(cls, mode: str) -> dict:
        """Retorna o dicionário com as cores do modo ativo ('DARK' ou 'LIGHT')"""
        if mode == "DARK":
            return cls.DARK_PALETTE
        return cls.LIGHT_PALETTE
