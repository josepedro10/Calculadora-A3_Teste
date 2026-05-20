import math

class CalculatorModel:
    def __init__(self):
        self.current_operation = ""
    
    def evaluate_expression(self, expression):
        """Avalia uma expressão matemática"""
        try:
            result = eval(expression)
            return str(result)
        except:
            return "Erro"
    
    def calculate_percentage(self, value):
        """Calcula porcentagem"""
        try:
            result = eval(value) / 100
            return str(result)
        except:
            return "Erro"
    
    def calculate_square_root(self, value):
        """Calcula raiz quadrada"""
        try:
            result = math.sqrt(eval(value))
            return str(result)
        except:
            return "Erro"
    
    def add_character(self, current, char):
        """Adiciona caractere à operação atual"""
        if current == "0" or current == "Erro":
            return char
        return current + char
    
    def remove_last(self, current):
        """Remove o último caractere"""
        if current and current != "0" and current != "Erro":
            return current[:-1] if len(current) > 1 else "0"
        return "0"
    
    def clear_all(self):
        """Limpa tudo"""
        self.current_operation = ""
        return "0"