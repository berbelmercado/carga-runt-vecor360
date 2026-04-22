# Carga RUNT ETL

## Descripción
Aplicación ETL para cargar datos del Registro Único Nacional de Tránsito (RUNT). Esta herramienta permite la extracción, transformación y carga de datos desde diversas fuentes hacia un sistema de almacenamiento.

## Características
- **Interfaz fácil de usar**: Proporciona una interfaz gráfica para facilitar la carga de datos.
- **Soporte para múltiples fuentes**: Capacidad para integrar datos de diferentes fuentes.
- **Transformaciones personalizables**: Permite aplicar transformaciones necesarias a los datos antes de cargarlos.
- **Integración con bases de datos**: Compatible con diversas bases de datos para almacenamiento.

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
   pip install -r requirements.txt
   ```

## Uso
1. Ejecutar la aplicación:
   ```bash
   python main.py
   ```
2. Seguir las instrucciones en pantalla para cargar los datos desde el RUNT.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.  

Si tienes preguntas, contacta al autor en: berbelmercado@gmail.com