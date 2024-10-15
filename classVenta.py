class Venta:
    __id_venta = None
    __fecha = None
    __cliente = None
    __productos = None  # Diccionario de productos vendidos
    __total = None

    def __init__(self):
        # Inicializamos un diccionario vacío para los productos
        self.__productos = {}
        self.__total = 0

    # Getters para acceder a los atributos privados
    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    # Setters para modificar los atributos privados
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    # Método para agregar productos con cantidad y precio unitario
    def agregar_producto(self, producto, cantidad, precio_unitario):
        if producto not in self.__productos and len(self.__productos) < 3:
            self.__productos[producto] = {'cantidad': cantidad, 'precio_unitario': precio_unitario}
        elif producto in self.__productos:
            # Si el producto ya está, sumamos la cantidad
            self.__productos[producto]['cantidad'] += cantidad
        else:
            print("Solo se permiten 3 productos como máximo.")
        self.__calcular_total()

    # Método para calcular el total
    def __calcular_total(self):
        self.__total = 0
        for producto, detalles in self.__productos.items():
            self.__total += detalles['cantidad'] * detalles['precio_unitario']

    # Método para mostrar los detalles de la venta
    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos:")
        for producto, detalles in self.__productos.items():
            print(f"  {producto} - Cantidad: {detalles['cantidad']}, Precio Unitario: ${detalles['precio_unitario']:.2f}")
        print(f"Total: ${self.__total:.2f}")
