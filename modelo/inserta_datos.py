
import pyodbc
import pandas
from os import getenv
class InsertaDatos:

    def __init__(self):
        """
        Inicializa la clase InsertaDatos con las credenciales de la base de datos.
        """
        self.servidor = getenv('SERVIDOR_DB')
        self.usuario = getenv('USUARIO_BD')
        self.clave = getenv('CLAVE_BD')
        self.bd_vecor = getenv('BD_VECORD')

    def conexion_sql(self):
        """
        Establece la conexión a la base de datos SQL Server.

        Returns:
        --------
        bool
            True si la conexión es exitosa, False en caso contrario.
        """
        try:
            self.cnx = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.servidor};DATABASE={self.bd_vecor};UID={self.usuario};PWD={self.clave}')
            self.cursor = self.cnx.cursor()
            self.cursor.fast_executemany = True

            return True
        except:
            return False

    def insertar_datos(self,dataframe):
        """
        Inserta los datos de un DataFrame en la tabla temporal de la base de datos.

        Parámetros:
        -----------
        dataframe : pandas.DataFrame
            DataFrame que contiene los datos a insertar.
        """
        query_sql = f'INSERT INTO temp_carga_runt (VIN,CANAL,Fecha,PLACA) VALUES (?,?,?,?)'

        try:
            self.cursor.setinputsizes(self.__typeToSize(dataframe))
            self.cursor.executemany(query_sql, dataframe.values.tolist())
            if self.__delta_data():
                self.cursor.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
        finally:
            self.cursor.close()
            self.cnx.close()

    def __typeToSize(self,df):
        """
        Determina los tamaños de los tipos de datos en el DataFrame para la inserción en la base de datos.

        Parámetros:
        -----------
        df : pandas.DataFrame
            DataFrame que contiene los datos a insertar.

        Returns:
        --------
        list
            Lista de tamaños de los tipos de datos.
        """
        try:
            types = df.dtypes.values.tolist()
            size = []

            for i in types:
                if i in ["int64", "int32"]:
                    size.append(pyodbc.SQL_INTEGER)
                elif i == "object":
                    size.append((pyodbc.SQL_WVARCHAR, 255))
                elif i == "float64":
                    size.append(pyodbc.SQL_DOUBLE)
                elif i in ["<M8[ns]", "datetime64[ns]"]:
                    size.append(pyodbc.SQL_TYPE_TIMESTAMP)
                elif i == "bool":
                    size.append(pyodbc.SQL_INTEGER)

            return size
        except Exception as e:
            self.obj_log.error(f'error size {e}')
        
    def __delta_data(self):
        """
        Ejecuta una consulta SQL para mover los datos de la tabla temporal a la tabla principal y limpiar la tabla temporal.
        """
        try:
            #Consulta SQL
            sql_query = f"""	UPDATE  T
		                SET T.[LicensePlate]=PLACA,
			                [LicensePlateDate]=Fecha,
			                LicensePlateDescription=4
	                    FROM [dbVentasCorporativas]..Trackings T
		                    inner join [dbVentasCorporativas]..temp_carga_runt M ON T.VIN=M.VIN
	                    WHERE T.LicensePlateDate IS NULL
		                        AND T.LicensePlateDescription<>4
                        """
            sql_query_limpiar = f"""DELETE [dbVentasCorporativas]..temp_carga_runt
                                """
            #Ejecutamos consulta
            self.cursor.execute(sql_query)
            self.cursor.execute(sql_query_limpiar)
            return True
        except Exception as ex:
            print(ex)
            return False
