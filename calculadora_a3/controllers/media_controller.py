from models.media_model import MediaModel

class MediaController:
    def __init__(self):
        self.model = MediaModel()
    
    def calcular_media(self, valores):
        """Calcula a média dos valores"""
        valores_validos = []
        
        for valor in valores:
            val = self.model.validar_valor(valor)
            if val is not None:
                valores_validos.append(val)
        
        if not valores_validos:
            return False, "Nenhum valor válido encontrado"
        
        media = self.model.calcular_media(valores_validos)
        return True, f"Média: {media:.2f}"