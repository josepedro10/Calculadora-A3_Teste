# -*- coding: utf-8 -*-
"""
Módulo de Cálculos Matemáticos e Utilitários.
"""

def calcular_consumo_energia(potencia_w: float, tempo_h: float, dias: int) -> float:
    try:
        if potencia_w < 0 or tempo_h < 0 or dias < 0:
            raise ValueError("Os valores inseridos não podem ser negativos.")
        if tempo_h > 24:
            raise ValueError("O tempo de uso diário não pode exceder 24 horas.")
        if dias > 31:
            raise ValueError("A quantidade de dias no mês não pode exceder 31.")
            
        consumo_kwh = (potencia_w * tempo_h * dias) / 1000.0
        return round(consumo_kwh, 2)
    except Exception as e:
        raise ValueError(f"Erro no cálculo de energia: {str(e)}")

def calcular_media_tres_valores(v1: float, v2: float, v3: float) -> float:
    try:
        media = (v1 + v2 + v3) / 3.0
        return round(media, 2)
    except Exception as e:
        raise ValueError(f"Erro no cálculo de média: {str(e)}")

def calcular_imc_status(peso_kg: float, altura_m: float) -> tuple[float, str]:
    try:
        if peso_kg <= 0 or altura_m <= 0:
            raise ValueError("Peso e altura devem ser maiores que zero.")
        if altura_m > 3.0:
            altura_m = altura_m / 100.0
            
        imc = peso_kg / (altura_m ** 2)
        imc = round(imc, 2)
        
        if imc < 18.5:
            status = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            status = "Peso Ideal"
        elif 25.0 <= imc < 29.9:
            status = "Levemente acima do peso"
        elif 30.0 <= imc < 34.9:
            status = "Obesidade Grau I"
        elif 35.0 <= imc < 39.9:
            status = "Obesidade II (Severa)"
        else:
            status = "Obesidade III (Mórbida)"
            
        return imc, status
    except Exception as e:
        raise ValueError(f"Erro no cálculo de IMC: {str(e)}")