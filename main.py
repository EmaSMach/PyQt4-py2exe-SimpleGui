# --*-- coding: utf-8 --*--

from tkinter import*
from radio_opciones import MyLabelFrameRadio, MyLabelFrameRadioQue
from archivos import MyLabelFrameArchivos, Acciones
from opciones_setup import MyLabelFrame
from escritorio_consola import MyLabelFrameEsCon
import funcionesEjecutables as ej
import os

class MyFrame(Frame):
    """Contenedor principal y funciones."""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH, pady=12, padx=12)
        self.master.title("Asistente para la generacion de Ejecutables y código Python PyQt")
        self.makeWidgets()

    def makeWidgets(self):
        """Instancia los widgets de los módulos importados."""
        self.radios1 = MyLabelFrameRadio(self)                      # Radiobutton de Version de Pyhton.
        self.radios2 = MyLabelFrameRadioQue(self)                   # Radiobutons de que hacer, ejecutable o código.
        self.radios1.grid(row=0, column=0, sticky=EW)               #
        self.radios2.grid(row=1, column=0, sticky=EW)               #
        self.radios2.radiotipo1.config(command=self.radio2set)    # Cambia una variable al hacer click.
        self.radios2.radiotipo2.config(command=self.radio2set)    #

        self.opciones1 = MyLabelFrame(self)                          # Es el contenedor de las opciones de setup.
        self.opciones1.grid(row=0, column=1, rowspan=2, sticky=NSEW)

        self.makeOpcionesWgets()

        self.tipoEsCon1 = MyLabelFrameEsCon(self)                   # Radiobuttons que indica tipo: consola o escritorio.
        self.tipoEsCon1.grid(row=2, column=0, columnspan=2, sticky=EW)
        self.tipoEsCon1.radioEsCon1.config(command=self.radio3set)
        self.tipoEsCon1.radioEsCon2.config(command=self.radio3set)

        self.aceptarono = Acciones(self)                            # Contenedor de los botones Acetar y Salir.
        self.aceptarono.grid(row=4, column=0, columnspan=2)
        self.aceptarono.botonAceptar.config(command=self.procesos)  # Asigno otra función a este boton.

    def makeOpcionesWgets(self):
        """Simple función que Instancia una clase de los módulos importados."""
        self.archivosopt = MyLabelFrameArchivos(self)               # Contiene wgets relativos a los archivos.
        self.archivosopt.grid(row=3, column=0, columnspan=2, sticky=EW)

    def radio2set(self):
        """Actúa según se elija generar código o ejectable."""
        self.quehacer = self.radios2.getVariable()                  # Asignación de una variable.
        self.archivosopt.setQue(self.quehacer)                      # A otra que esta dentro de otra clase.
        print(self.quehacer)
        if self.quehacer == 1:                                      # Si se elige generar código
            self.opciones1.grid_remove()                            # Se quita de vista lo que no se va a usar
            self.tipoEsCon1.grid_remove()                           # las opciones setup y el tipo de aplicacion.
        else:
            self.opciones1.grid()                                   # Se vuelve a mostrar estos widgets, ya que serán
            self.tipoEsCon1.grid()                                  # usados.

    def radio3set(self, event=None):
        """Asigna a una variable la opción tipo aplicacion: consola o escritorio."""
        self.tipoaplicacion = self.tipoEsCon1.getVariable()
        print(self.tipoaplicacion)
        #self.archivosopt.setQue(self.tipoaplicacion)

    def procesos(self, event=None):
        """Proceso principal a ejecutarse cuando se selecciona aceptar.
        Genera los códigos python o el ejecutable."""
        self.quehacer = self.radios2.getVariable()                  # Averigua qué se desea hacer, codigo o ejecutable.
        if self.quehacer == 1:                                      ## Si código:
            path = self.archivosopt.getPath()                       # Se obtien el path del archivo elegido.
            archivopy = os.path.split(path)[1]                      # Se divide el cuerpo del path de su archivo.
            archivopy = archivopy[:-3] + '.py'                      # A ese archivo se le asigna extension .py
            #print archivopy
            ej.siCodigo(path, archivopy)                            # Se genera arhivo py.
        else:                                                       ## Si ejecutable:
            self.diccionario = self.opciones1.getDiccionario()      # Se obtine el diccionario de las opciones setup.

            self.cadena = """# --*-- coding: utf-8 --*--
from distutils.core import setup
import py2exe
setup(name = u"%s",
description = u"%s",
author = u"%s",
version = u"%s",
license = u"%s",
""" % (self.diccionario['name'], self.diccionario['description'], self.diccionario['author'], self.diccionario['version'],
        self.diccionario['license'])                                # Se agrega a la cadena del setup.

            path = self.archivosopt.getPath()                       # Se obtiene el path elegido.
            archivopy = os.path.split(path)[1]
            escocon = self.tipoEsCon1.getVariable()                 # Se averigua el tipo: consola o escritorio.
            if escocon == 0:                                        ## Si consola:
                tipo = 'console'                                    # Se asigna el console a tipo
            else:                                                   ## si no:
                tipo = 'windows'                                    # Se asigna windows a tipo.
            self.cadenaagregada = '%s = [u"%s"])' % (tipo, path)     # Se genera un string con el tipo de app.
            self.cadena = self.cadena + self.cadenaagregada         # Se concatena esa cadena con la del setup.
            #print self.cadena
            ej.archivar(cadena=self.cadena)                         # Se guarda el setup con contenido de cadena setup.
            ej.siEjecutable()                                       # Se genera el ejecutable.

def main():
    root = Tk()
    ap = MyFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()