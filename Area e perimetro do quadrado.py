lado=float(input())
def calcular_area(lado):
    return lado**2
def calcular_perimetro(lado):
    return 4*lado
area=calcular_area(lado)
perimetro=calcular_perimetro(lado)
area_formatada=f"{area:.4f}"
perimetro_formatada=f"{perimetro:.4f}"
print(f"{area_formatada:>10}")
print(f"{perimetro_formatada:>10}")
