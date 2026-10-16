# Carga RUNT ETL

## Descripción
Aplicación ETL para cargar datos del Registro Único Nacional de Tránsito (RUNT). Esta herramienta permite carga de datos desde un archivo de excel hacia un sistema de almacenamiento.

## Requisitos
- Python 3.x
- Bibliotecas necesarias: `pandas`, `sqlalchemy`, `requests`
- Acceso a la base de datos donde se cargarán los datos.

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/berbelmercado/carga-runt-vecor360.git
   cd carga-runt-vecor360
   ```
2. Instalar las dependencias:
   ```bash
   pip install -r requerimientos.txt
   ```
3. crear archivo .env al mismo nivel que el archivo carga_runt.py con la siguiente estructura:
   ```bash
   SERVIDOR_DB = Tu servidor.
   USUARIO_BD = Usuario de base de datos.
   CLAVE_BD = Clave de base de datos.
   BD_VECORD = Tu base de datos.


   ```
## Uso
1. Ejecutar la aplicación:
   ```bash
   python carga_runt.py
   ```
2. Seguir las instrucciones en pantalla para cargar los datos desde el archivo.xlsx.

## Ejecutable para Windows (sin Python)
### Generar el ejecutable (solo en la máquina de desarrollo)
```bat
build.bat
```
Esto crea `dist\CargaRUNT.exe` (un solo archivo) y copia el `.env` a `dist\`.

### Distribuir a otras máquinas
1. Copiar `CargaRUNT.exe` y el archivo `.env` **en la misma carpeta**.
2. La máquina destino necesita **Microsoft ODBC Driver 17 for SQL Server** instalado
   (es un controlador del sistema y no se puede incluir dentro del ejecutable):
   https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server
3. Ejecutar `CargaRUNT.exe` con doble clic. No se requiere Python.

> El archivo `.env` se lee desde la carpeta del ejecutable, por lo que las credenciales
> pueden cambiarse sin recompilar y no quedan embebidas en el `.exe`.
