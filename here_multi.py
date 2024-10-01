class persona:
    def __init__(self,nombre,edad) :
        self.nombre = nombre
        self.edad = edad



class empleado(persona) :
    def __init__(self, nombre, edad,salario,area):
        super().__init__(nombre, edad)
        self.salario = salario
        self.area = area

class vendedor(empleado,persona):
    def __init__(self, nombre, edad, salario, area,venta,sucursal):
        super().__init__(nombre, edad, salario, area)
        self.venta = venta
        self.sucursal = sucursal

    def comision(self):
        return self.venta * 0.11

    def descuento(self):
        return self.venta - self.venta *0.1
       
class cliente(persona) :
    def __init__(self,nombre,edad,compra,bono):
        super().__init__(nombre, edad)
        self.compra = compra
        self.bono = bono


vendedor1=vendedor(" frank",18,1000,"comercial",200,"galapa")
comision=vendedor1.comision()
print(f"la comision es {comision}")

descuento = vendedor1.descuento()
print(f"la venta con el descuento es {descuento}")
