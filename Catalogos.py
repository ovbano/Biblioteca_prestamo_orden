#Creación de super clase
class catalogo:
    '''
     A continuación se mostrará un código que permitirá organizar los libros nuevos 
     que se ingresen en una biblioteca mediante la programacion orientada a objetos.
     Además de llevar un control en el prestamo de libros tomando en cuenta el tiempo
     en que se va a realizar el préstamos. Para realizar eso se deberá importar la 
     siguiente librería (calendar, que importa a c y a datetime), la cual permitira 
     utilizar el formato real de la hora actual. Finalmente el código será realizado 
     por medio de lista (arrays) que contendran la información correspondiente a cada
     genero de libro. A continuación se evidencian las clases y los métodos correspondientes.

     Clase que mostrará la lista de de los generos de libros, retornando 
     en formato nombre - autor - editorial.

        Parámetros
        --------
         Atributos
         --------
         -contador = de las listas de cada tipo de género, devuelve el número
         de espacios que contiene cada lista.

         Métodos
         --------
         -Asignacion():función que contiene la asignación de los método.
         
    '''

    #Atributo constructor del programa 
    def __init__(self) -> None:
        #Contador que permitirá concatenar nuevos datos con los datos ya existentes.
        self.contador = [0, 0, 0, 0, 0, 0, 0]

    #Metodos del la super clase 
    def asignacion():
        #Asignando funciones, para poder utilizar varibles
        ave.asigAven()
        terr.asigTerr()
        dra.asigDrama()
        infa.asigInfa()
        ciencia.asigCCFF()
        roman.asigRoman()
        com.asigcome()

class aventura(catalogo):
    '''
     Clase aventura que hereda atributos de la clase mayor catalogo .
     
     Métodos
     ------------
      -aingAven (): función en forma de lista que permite almacenar libros del genero aventura con nombre autor y editorial
    '''
    def asigAven(self):
        self.nomAventura = ["La isla del tesoro", "Robinson Crusoe", "Moby-Dick", "Viaje al centro de la Tierra",
                            "El corsario negro"]
        self.autorAventura = ["Robert Louis Stevenson", "Daniel Defoe", "Herman Melville", "Julio Verne",
                              "Emilio Salgari"]
        self.editAventura = ["Fontana", "W.Taylor", "Richard Bentley", "Hetzel", "Verbum"]
        self.contador[0] = len(self.nomAventura)

class terror(catalogo):

    '''
     Clase terror que hereda atributos de la clase mayor catalogo .
     
     Métodos
     ------------
      -asigTerr (): función en forma de lista que permite almacenar libros del genero aventura con nombre autor y editorial
    '''
    def asigTerr(self):
        self.nomTerror = ["It", "Drácula", "El resplandor", "Apartamento 16", "Dejame entrar"]
        self.autorTerror = ["Stephen King", "Bram Stoker", "Stephen King", "Adam L. G. Nevill", "John Ajvide Lindqvist"]
        self.editTerror = ["debolsillo", "Porrúa", "Doubleday", "Planeta Editorial", "Espasa "]
        self.contador[1] = len(self.nomTerror)

class drama(catalogo):
    '''
     Clase drama que hereda atributos de la clase mayor catalogo .
     
     Métodos
     ------------
      -asigDrama (): función en forma de lista que permite almacenar libros del genero aventura con nombre autor y editorial
    '''
    def asigDrama(self):
        self.nomDrama = ["Las dos esfinges", "La sombra de tu memoria", "Sueños de papel", "Khalil",
                         "El perro del hortelano"]
        self.autorDrama = ["L. Sancho", "Noelia Amarillo", "María Amorós", "Susana López Pérez", "Lope de Vega"]
        self.editDrama = ["Casa del Libro", "Noelia Amarillo", "Casa del Libro", "Alianza Editorial", "CATEDRA"]
        self.contador[2] = len(self.nomDrama)

class CCFF(catalogo):
    '''
     Clase CCFF que hereda atributos de la clase mayor catalogo .
     
     Métodos
     ------------
      -asigCCFF (): función en forma de lista que permite almacenar libros del genero aventura con nombre autor y editorial
    '''
    def asigCCFF(self):
        self.nomCCFF = ["Dune", "Fahrenheit 451", "El problema de los tres cuerpos", "El juego de Ender",
                        "Un mundo feliz"]
        self.autorCCFF = ["Frank Herbert", "Ray Bradbury", "Liu Cixin", "Orson Scott Card", "Aldous Huxley"]
        self.editCCFF = ["Chilton Books", "Minotauro", "NOVA", "Tor Books", "DEBOS"]
        self.contador[3] = len(self.nomCCFF)

class comedia(catalogo):
    '''
     Clase comedia que hereda atributos de la clase mayor catalogo .
     
     Métodos
     ------------
      -asigcome (): función en forma de lista que permite almacenar libros del genero aventura con nombre autor y editorial
    '''
    def asigcome(self):
        self.nomComedia = ["La conjura de los necios", "Ha vuelto", "El proyecto esposa", "Maldito karma",
                           "Cuentos sin plumas"]
        self.autorComedia = ["John Kennedy", "Timur Vermes", "Graeme Simsion", "David Safier", "Woody Allen"]
        self.editComedia = ["Louisiana State University Press", "Casa del Libro", "Salamandra", "Rowohlt Verlag GmbH",
                            "Tusquets"]
        self.contador[4] = len(self.nomComedia)

class romance(catalogo):
    '''
     Clase romance que hereda atributos de la clase mayor catalogo .
     
     Métodos
     ------------
      -asigRoman (): función en forma de lista que permite almacenar libros del genero aventura con nombre autor y editorial
    '''
    def asigRoman(self):
        self.nomRomance = ["Cumbres borrascosas", "Jane Eyre", "Un cuento perfecto", "Bajo la misma estrella",
                           "Eleanor & Park"]
        self.autorRomance = ["Emily Brontë", "Charlotte Brontë", "Elísabet Benavent", "John Green", "Rainbow Rowell"]
        self.editRomance = ["Alma", "Smith, Elder & Company", "SUMA", "Dutton Books", "St. Martin's Press"]
        self.contador[5] = len(self.nomRomance)

class infantil(catalogo):
    '''
     Clase infantil que hereda atributos de la clase mayor catalogo .
     
     Métodos
     ------------
      -asigInfa (): función en forma de lista que permite almacenar libros del genero aventura con nombre autor y editorial
    '''
    def asigInfa(self):
        self.nomInfantil = ["El principito", "El monstruo de colores", "El pollo Pepe", "A qué sabe la luna?",
                            "La historia interminable"]
        self.autorInfantil = ["Antoine de Saint-Exupéry", "Anna Llenas", "Nick Denchfield", "Michael Grejniec",
                              "Michael Ende"]
        self.editInfantil = ["Reynal & Hitchcock", "Flamboyant", "EDICIONES SM", "Kalandraka", "Thienemanns Verlag"]
        self.contador[6] = len(self.nomInfantil)



cata=catalogo
ave=aventura()
terr=terror()
dra=drama()
ciencia=CCFF()
com=comedia()
roman=romance()
infa=infantil()
