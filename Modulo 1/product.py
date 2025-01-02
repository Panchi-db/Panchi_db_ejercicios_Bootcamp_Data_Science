class Product:
    title= "Definicion producto"
    iva=0.21
    
    #Método constructor
    def __init__(self,title, price): #atributos de instancia
        self.title = title
        self.price = price
        print ("Producto creado correctamente")
    
    def __str__(self):
        return f"Producto: Modelo= {self.title},Precio= {self.price}"
    
    def calcular_iva(self):
        return round(self.price * self.iva,2) #round: redondea( dos valores: lo que se quiere redondear , el num de decimales)
        
    
        """Calcula el iva, lo más s eguro un float: Iva calculado.
        """
        
        
ordenador_asus = Product ("Ordenador Asus", 399)
print(ordenador_asus.title)
print(ordenador_asus.price)
print(ordenador_asus.calcular_iva())