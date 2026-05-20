class IMCModel:
    def calcular_imc(self, peso, altura):
        """Calcula o IMC"""
        if altura <= 0 or peso <= 0:
            return None
        return peso / (altura ** 2)
    
    def classificar_imc(self, imc):
        """Classifica o IMC"""
        if imc < 18.5:
            return "Abaixo do peso", "warning"
        elif imc < 25:
            return "Peso normal", "success"
        elif imc < 30:
            return "Sobrepeso", "warning"
        elif imc < 35:
            return "Obesidade grau I", "danger"
        elif imc < 40:
            return "Obesidade grau II", "danger"
        else:
            return "Obesidade grau III", "danger"