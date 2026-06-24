class Usuario(Sistema): # Hereda de sistema y se vuelve padre de cliente y usuario

    def __init__(self, email, contraseña):
        self.__email = email
        self.__contraseña = contraseña


class Cliente(Usuario):

    def __init__(self, email, contraseña, direccion_envio):
        super().__init__(email, contraseña) # atributos de la clase padre

        self.__direccion_envio = direccion_envio

class Admin(Usuario):

    def __init__(self, email, contraseña, numero_legajo):

        super().__init__(email, contraseña) # atributos de la clase padre

        self.__numero_legajo = numero_legajo

    def agregar_productos(numero_legajo):



    def reponer_stock(numero_legajo):



    def reducir_stock(numero_legajo):