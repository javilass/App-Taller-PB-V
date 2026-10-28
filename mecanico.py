from persona import Persona
from bicicleta import Bicicleta

class Mecanico(Persona):
    
    def __init__(self, nombre, rut, telefono, especialidad, sueldo):
        super().__init__(nombre, rut, telefono)
        self.especialidad = especialidad
        self.sueldo = sueldo    
    
    def mostrar_informacion(self):
        super().mostrar_informacion() #sacamos el "return" que nos tira por defecto, porque nuestra UML dice que debe ser void
        print(f"Especialidad: {self.especialidad}")
        print(f"Sueldo: {self.sueldo}")
    
    def reparar_bicicleta(self,bicicleta):
        return f"El mecánico {self.nombre} está reparando la bicicleta {bicicleta.numero_serie}"
        