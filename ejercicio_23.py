# ¡CORRECCIÓN CLAVE! El valor por defecto se establece aquí (bono=0).
def calcular_salario_final(salario_base, bono=0): 
    return salario_base + bono

# Ahora podemos omitir el argumento 'bono' en la primera llamada:
salario_sin_bono = calcular_salario_final(5000)      # Python usa bono=0
salario_con_bono = calcular_salario_final(5000, 1000) # Python usa bono=1000