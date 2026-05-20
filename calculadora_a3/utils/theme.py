# Temas da aplicação
THEMES = {
    'light': {
        'name': 'Claro',
        'colors': {
            'bg': '#f0f0f0',
            'primary': '#2c3e50',
            'secondary': '#3498db',
            'success': '#27ae60',
            'danger': '#e74c3c',
            'warning': '#f39c12',
            'white': '#ffffff',
            'black': '#000000',
            'card_bg': '#ffffff',
            'entry_bg': '#ffffff',
            'entry_fg': '#000000',
            'button_bg': '#3498db',
            'button_fg': '#ffffff',
            'display_bg': '#ffffff',
            'display_fg': '#000000'
        }
    },
    'dark': {
        'name': 'Escuro',
        'colors': {
            'bg': '#1e1e1e',        # Fundo principal escuro
            'primary': '#ecf0f1',    # Texto claro
            'secondary': '#5dade2',  # Azul claro
            'success': '#2ecc71',    # Verde
            'danger': '#e74c3c',     # Vermelho
            'warning': '#f39c12',    # Laranja
            'white': '#2c2c2c',      # Cinza escuro para cards
            'black': '#000000',      # Preto
            'card_bg': '#2c2c2c',    # Fundo dos cards escuro
            'entry_bg': '#3c3c3c',   # Fundo inputs escuro
            'entry_fg': '#ecf0f1',   # Texto inputs claro
            'button_bg': '#000000',  # Botões PRETOS no tema escuro
            'button_fg': '#ffffff',  # Texto branco
            'display_bg': '#2c2c2c', # Display calculadora escuro
            'display_fg': '#ecf0f1'  # Texto display claro
        }
    }
}

class ThemeManager:
    def __init__(self):
        self.current_theme = 'light'
    
    def get_colors(self):
        return THEMES[self.current_theme]['colors']
    
    def toggle_theme(self):
        self.current_theme = 'dark' if self.current_theme == 'light' else 'light'
        return self.get_colors()
    
    def get_theme_name(self):
        return THEMES[self.current_theme]['name']