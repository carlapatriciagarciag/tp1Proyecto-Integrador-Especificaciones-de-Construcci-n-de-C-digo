from usuario import Cliente, Admin
from productos import Hardware,Software
from carrito import Carrito, LineaDeFactura
from sistemas import Sistema

admin = Admin(1,"admin@gmail.com", "123",16049)
cliente = Cliente(1,"cli@gmail.com", "1234", "calle 1234")

p1 = Hardware(1,"pc", 100, 10, 12, 2.5)
p2 = Software(2, "office", 200, 20, 500, "abc123")

carrito = Carrito()
carrito.agregar_producto(p1, 3)
carrito.agregar_producto(p2, 5)
print("total: ", carrito.calcular_total())

factura = carrito.consolidar()
print("Stock PC:", p1.stock_disponible)
print("Stock Office:", p2.stock_disponible)
admin.reponer_stock(p1,5)