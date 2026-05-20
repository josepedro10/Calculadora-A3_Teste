from models.calculator_model import CalculatorModel

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
    
    def process_button(self, value, current_display):
        """Processa o clique de um botão da calculadora"""
        if value == '=':
            return self.model.evaluate_expression(current_display)
        elif value == 'C':
            return self.model.remove_last(current_display)
        elif value == 'AC':
            return self.model.clear_all()
        elif value == '%':
            return self.model.calculate_percentage(current_display)
        elif value == '√':
            return self.model.calculate_square_root(current_display)
        else:
            return self.model.add_character(current_display, value)