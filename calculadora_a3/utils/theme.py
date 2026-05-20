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
            'bg': '#1e1e1e',
            'primary': '#ecf0f1',
            'secondary': '#5dade2',
            'success': '#2ecc71',
            'danger': '#e74c3c',
            'warning': '#f39c12',
            'white': '#2c2c2c',
            'black': '#ecf0f1',
            'card_bg': '#2c2c2c',
            'entry_bg': '#3c3c3c',
            'entry_fg': '#ecf0f1',
            'button_bg': '#5dade2',
            'button_fg': '#ffffff',
            'display_bg': '#2c2c2c',
            'display_fg': '#ecf0f1'
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