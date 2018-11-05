# --*-- coding: utf-8 --*--
# --*-- coding: utf-8 --*--

import os
def archivar(setup='setup', cadena=''):
    setup = setup + '.py'
    with open(setup, 'w') as f:
        f.write(cadena)



#archivar(cadena='from Tkinter import*')
def siCodigo(archivoUI, archivoSalida):
    """Genera el codigo a partir del archivo UI."""
    import os
    cadena = '''C:\Python27\Lib\site-packages\PyQt4\pyuic4 %s -o %s''' % (archivoUI, archivoSalida)
    print(cadena)
    os.system(cadena)

def siEjecutable():
    """Ejecuta los comandos para generar el ejecutable."""
    cadena = 'python setup.py py2exe'
    os.system(cadena)
    os.system('exit')

def makeString(tipo=0, archivopy='sinnombre'):
    """Retorna una cadena modelo del setup, se tiene que ingresar el nombre del archivo py."""
    if tipo ==0:
        tipo = 'console'
    else:
        tipo = 'windows'

    cadenasetup = """# --*-- coding: utf-8 --*--
from distutils.core import setup
import py2exe

setup(
name = 'Asistente para ejecutar py2exe',
description = u'Crea ejecutales de Python',
author = 'David Emanuel Sandoval',
version = '1.0.0.1',
packages = [],
platforms = 'nt',
data_files = [('bitmaps', []), ('config', [])],
py_modules = [],
license = 'General Public License',
%s=(['%s']))
    """ % (tipo, archivopy)
    return cadenasetup

