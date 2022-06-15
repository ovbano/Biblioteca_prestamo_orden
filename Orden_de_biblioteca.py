#Librería que define un calendario de módulo incorporado que maneja las operaciones relacionadas con el calendario.
from calendar import c 
#Importa el módulo de fecha y hora y muestre la fecha actual
import datetime
from holidays.constants import JAN, DEC
from holidays.holiday_base import HolidayBase

from Menus import menuPrincipal
from Catalogos import *



print("|                     Bienvenido a la Biblioteca                        |")

class Fiestas(HolidayBase):
    """
    Esta clase va a permitir identificar cuando un día sea feriado. En el 
    cual habra una restricción en el programa ya que es conocido que en los 
    feriados las bibliotecas no laboran normalmente: 
    https://bibliotecaviva.cl/cierre-por-feriados/
    ...
    Atributos (Hereda la clase HelidayBase )
    ----------
    prov: str
        código de provincia según ISO3166-2
    
    """    
    PROVINCES = ["EC-P"]  # TODO añadir más provincias

    def __init__(self, **kwargs):
        """
         Construye todos los atributos necesarios para el objeto HolidayEcuador.
        """         
        self.country = "ECU"
        self.prov = kwargs.pop("prov", "ON")
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        """
        Comprueba si una fecha es feriado o no
        
        Parametros
        ----------
        anio : str
            año de una fecha
        Retornar
        -------
        Rrtornar true si una fecha es uno de los días festivo declarados, de lo contrario, se muestra como fase.
        """                    
        # Dia de Año Nuevo 
        self[datetime.date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"
        
        # Navidad
        self[datetime.date(year, DEC, 25)] = "Navidad [Christmas]"


class libNuevo(catalogo):
    '''
    La clase catálogo correspondrá a la super clases que heredará sus atributos
    y métodos a una sub clase denominada libNuevo(catalogo): la cual contendrá
    los atributos y métodos caracteristicos para agrega un libro nuevo a la lista
    ya existente en la super clase catalogo. Esta clase se la declararía de la 
    siguiente manera:

    clase que permitirá registrar un nuevolibro ingresado por partedel usuario

    Parametros
    ----------
     
     Atributos
     ------------
     -nombre = del libro que el usuario ingresará por teclado
     -editorial = del libro que el usuario ingresará por teclado
     -fechas = correspondiente al prestamo de libros
     -autor = del los libros que se ingresen
     -datoLib = datos de los libros como su nombre - autor ...
     -a = contador

     Método
     ----------
     
     -agregarLib():  Para este método se van a realizan una serie de condiciones que validen 
      el ingreso de los géneros ya establecidos, pues que antes de registrar un libro primeramente
      deberá digitar el número de libros que desea registrar también el género al que pertenece... 

     -registroLib(): Muestra los libros registrados con el formato nombre - autor - editorial.

    '''

    #Atributo constructor de la sub clase
    def __init__(self,a ):
        #Para esta sub clase se tienen los siguientes atributos los cuales 
        #también son una lista a manera de arrays.
        super().__init__()
        self.nombre = []
        self.editorial = []
        self.fechas = []
        self.autor = []
        self.datoLib=[""]
        self.a=0 #Contador
    

    def agregarLib(self):

        print("Ha seleccionado la opcion para agregar libros nuevos a la biblioteca")
        print(
            "Los generos disponibles para agregar libros son: \n -Aventura \n -Terror \n -Drama \n -Ciencia Ficción \n -Comedia \n -Romance \n -Infantil")
        genero = input("Ingrese el genero del/los libro/s que desea agregar a la biblioteca: ")
        minusGen = genero.lower() #Función que permite transformar una cadena de caracte a minúscula
        #Validación del ingreso de datos.
        while not (
                minusGen == "aventura" or minusGen == "terror" or minusGen == "drama" or minusGen == "ciencia ficcion" or minusGen == "comedia" or minusGen == "romance" or minusGen == "infantil"):
            print("El genero que ingreso no se encuentra en la biblioteca \n Por favor ingrese un genero disponible")
            genero = input("")
            minusGen = genero.lower()

        cantidad = int(input("Cuantos libros nuevos desea agregar al genero de Aventura?: "))

        for contador in range(0,cantidad):
                print("Ingrese el nombre del libro", contador + 1)
                self.nombre.append(input())

                print("Ingrese el nombre del autor", contador + 1)
                self.autor.append(input())

                print("Ingrese el editorial", contador + 1)
                self.editorial.append(input())

        if minusGen == "aventura":
           
            ave.nomAventura.extend(self.nombre)
            ave.autorAventura.extend(self.autor)
            ave.editAventura.extend(self.editorial)
            ave.contador[0] = ave.contador[0] + cantidad

        elif minusGen == "terror":

            terr.nomTerror.extend(self.nombre)
            terr.autorTerror.extend(self.autor)
            terr.editTerror.extend(self.editorial)
            terr.contador[1] = terr.contador[1] + cantidad

        elif minusGen == "drama":

            dra.nomDrama.extend(self.nombre)
            dra.autorDrama.extend(self.autor)
            dra.editDrama.extend(self.editorial)
            dra.contador[2] = dra.contador[2] + cantidad

        elif minusGen == "ciencia ficcion":

            ciencia.nomCCFF.extend(self.nombre)
            ciencia.autorCCFF.extend(self.autor)
            ciencia.editCCFF.extend(self.editorial)
            ciencia.contador[3] = ciencia.contador[3] + cantidad

        elif minusGen == "comedia":

            com.nomComedia.extend(self.nombre)
            com.autorComedia.extend(self.autor)
            com.editComedia.extend(self.editorial)
            com.contador[4] = com.contador[4] + cantidad

        elif minusGen == "romance":

            roman.nomRomance.extend(self.nombre)
            roman.autorRomance.extend(self.autor)
            roman.editRomance.extend(self.editorial)
            roman.contador[5] = roman.contador[5] + cantidad

        elif minusGen == "infantil":

            infa.nomInfantil.extend(self.nombre)
            infa.autorInfantil.extend(self.autor)
            infa.editInfantil.extend(self.editorial)
            infa.contador[6] = infa.contador[6] + cantidad

        fecha = datetime.datetime.now()
        fechaa = datetime.datetime.strftime(fecha, '%d, %B %Y')
        self.fechas.append(fechaa)
        for x in range(len(self.nombre)):
            self.datoLib[self.a] += self.nombre[x] + ", "
        print("El/Los libro/s:", self.nombre, "\n Se agregaron correctamente al catalogo en el genero de", genero)
        print("En la fecha ", fechaa)
        for x in range(len(self.nombre)):
            self.nombre.pop()
            self.autor.pop()
            self.editorial.pop()

    def registroLib(self):

        print("Registro de libros ingresados a la biblioteca")
        print("_______________")
        for x in range(len(self.datoLib)):
            print("El/Los libro/s:", self.datoLib[x], "\n fueron ingresados al catalogo")
            print("En la fecha ", self.fechas[x])
            print("_______________")
    


class prestamo:
    """
    La siguiente clase fué creada para llevar el registro de los prestamos de libros
    dentro de la biblioteca, la clase consta de los atributos y metodos correspondientes
    para su correcto funcionamiento. Acontinuación se declaran la clase prestamo:

    Parámetros
    -----------
     Atributos
     ------------
     -nomCliente = nombre del cliente que desea prestar un libro.
     -apelliCliente = apellido del cliente que desea prestar un libro.
     -id = identificación del cliente que desea prestar un libro.
     -nomLibro = nombre del libro a prestar.
     -tiemPrestamo = tiempo que propone el cliente para prestar un libro.
     -fechaPress = fecha de entrega del libro.
     -dia = día de entrega del libro prestado.
     -b = contador.

     Métodos
     ---------
     prestarLib(): función en la cual el usuario llena los campos correspondiente para 
      el correcto registro del prestamo de un libro.

     registroprestamo(): funcion que muestra los datos del cliente y el registro pertinente
      junto con la fecha de entrega del libro prestado

    """
    #Atributos con el Costructor de la clase
    def __init__(self):
        self.nomCliente = []
        self.apelliCliente=[]
        self.id=[]
        self.nomLibro = []
        self.tiemPrestamo = [""]
        self.fechaPress =[]
        self.dia=0
        self.b=0
    #Métodos de la clase
    def prestarLib(self):
        #Compos que proporcionan información sobre los prestamosde libros correspondientemente
        #al género que valla a señalar el usuario.
        print("A solicitado prestar un libro a la biblioteca\nIngrese algunos datos y condiciones para realizar este proceso")
        self.nomCliente.append(input("Ingrese su nombre: "))
        self.apelliCliente.append(input("Ingrese su apellido: "))
        self.id.append(input("Ingrese su numero de identificacion/cedula: "))
        genero = input("Ingrese el genero del libro que desea prestar: ")
        minusGen = genero.lower()
        while not (minusGen == "aventura" or minusGen == "terror" or minusGen == "drama" or minusGen == "ciencia ficcion" or minusGen == "comedia" or minusGen == "romance" or minusGen == "infantil"):
            print("El genero que ingreso no se encuentra en la biblioteca \n Por favor ingrese un genero disponible")
            genero = input("")
            minusGen = genero.lower()

        if minusGen == "aventura":
            nom=input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(ave.nomAventura,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            self.nomLibro.append(nom)

        elif minusGen == "terror":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(terr.nomTerror,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            self.nomLibro.append(nom)

        elif minusGen == "drama":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(dra.nomDrama,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            self.nomLibro.append(nom)

        elif minusGen == "ciencia ficcion":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(ciencia.nomCCFF,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            self.nomLibro.append(nom)

        elif minusGen == "comedia":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(com.nomComedia,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            self.nomLibro.append(nom)

        elif minusGen == "romance":
            nom = input("Ingrese el nombre del libro que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(roman.nomRomance,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            self.nomLibro.append(nom)

        elif minusGen == "infantil":
            nom = input("Ingrese el nombre del libro de que requiere prestar\nRecuerde escribir el nombre del libro tal y como se muestra en el catalogo: ")
            while busquedaLib(infa.nomInfantil,nom) == False:
                nom = input("El libro que ingreso no se encuentra\nComprobar que este bien escrito o se encuentre en el catalogo\nIntente otra vez: ")
            self.nomLibro.append(nom)
        #Tiempo que el usuario valla aprestar los libros
        print("Puede solicitar el prestamo por un tiempo limitado de 3 meses\nIngrese en numeros los mes y dias, que dispodra del libro")
        mes=int(input("Meses: "))
        while mes<1 or mes>3:
            mes=int(input("El numero que ingreso esta fuera de rango, con respecto al tiempo de prestamo segun el mes\nIntente nuevamente: "))
        #Validación de presamos de libros
        if mes == 3:
            self.dia=0
        elif mes == 2:
            self.dia = int(input("Debido a que a ingresado para 2 meses el prestamo, podra ingresar como maximo 30 dias: "))
            while self.dia < 0 or self.dia > 30:
                self.dia = int(input("Ingreso mal los dias\nIntente nuevamente: "))
        elif mes == 1:
            self.dia = int(input("Puede ingresar como maximo 60 dias"))
            while self.dia < 0 or self.dia > 60:
                self.dia = int(input("Ingreso mal los dias\nIntente nuevamente: "))
        #Cálculos para determinar el dia exacto en el que se debe devlver los libros.
        self.tiemPrestamo[self.b]=str(mes)+" meses con "+str(self.dia)+" dias"
        fecha = datetime.datetime.now()
        fechaa = datetime.datetime.strftime(fecha, '%d, %B %Y')
        self.fechaPress.append(fechaa)
        print("Felicidades!, a realizado el proceso de prestamo con exito\nDisfrute del libro")
    #Enseñar los datos a usuario.
    def registroprestamo(self):
        print("Registro de Prestamo realizados")
        print("_______________")
        for x in range(len(self.nomCliente)):
            print("El/La Señor/a:", self.nomCliente[x], self.apelliCliente[x],"con ID:",self.id[x])
            print("Solicito prestar el libro: ", self.nomLibro[x],"con tiempo de",self.tiemPrestamo[x])
            print("En la fecha", self.fechaPress[x])
            print("_______________")

def mostrarCatalogo():
        print(
            "______________________________________________\n CATALOGO\n ______________________________________________")
        print("Formato de visualizacion: Nombre-Autor-Editorial")
        print(
            "______________________________________________\nLibros de Aventura\n")
        for x in range(ave.contador[0]):
            print(ave.nomAventura[x], "-", ave.autorAventura[x], "-", ave.editAventura[x])
        print("______________________________________________")

        print("Libros de Terror\n")
        for x in range(terr.contador[1]):
            print(terr.nomTerror[x], "-", terr.autorTerror[x], "-", terr.editTerror[x])
        print("______________________________________________")

        print("Libros de Drama\n")
        for x in range(dra.contador[2]):
            print(dra.nomDrama[x], "-", dra.autorDrama[x], "-", dra.editDrama[x])
        print("______________________________________________")

        print("Libros de Ciencia Ficción\n")
        for x in range(ciencia.contador[3]):
            print(ciencia.nomCCFF[x], "-", ciencia.autorCCFF[x], "-", ciencia.editCCFF[x])
        print("______________________________________________")

        print("Libros de Comedia\n")
        for x in range(com.contador[4]):
            print(com.nomComedia[x], "-", com.autorComedia[x], "-", com.editComedia[x])
        print("______________________________________________")

        print("Libros de Romance\n")
        for x in range(roman.contador[5]):
            print(roman.nomRomance[x], "-", roman.autorRomance[x], "-", roman.editRomance[x])
        print("______________________________________________")

        print("Libros Infantiles\n")
        for x in range(infa.contador[6]):
            print(infa.nomInfantil[x], "-", infa.autorInfantil[x], "-", infa.editInfantil[x])
        print("______________________________________________")

#Algoritmo de busque binaria
def busquedaLib(lista,valor):
    """
    Este algoritmo de busqueda se cumple siempre y cuando el usuario ingrese el mismo nombre
    que se declaró en la parte de arriba de la lista, de ser el caso contrario quedará atrapado 
    en un bucle hasta que vuelva a ingresar correctamente el nombre. Lo que retorna es una variable
    de tipo bool (verdadera o falsa),
    """
    primero=0
    ultimo=len(lista)-1
    encontrado=False

    while primero <= ultimo and not encontrado:
        mitad=(primero+ultimo)//2

        if lista[mitad]==valor:
            encontrado=True
        else:
            if valor<lista[mitad]:
                ultimo=mitad-1
            else:
                primero=mitad+1

    return encontrado

#---------------------mein principal-----------------------
#Instanciar objetos de clases y subclases.
nuevo = libNuevo(catalogo)
pres=prestamo()
#Llamar a los métodos de cada clase correspondiente mente.
fecha = datetime.datetime.now()
fechaa = datetime.datetime.strftime(fecha, '%d, %B %Y')

if fechaa != "1, January 2022" and fechaa != "25, December 2022":
    cata.asignacion()
    menuPrincipal()

elif fechaa == "1, January 2022":
    "Debido al primer Dia de Año Nuevo los servicios de la biblioteca estan suspendidos "
elif fechaa == "25, December 2022":
    "Debido al feriado de Navidad los servicios de la biblioteca estan suspendidos "