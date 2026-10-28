from persona import Persona
from bicicleta import Bicicleta

class Cliente(Persona): #indicamos la clase padre de la cual estamos heredando
    
    def __init__(self, nombre, rut, telefono, direccion):
        super().__init__(nombre, rut, telefono) #este super no lo tocamos, porque trae los atributos del padre!! -> HERENCIA
        self.direccion = direccion
        self.bicicletas = []
        
    def agregar_bicicletas(self, bicicleta: Bicicleta):
        self.bicicletas.append(bicicleta)
        print(f"Bicicleta añadida correctamente")
        
    def mostrar_informacion(self):
        super().mostrar_informacion() #el hijo toma el mismo método, pero lo va a modificar con algo propio -> POLIMORFISMO
        print(f"Dirección: {self.direccion}")
        
    def contar_bicicletas(self) -> int:
        return len(self.bicicletas) #usamos el len(self.bicicletas) porque contaremos el numero de items en la lista y lo devolveremos