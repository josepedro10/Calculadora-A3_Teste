from models.consumo_model import ConsumoModel

class ConsumoController:
    def __init__(self):
        self.model = ConsumoModel()
    
    def calcular(self, potencia, horas, dias, preco):
        """Calcula o consumo de energia"""
        try:
            potencia_f = float(potencia)
            horas_f = float(horas)
            dias_f = float(dias)
            preco_f = float(preco)
            
            resultado = self.model.calcular_consumo(potencia_f, horas_f, dias_f, preco_f)
            return True, resultado
        except ValueError:
            return False, "Erro: Valores inválidos"