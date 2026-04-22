from controlador.cargar_runt_controlador import CargarRuntControllador
from dotenv import load_dotenv
from utilidades.resolver_rutas import resource_path

class Main():
    @staticmethod
    def inicio():
        load_dotenv(resource_path('.env'))
        CargarRuntControllador.etl_runt()

if __name__ == "__main__":
    Main.inicio()