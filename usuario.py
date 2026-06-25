from sistemas import Sistema
class Usuario(Sistema): # Hereda de sistema y se vuelve padre de cliente y usuario
    def __init__(self, id_sistema, email, contraseña):
        super().__init__(id_sistema)
        self.__email = email
        self.__contraseña = contraseña
    def __str__(self):
        return self.__email
    


class Cliente(Usuario):

    def __init__(self, id_sistema,email, contraseña, direccion_envio):
        super().__init__(id_sistema,email, contraseña) # atributos de la clase padre
        self.__direccion_envio = direccion_envio

class Admin(Usuario):

    def __init__(self,id_sistema, email, contraseña, numero_legajo):

        super().__init__(id_sistema, email, contraseña) # atributos de la clase padre

        self.__numero_legajo = numero_legajo

    def agregar_productos(numero_legajo, producto, cantidad):
        print(f"admin: {numero_legajo} esta agregando productos")
        producto.agregar_producto(cantidad)



    def reponer_stock(numero_legajo,producto, cantidad):
        print(f"admin: {numero_legajo} esta reponiendo el stock")
        producto.reponer_stock(cantidad)

        
   