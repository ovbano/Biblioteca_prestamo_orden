

# Menú principal del programa
def menuPrincipal():

    import Orden_de_biblioteca
    opcion = 0

    while opcion != 5:
        print("________________")
        print("Menu Principal")
        print("1- Visualizar Catalogo")
        print("2- Agregar libros")
        print("3- Visualizar registros")
        print("4- Solicitar prestamo de libros")
        print("5- Salir")
        print("________________")
        opcion = int(input("Ingrese su opcion:"))
        if opcion == 1:
            Orden_de_biblioteca.mostrarCatalogo()
        elif opcion == 2:
            Orden_de_biblioteca.nuevo.agregarLib()
        elif opcion == 3:
            subMenu()
        elif opcion == 4:
            Orden_de_biblioteca.pres.prestarLib()
            Orden_de_biblioteca.pres.b = Orden_de_biblioteca.pres.b + 1
        elif opcion == 5:
            "Salir"


def subMenu():

    import Orden_de_biblioteca 
    
    op_regis = 0

    while op_regis != 3:
        print("________________")
        print("Registros")
        print("1- Registro de Libros ingresados")
        print("2- Registro de prestamos")
        print("3- Salir")
        print("________________")
        op_regis = int(input("Ingrese su opcion:"))
        if op_regis == 1:
            Orden_de_biblioteca.nuevo.registroLib()
            Orden_de_biblioteca.nuevo.a = Orden_de_biblioteca.nuevo.a + 1
        elif op_regis == 2:
            Orden_de_biblioteca.pres.registroprestamo()
        elif op_regis == 3:
            print("Salir")

