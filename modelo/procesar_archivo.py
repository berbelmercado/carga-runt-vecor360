import pandas as pd
from os import path

class ProcesarArchivo:
    """
    Clase para procesar archivos de reporte RUNT en formato Excel.
    Permite verificar si el archivo está vacío, leerlo y filtrar los datos relevantes.
    """
    def __init__(self,ruta_archivo_runt):
        """
        Inicializa la clase ProcesarArchivo con la ruta del archivo de reporte.
        
        :param ruta_archivo_runt: Ruta al archivo de reporte RUNT en formato Excel.
        """
        self.archivo_reporte = ruta_archivo_runt
        self.dataframe_filtrado = pd.DataFrame()

    def archivo_vacio(self):
        """
        Verifica si el archivo de reporte está vacío.
        
        :return: True si el archivo está vacío, False en caso contrario.
        """
        if path.getsize(self.archivo_reporte) == 0:
            return True
        return False

    def leer_archivo(self):
        """
        Lee el archivo de reporte y lo carga en un DataFrame de pandas.
        
        :return: True si la lectura fue exitosa, False si ocurrió un error.
        """
        try:
            self.dataframe = pd.read_excel(self.archivo_reporte)
            return True
        except:
            return False

    def procesar_archivo(self):
        """
        Procesa y filtra los datos del archivo de reporte.
        Crea una columna de fecha a partir de las columnas 'AÑO_MATRICULA', 'MES_MATRICULA' y 'DIA_MI',
        convierte la columna a tipo datetime y filtra las columnas relevantes.
        
        :return: Una tupla (True, dataframe_filtrado) si el procesamiento fue exitoso,
                 (False) si ocurrió un error.
        """
        try:
            #Juntar 3 columnas en una sola columna de fechas
            self.dataframe["Fecha"] = (
                self.dataframe['AÑO_MATRICULA'].astype(str) + '-' +
                self.dataframe['MES_MATRICULA'].astype(str).str.zfill(2) + '-' +
                self.dataframe['DIA_MI'].astype(str).str.zfill(2)
            )
            # Modificar columna fecha
            self.dataframe["Fecha"] = pd.to_datetime(self.dataframe["Fecha"], errors="coerce")
            self.dataframe["Fecha"] = self.dataframe["Fecha"].dt.strftime("%Y-%m-%d")
            self.dataframe["Fecha"] = self.dataframe["Fecha"].where(self.dataframe["Fecha"].notna(), None)

            #Filtramos los datos del archivo y lo guardamos en un nuevo Dataframe
            self.dataframe_filtrado = self.dataframe[['VIN','CANAL','Fecha','PLACA']]

            self.dataframe_filtrado.to_excel('dataframe_filtrado.xlsx', index=False)

            return True,self.dataframe_filtrado
        except Exception as e:
            print(e)
            return False,self.dataframe_filtrado


