class Bicicleta:
    
    def __init__(self, marca:str, tipo:str, numero_serie:str):
        self.marca = marca
        self.tipo = tipo
        numero_serie =numero_serie
        
    def mostrar_informacion(self): #es un void, entonces solo regresa un print, no un return
        print(f"Bicicleta {self.marca} ({self.tipo}) - N° serie: {self.numero_serie}")
 
    def obtener_marca(self) -> str: #este es un string, entonces, si usamos el tipo de dato tambien usamos return
        return self.marca