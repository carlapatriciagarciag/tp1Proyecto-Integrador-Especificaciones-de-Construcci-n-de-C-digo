class Sistema:
    def __init__(self, id_sistema):
        # privado porque en el diagrama tiene el signo -
        self.__id = id_sistema

    def validar(self, id):
        # público (+), valida las credenciales de un usuario
        print(f"Validando credenciales del usuario {id}...")
        return True

    def _elegibilidad(self, id):
        # protegido (#)
        print(f"Chequeando elegibilidad de {id}...")
        return True

    def _procesar_checkout(self, id):
        # protegido (#) también, acá se dispara todo el proceso de cobro
        print(f"Procesando checkout del usuario {id}...")
        return True
    
# -------------------------------------------------------------------------------------------------------------

class Usuario(Sistema):
    def __init__(self,id_sistema):
       super().__init__(id_sistema)



        
          

# -------------------------------------------------------------------------------------------------------------

class LineaDeFactura:
    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad
        self.__monto = producto.mostrar_precio() * cantidad  # precio x cantidad, lo calculo una sola vez acá

    def get_cantidad(self):
        return self.__cantidad

    def get_monto(self):
        return self.__monto

    def get_producto(self):
        return self.__producto


class Carrito:
    def __init__(self):
        # acá solo van a vivir referencias a productos, no copias
        self.__productos = []

    def agregar_producto(self, producto_externo, cantidad):
        # el producto ya existe afuera, el carrito solo lo referencia
        if len(self.__productos) >= 50:
            raise ValueError("El carrito alcanzó su límite de 50 productos")
        self.__productos.append((producto_externo, cantidad))

    def quitar_producto(self, producto_externo):
        # filtro la lista y me quedo con todo menos el producto que me pasaron
        self.__productos = [
            (p, c) for (p, c) in self.__productos if p != producto_externo
        ]

    def calcular_total(self):
        # recorro todo lo que hay en el carrito y voy sumando precio * cantidad
        return sum(p.mostrar_precio() * c for (p, c) in self.__productos)

    def get_productos(self):
        # esto lo va a usar Factura para armar sus LineaDeFactura al consolidar
        return self.__productos

    def consolidar(self):
        factura = LineaDeFactura(self.__productos)
        for producto, cantidad in self.__productos:
            producto.reducir_stock(cantidad)
        self.__productos = []
        return factura