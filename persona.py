class Persona: #nuestro molde para las clases hijos (mecanico y cliente)
    
    def __init__(self, nombre:str,rut:str,telefono:str): #nuestro constructor es la estructura
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}") #usamos f"string" para concatenar string con una variable
        print(f"RUT: {self.rut}")
        print(f"Teléfono: {self.telefono}")
        
    def obtener_nombre(self) -> str: #le estoy indicando que debe devolver un dato tipo string
        return self.nombre
    