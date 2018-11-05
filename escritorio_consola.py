# --*-- coding: utf-8 --*--
from tkinter import *


class MyLabelFrameEsCon(LabelFrame):
    def __init__(self, parent=None, **conf):
        LabelFrame.__init__(self, parent, conf)
        self.config(text='Tipo de aplicación')
        self.grid()

        self.makeWidgets()

    def makeWidgets(self):
        self.varexcon = IntVar()
        self.radioEsCon1 = Radiobutton(self, text='Consola', variable=self.varexcon, value=0)
        self.radioEsCon2 = Radiobutton(self, text='Escritorio', variable=self.varexcon, value=1)
        self.radioEsCon1.grid(row=0, column=0, sticky=W)
        self.radioEsCon2.grid(row=1, column=0)

    def getVariable(self):
        return self.varexcon.get()

def main():
    MyLabelFrameEsCon().mainloop()

if __name__ == '__main__':
    main()