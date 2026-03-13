class personas:
    def __init__(self,idpersona,nombre,mail):
        self.idpersona=idpersona
        self.nombre=nombre
        self.mail=mail   
    def login(self):
        return f"{self.nombre} inicio sesión"
    def actualizarperfil(self,nuevo, mailnuevo):
        self.nombre=nuevo
        self.mail=mailnuevo
        print("perfil actualizado")
        
class cliente(personas):
    def __init__(self, idpersona,nombre, email):
        personas.__init__(self, idpersona, nombre, email)
        self.puntosfidelidad=0
        self.historial=[]
    def realizarPedido(self, pedido):
        self.historial.append(pedido)
        print("Pedido hecho")
    def verhistorial(self):
        for a in self.historial:
            print(a.idpedido)
    def canjearpuntos(self):
        if self.puntosfidelidad>=90:
            print("Secanjearon los puntos")
            self.puntosfidelidad-=90
        else:
            print("necesitas más puntos")

class empleado(personas):
    def __init__(self, idpersona, mail, nombre, idempleado, rol):
        personas.__init__(self, idpersona, nombre, mail)
        self.idempleado=idempleado
        self.rol=rol
    def actualizarestado(self, pedido, nuevoestado):
        pedido.estado=nuevoestado
        print("Estado actualizado")
    def cambiarestado(self, pedido, nuevoestado):
        pedido.estado=nuevoestado

class productobase:
    def __init__(self, idProducto, nombre, preciobase):
        self.idProducto=idProducto
        self.nombre=nombre
        self.preciobase=preciobase

class Bebida(productobase):
    def __init__(self, idProducto,nombre, preciobase, tamaño, temperatura):
        productobase.__init__(self, idProducto, nombre, preciobase)
        self.tamaño=tamaño
        self.temperatura=temperatura
        self.modificar=[]
    def agregarExtra(self, extra):
        self.modificar.append(extra)
    def calcularprecioBase(self):
        return self.preciobase + len(self.modificar)*5

class Postre(productobase):
    def __init__(self, idProducto, nombre, preciobase, esVegano,sinGluten):
        productobase.__init__(self, idProducto, nombre, preciobase)
        self.esVegano=esVegano
        self.sinGluten=sinGluten

class pedido:
    def __init__(self, idpedido):
        self.idpedido=idpedido
        self.productos=[]
        self.estado="pendiente"
        self.total=0
    def calcularTotal(self):
        total=0
        for b in self.productos:
            total+=b.preciobase
        self.total=total
        return total
    def validarelstock(self):
        print("el stock ha sido revisado")

class Inventario:
    def __init__(self):
        self.ingredientes={}
    def reducirStock(self, ingrediente, cantidad):
        if ingrediente in self.ingredientes:
            self.ingredientes[ingrediente]-=cantidad
    def notificarfaltante(self, ingrediente):
        if self.ingredientes.get(ingrediente,0)<=0:
            print(f"falta {ingrediente}")