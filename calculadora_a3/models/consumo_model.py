class ConsumoModel:
    def calcular_consumo(self, potencia, horas, dias, preco_kwh):
        """
        Calcula o consumo de energia
        Retorna: (consumo_kwh, custo_total, custo_diario)
        """
        consumo_kwh = (potencia * horas * dias) / 1000
        custo_total = consumo_kwh * preco_kwh
        custo_diario = custo_total / dias if dias > 0 else 0
        
        return consumo_kwh, custo_total, custo_diario