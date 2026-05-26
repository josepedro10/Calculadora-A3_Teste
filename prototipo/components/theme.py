# -*- coding: utf-8 -*-
"""
Gerenciamento de Cores e Estilos (Temas) para o Tkinter.
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
    
    DARK_PALETTE = {
        "bg_window": "#363636",
        "bg_card": "#454545",
        "text_main": "#FFFFFF",
        "text_muted": "#A5A5A5",
        "text_dark": "#000000",
        "bg_input": "#EAEAEA",
        "fg_input": "#000000",
        "bg_display": "#FFFFFF",
        "fg_display": "#000000",
        "bg_btn_num": "#FFFFFF",
        "fg_btn_num": "#000000",
        "bg_btn_gray": "#A5A5A5",
        "fg_btn_gray": "#000000",
        "bg_btn_orange": "#E67E22",
        "fg_btn_orange": "#FFFFFF",
        "bg_btn_primary": "#FFFFFF",
        "fg_btn_primary": "#000000",
        "bg_btn_action": "#D35400",
        "fg_btn_action": "#FFFFFF",
        "bg_badge": "#FFFFFF",
        "fg_badge": "#000000"
    }
    
    LIGHT_PALETTE = {
        "bg_window": "#EAEAEA",
        "bg_card": "#D8D8D8",
        "text_main": "#000000",
        "text_muted": "#666666",
        "text_dark": "#FFFFFF",
        "bg_input": "#4C4C4C",
        "fg_input": "#FFFFFF",
        "bg_display": "#FFFFFF",
        "fg_display": "#000000",
        "bg_btn_num": "#4C4C4C",
        "fg_btn_num": "#FFFFFF",
        "bg_btn_gray": "#A5A5A5",
        "fg_btn_gray": "#000000",
        "bg_btn_orange": "#E67E22",
        "fg_btn_orange": "#FFFFFF",
        "bg_btn_primary": "#4C4C4C",
        "fg_btn_primary": "#FFFFFF",
        "bg_btn_action": "#D35400",
        "fg_btn_action": "#FFFFFF",
        "bg_badge": "#4C4C4C",
        "fg_badge": "#FFFFFF"
    }

    @classmethod
    def get_palette(cls, mode: str) -> dict:
        if mode == "DARK":
            return cls.DARK_PALETTE
        return cls.LIGHT_PALETTE