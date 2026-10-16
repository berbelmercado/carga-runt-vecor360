from controlador.cargar_runt_controlador import CargarRuntControllador
from dotenv import load_dotenv
from utilidades.resolver_rutas import ruta_ejecutable

class Main():
    @staticmethod
    def inicio():
        load_dotenv(ruta_ejecutable('.env'))
        CargarRuntControllador.etl_runt()

if __name__ == "__main__":
    Main.inicio()