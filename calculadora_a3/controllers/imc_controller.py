from models.imc_model import IMCModel

class IMCController:
    def __init__(self):
        self.model = IMCModel()
    
    def calcular(self, peso, altura):
        """Calcula o IMC e retorna classificação"""
        try:
            peso_f = float(peso)
            altura_f = float(altura)
            
            if altura_f <= 0 or peso_f <= 0:
                return False, "Valores inválidos", None
            
            imc = self.model.calcular_imc(peso_f, altura_f)
            classificacao, cor_tipo = self.model.classificar_imc(imc)
            
            return True, f"IMC: {imc:.2f} - {classificacao}", cor_tipo
        except ValueError:
            return False, "Erro: Valores inválidos", None