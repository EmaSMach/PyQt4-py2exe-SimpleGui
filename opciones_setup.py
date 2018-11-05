# --*-- coding: utf-8 --*--
from tkinter import *

class MyLabelFrame(LabelFrame):
    """Inicia el contenedor de los Widgets"""
    def __init__(self, parent=None, tipo='console', **conf):
        LabelFrame.__init__(self, parent, conf)
        self.grid()
        self.config(text='Opciones del Setup', width=500)
        self.dictopciones = {'name': '',           # Distintas opciones el setup.
                             'description': '',
                             'version': '',
                             'author': '',
                             'license': '',
                             }
        #self.diccionario = {}
        self.crearWidgets()

        #self.btn = Button(self, text='Averiguar', command=self.getDiccionario)
        #self.btn.grid()
    def crearWidgets(self):
        """Crea los widgets según items del diccionario de opciones."""
        nfila = 0; ncol = 0
        for k, v in list(self.dictopciones.items()):
            self.lbl = Label(self, text=k)
            self.en = MyEntry(self, llave=k)
            self.lbl.grid(row=nfila, column=ncol)
            self.en.grid(row=nfila, column=ncol + 1, sticky=EW)
            nfila += 1

    def getDiccionario(self):
        """Retorna el diccionario de opciones"""
        return self.dictopciones


class MyEntry(Entry):
    """Clase que define un Entry que puede retornar su contenido y se le puede asignar
    un atributo llamado llave."""
    def __init__(self, parent=None, llave='', nfila=0, ncol=0, **conf):
        Entry.__init__(self, parent, conf)
        self.grid(row=nfila, column=ncol)
        self.config(width=45)
        self.llave = llave                          # Contendrá la llave del diccionario.
        self.bind('<KeyRelease>', self.valoraDict)      # Conectamos temporalmente con este método.

    def getValor(self, event=None):
        """Retorna el valor actual del Entry"""
        return self.get()                           # Retorna el valor del Entry.

    def getLlave(self, event=None):
        """Retorna el valor de self.llave"""
        return self.llave

    def valoraDict(self, event=None):
        """Agrega el valor del Entry en la llave del diccionario"""
        valor = self.getValor()                     # Otenemos el valor del Entry.
        llave = self.getLlave()                     # Y del atributo llave.
        self.master.dictopciones[llave] = valor     # Y Asignamos el valor a la llave del diccionario.

    def desactivar(self, event=None):
        self.config(state='disable')

def main():
    root = Tk()
    w = MyLabelFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()