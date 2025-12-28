class CalculadoraBonos:
    def __init__(self, factor_bono):
        self.factor_bono = factor_bono
    
    def calcular_bono_anual(self, salario):
        return salario * self.factor_bono
    
    @classmethod
    def modelo_10_porciento(cls, salario):
        calculadora = cls(factor_bono=0.1)
        return calculadora.calcular_bono_anual(salario)


# Uso
bono_calculado = CalculadoraBonos.modelo_10_porciento(salario=80000)
print(bono_calculado)  # Resultado: 8000.0
