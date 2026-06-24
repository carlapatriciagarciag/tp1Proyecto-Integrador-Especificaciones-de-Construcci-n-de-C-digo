class Producto:

    def __init__(self, id, nombre, precio_base, stock_disponible):
        self.__id = id #privado
        self.nombre = nombre #publico
        self.precio_base = precio_base
        self._stock_disponible = stock_disponible #protegido

    @property
    def id(self): #permite leer id
        return self.__id
    @property
    def stock_disponible(self): #permite leer stock
        return self._stock_disponible
    
    def reponer_stock(self, cantidad):
        self._stock_disponible += cantidad
    
    def mostrar_precio(self):
        return self.precio_base
    def _reducir_stock(self, cantidad): #Carrito le debe mandar la cantidad que estan comprando de tal producto
        self._stock_disponible -= cantidad
    
    

class Software(Producto):
    def __init__(self, id, nombre, precio_base, stock_disponible, tamaño, clave_licencia):
        super().__init__(id, nombre, precio_base, stock_disponible)
        self.tamaño = tamaño
        self._clave_licencia = clave_licencia
    
    @property
    def enviar_licencia(self):
        print("La licencia de este software es: ", self._clave_licencia)

class Hardware(Producto):
    def __init__(self, id, nombre, precio_base, stock_disponible, garantia, peso):
        super().__init__(id, nombre, precio_base, stock_disponible)
        self._garantia = garantia
        self.peso = peso