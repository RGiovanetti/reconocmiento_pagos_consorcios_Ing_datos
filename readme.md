# Proyecto de Reconocimiento de Pagos de un Consorcio en Extracto de Banco Provincia 🏢💰

## Descripción del Proyecto 📜

Este proyecto tiene como objetivo automatizar el proceso de reconocimiento de pagos realizados por los propietarios de un consorcio. Utilizando Python, pandas y la API de Google Sheets, se desarrolló una herramienta que permite extraer datos de un extracto bancario descargado del homebanking del Banco Provincia (BPI), identificar los pagos y registrar la información en una hoja de cálculo de Google de forma automatizada.


## Tecnologías Utilizadas 🛠️

- **Python**: El lenguaje de programación principal que usamos para el desarrollo del proyecto.
- **Pandas**: Biblioteca de Python para manipular y analizar datos de manera fácil y rápida.
- **gspread**: Biblioteca de Python que nos permite interactuar con Google Sheets sin complicaciones.
- **oauth2client**: Facilita la autenticación y autorización con la API de Google.

## Estructura del Proyecto 📂

1. **`extracto_bancario.py`**: Script principal que lee el archivo del extracto bancario, identifica los pagos y genera un archivo Excel con los resultados.
2. **`subir_a_google_sheets.py`**: Script que carga los pagos reconocidos en una hoja de cálculo de Google.
3. **`cred.json`**: Archivo de credenciales para acceder a la API de Google (¡mantenerlo privado, por favor!).

## Flujo de Trabajo 🔄
## Flujo de Trabajo 🔄

1. **Lectura del Extracto Bancario**: El script `extracto_bancario.py` lee el archivo `ExtractoBancario.xlsx`, busca coincidencias de pagos utilizando un diccionario de propietarios y los registra en un archivo Excel.
2. **Identificación de Pagos**: El sistema busca pagos realizados por los propietarios y clasifica tanto los reconocidos como los no identificados.
3. **Generación de Reportes**: Se genera el archivo `pagos_reconocidos.xlsx`, el cual contiene una lista de pagos identificados de forma automática.
4. **Carga a Google Sheets**: El script `subir_a_google_sheets.py` carga los datos de `pagos_reconocidos.xlsx` a una hoja de cálculo de Google utilizando la API de Google Sheets.

## Cómo Ejecutar el Proyecto 🚀

1. **Instalación de Dependencias**:
   ```bash
   pip install pandas gspread oauth2client openpyxl


## Configuración de Google Sheets 📊

1. **Crea un proyecto en Google Cloud** y habilita la API de Google Sheets y Google Drive.
2. **Generá credenciales de tipo "Servicio"** y descargá el archivo `cred.json`.

## Ejecutar el Script 🏃‍♂️

1. Asegurate de tener el archivo de extracto bancario (`ExtractoBancario.xlsx`) en la misma carpeta que los scripts.
2. Ejecutá el script de reconocimiento de pagos:
   ```bash
   python extracto_bancario.py

## Por último

1. Ejecutá el script para subir los datos a Google Sheets:
   ```bash
   python extracto_bancario.py

## ⚠️ Datos del Proyecto

**Aviso Importante** Los archivos presentes, ExtractoBancario.xlsx y Pagos_reconocidos.xlsx, son ejemplos ficticios creados para demostrar el funcionamiento del programa. Estos archivos contienen nombres de actores de Hollywood para proteger la privacidad y evitar la exposición de datos sensibles.

## Importante:
 - Datos ficticios: Los datos que ves en los archivos proporcionados son **totalmente ficticios**. Si intentas correr el programa con estos archivos, no obtendrás resultados reales porque no representan datos válidos o actuales.
 - Credenciales de Google API: Para que el programa funcione correctamente, deberás solicitar y configurar tus propias credenciales de la API de Google, ya que estas no están incluidas en el repositorio por motivos de seguridad. Consulta la documentación oficial de Google para obtener más información sobre cómo generar estas credenciales.

## Aprendizajes y Futuro 🎓✨
A través de este proyecto, pude aplicar y fortalecer mis habilidades en Python, manipulación de datos con pandas y la integración con APIs. Como aspirante a ingeniero de datos, este proyecto representa un paso importante en mi carrera, ya que me ha permitido trabajar en la automatización de procesos y en la gestión de datos.


## Contribuciones 🤝
Si querés contribuir a este proyecto, no dudes en abrir un issue o enviar un pull request. Tené en cuenta que para hacer pruebas reales deberás generar tus propios datos(ingrensando al Banco Provincia y bajando el extracto) y además descargar tus propias credenciales de la API de Google, ya que los archivos proporcionados son ejemplos ficticios.

