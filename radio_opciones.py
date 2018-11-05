# --*-- coding: utf-8 --*--
from tkinter import *

class MyLabelFrameRadio(LabelFrame):
    """Clase de LabelFrame que contiene dos radiobuttons, indicando versión de python."""
    def __init__(self, parent=None, **conf):
        LabelFrame.__init__(self, parent, conf)
        self.grid()
        self.config(text='Versión de Python')
        self.variableTipos = IntVar()  # Instanciamos una variable INT.
        self.makeRadioTipos()

    def makeRadioTipos(self):
        """Agregamos los radiobuttons."""
        self.radiotipo1 = Radiobutton(self, value=0, variable=self.variableTipos, text='Python 2')
        self.radiotipo2 = Radiobutton(self, value=1, variable=self.variableTipos, text='Python 3', state='disable')
        self.radiotipo1.grid()
        self.radiotipo2.grid()

    def getVariable(self):
        return self.variableTipos.get()

class MyLabelFrameRadioQue(LabelFrame):
    """Clase de LabelFrame que contiene dos radiobuttons, indcando accion a ejecutar."""
    def __init__(self, parent=None, **conf):
        LabelFrame.__init__(self, parent, conf)
        self.grid()
        self.config(text='Acción a Ejecutar')
        self.variableQue = IntVar()  # Instanciamos una variable INT.
        self.makeRadioTiposQue()

    def makeRadioTiposQue(self):
        """Agregamos los radiobttons."""
        self.radiotipo1 = Radiobutton(self, value=0, variable=self.variableQue, text='Generar Ejecutable')
        self.radiotipo2 = Radiobutton(self, value=1, variable=self.variableQue, text='Generar Código', anchor='w')
        self.radiotipo1.grid()
        self.radiotipo2.grid(sticky=EW)  # Incdico que ocupe todo el espacio restante, con anchor se alineará a la
                                         # Izquierda.

    def getVariable(self):
        """Retorna la variable de los radiobuttons"""
        return self.variableQue.get()

def main():
    root = Tk()
    MyLabelFrameRadio(root)
    MyLabelFrameRadioQue(root)
    root.mainloop()


if __name__ == '__main__':
    main()
    