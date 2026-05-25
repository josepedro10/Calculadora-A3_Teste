class MediaModel:
    def calcular_media(self, valores):
        """Calcula a média de uma lista de valores"""
        if not valores:
            return None
        return sum(valores) / len(valores)
    
    def validar_valor(self, valor):
        """Valida se o valor é um número válido"""
        try:
            return float(valor)
        except ValueError:
            return None