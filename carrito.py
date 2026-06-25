from productos import Producto

class LineaDeFactura:
    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad
        self.__monto = producto.mostrar_precio() * cantidad

    def __str__(self):
        return f"{self.__producto} - Cantidad: {self.get_cantidad()} - Monto: {self.get_monto()}"

    def get_cantidad(self):
        return self.__cantidad

    def get_monto(self):
        return self.__monto

    def get_producto(self):
        return self.__producto


class Carrito:
    def __init__(self):
        self.__productos = []  # lista de tuplas (producto, cantidad)

    def agregar_producto(self, producto_externo, cantidad):
        if len(self.__productos) >= 50:
            raise ValueError("El carrito alcanzó su límite de 50 productos")
        if cantidad > producto_externo.stock_disponible:
            raise ValueError("No hay suficiente stock")
        self.__productos.append((producto_externo, cantidad))

    def quitar_producto(self, producto_externo):
        self.__productos = [
            (p, c)
            for (p, c) in self.__productos
            if p != producto_externo
        ]

    def calcular_total(self):
        return sum(p.mostrar_precio() * c for (p, c) in self.__productos)

    def get_productos(self):
        return self.__productos

    def consolidar(self):
        lineas = []
        for producto, cantidad in self.__productos:  # sin .items()
            lineas.append(LineaDeFactura(producto, cantidad))
            producto._reducir_stock(cantidad)
        return lineas