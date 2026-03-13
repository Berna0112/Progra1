from modelstwo import *
cliente1=cliente(1,"Jimmy","Jimmyneutron@gmail.com")
cliente2=cliente(2,"Berni777","bernipro@hotmail.com")

empleado1=empleado(1,"pedro@mail.com","Pedro","EMP01","gerente")
bebida1=Bebida(1,"Café",40,"Grande","Caliente")
bebida2=Bebida(2,"Té",35,"Mediano","Caliente")

postre1=Postre(3,"Cheesecake",60,False,False)
postre2=Postre(4,"Brownie",50,False,True)
pedido1=pedido(101)
pedido1.productos.append(bebida1)
pedido1.productos.append(postre1)

print("Productos del pedido:")
for aña in pedido1.productos:
    print(aña.nombre)
print("total:", pedido1.calcularTotal())

cliente1.realizarPedido(pedido1)
print("hisrorial del cliente:")
cliente1.verhistorial()

empleado1.actualizarestado(pedido1,"entregado")
print("Estado del pedido", pedido1.estado)

inventario=Inventario()
inventario.ingredientes["cafe"]=10
inventario.ingredientes["leche"]=3
inventario.ingredientes["azucar"]=1
inventario.reducirStock("cafe",2)

inventario.notificarfaltante("cafe")
inventario.notificarfaltante("leche")
inventario.notificarfaltante("azucar")