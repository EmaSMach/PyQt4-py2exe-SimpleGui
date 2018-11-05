# --*-- coding: utf-8 --*--
from tkinter import *
from tkinter.filedialog import askopenfilename

class MyLabelFrameArchivos(LabelFrame):
    """Clase que sirve para seleccionar el o los archivos a procesar."""
    def __init__(self, parent=None, que=0):
        LabelFrame.__init__(self, parent)
        self.grid()
        self.que = que
        self.nombre = ''
        self.config(text='Archivo')
        # if self.que == 0:                                                    # Defino variables según flag que == 0
        #     self.nombre = u'Archivo PY'                                 # Texto del label.
        #     self.tipoarchivo = [("Archivos PYTHON", ("*.py", "*.pyw"))] # Tipos de archivos a buscar.
        # else:                                                           # Defino variables según flag que != 0
        #     self.nombre = u'Archivo UI'                                 # Texto del label.
        #     self.tipoarchivo = [("Archivos UI", "*.ui")]              # Tipos de archivos a buscar.

        self.makeWidgets()

    def getSet(self):
        if self.que == 0:                                                    # Defino variables según flag que == 0
            self.nombre = 'Archivo PY'                                 # Texto del label.
            self.tipoarchivo = [("Archivos PYTHON", ("*.py", "*.pyw"))] # Tipos de archivos a buscar.
        else:                                                           # Defino variables según flag que != 0
            self.nombre = 'Archivo UI'                                 # Texto del label.
            self.tipoarchivo = [("Archivos UI", "*.ui")]



    def makeWidgets(self):
        """Crea los widgets Label, Entry y Examinar."""
        self.lblarchivopy = Label(self, text=self.nombre)
        self.enarchivopy = Entry(self, width=40)
        self.btnexaminar = Button(self, text='Examinar', command=self.examinar)
        self.lblarchivopy.grid(row=0, column=0)
        self.enarchivopy.grid(row=0, column=1, sticky=EW)
        self.btnexaminar.grid(row=0, column=2)
        self.columnconfigure(1, weight=1)

    def examinar(self):
        """Abre el cuadro de diálogo para buscar un archivo."""
        self.getSet()
        path = askopenfilename(title='Elija el archivo PYTHON', filetypes=self.tipoarchivo)
        self.enarchivopy.delete(0, END)
        self.enarchivopy.insert(0, path)

    def getPath(self):
        """Retorna el path actual del Entry."""
        return self.enarchivopy.get()

    def setQue(self, nvalor):
        self.que = nvalor

class Acciones(LabelFrame):
    """Clase que forma los botones Aceptar o Cancelar y sus acciones."""
    def __init__(self, parent=None):
        LabelFrame.__init__(self, parent)
        self.grid(sticky=EW)
        self.configure(text='Acciones')

        self.makeButtons()

    def makeButtons(self):
        """Crea los botones Aceptar y Cancelar."""
        self.botonAceptar = Button(self, text='Aceptar', command=self.onAceptarButton)
        self.botonSalir = Button(self, text='Salir', command=self.onSalirButton)
        self.botonAceptar.grid(row=0, column=0)
        self.botonSalir.grid(row=0, column=1, sticky='e')
        self.columnconfigure(1, weight=1)

    def onAceptarButton(self, funcion):
        pass

    def onSalirButton(self):
        self.quit()


def main():
    root = Tk()
    root.columnconfigure(0, weight=1)
    ap = MyLabelFrameArchivos()
    root.mainloop()

if __name__ == '__main__':
    main()