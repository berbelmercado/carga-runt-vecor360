"""modulo para resolver rutas base y rutas relativas"""
import os
import sys

def resource_path(ruta_relativa):
    """resuelve las rutas"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,ruta_relativa)


def ruta_ejecutable(ruta_relativa):
    """resuelve rutas junto al ejecutable (o junto al script si no está empaquetado)"""
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(base_path, ruta_relativa)
