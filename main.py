from classVenta import Venta
#Instanciamos la variable
venta = Venta()

venta.set_id_venta(1)
venta.set_fecha("15/10/2024")
venta.set_cliente("Reyna")
#venta.set_productos(["Producto1" , "Producto2" , "Producto3"]) si es lista
#venta.set_total(150.75)
venta.agregar_producto('Producto A', 3, 15.0)  # 2 unidades de Producto A, precio unitario 15.0
venta.agregar_producto('Producto B', 1, 25.0)  # 1 unidad de Producto B, precio unitario 25.0
venta.agregar_producto('Producto C', 3, 35.0)  # 3 unidades de Producto C, precio unitario 35.0

venta.mostrar_detalle()


