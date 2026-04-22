from vista.gui_general import GuiGeneral
from modelo.procesar_archivo import ProcesarArchivo
from modelo.inserta_datos import InsertaDatos

class CargarRuntControllador():
    """
    Clase para gestionar la lectura, transformación y carga de archivos RUNT.
    Se encarga de la extracción, transformación y carga (ETL) de los datos,
    así como de la gestión de mensajes informativos y de error para el usuario.
    """

    @staticmethod
    def etl_runt():
        """
        Ejecuta el proceso ETL para cargar datos RUNT:
        1. Solicita al usuario seleccionar un archivo.
        2. Verifica si el archivo está vacío.
        3. Lee el archivo y procesa los datos.
        4. Intenta conectar a la base de datos.
        5. Inserta los datos procesados en la base de datos.
        6. Muestra mensajes informativos o de error según el resultado de cada paso.
        """
        #Declaramos variables
        estado_procesamiento_archivo = None
        dataframe_procesado = None
        ruta_archivo = GuiGeneral.cargar_archivo()#Obtenemos la ruta del archivo a procesar

        #Declaramos los objetos
        obj_archivo = ProcesarArchivo(ruta_archivo)
        obj_inserta_datos = InsertaDatos()

        #Validamos si el archivo está vacío
        if not obj_archivo.archivo_vacio():
            #Leemos el archivo
            if obj_archivo.leer_archivo():
                #Limpiamos y filtramos la data
                estado_procesamiento_archivo,dataframe_procesado = obj_archivo.procesar_archivo()

                if estado_procesamiento_archivo:
                    if  obj_inserta_datos.conexion_sql():
                        #Insertamos los datos filtrados ala base de datos
                        if obj_inserta_datos.insertar_datos(dataframe_procesado):
                            GuiGeneral.mostrar_mensaje_informativo('Se cargó correctamente la información')
                        else:
                                GuiGeneral.mostrar_mensaje_error('No fue posible insertar la información en la base de datos')
                    else:
                        GuiGeneral.mostrar_mensaje_error('Error en la conexión a la Base de datos') 
            else:
                GuiGeneral.mostrar_mensaje_error('Error al leer el archivo')
        else:
                GuiGeneral.mostrar_mensaje_error('El archivo está vacío')
