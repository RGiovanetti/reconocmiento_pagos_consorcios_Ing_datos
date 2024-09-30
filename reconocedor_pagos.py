import pandas as pd
import re

propietarios = {
    'C:93458261792': 'Chris Evans',
    'S.123456 C:93458261792': 'Chris Evans',
    'S.123456': 'Chris Evans',
    'C.456789123457 D:34567891234': 'Scarlett Johansson',
    'D:34567891234': 'Scarlett Johansson',
    'C.456789123457': 'Scarlett Johansson',
    'C.654321 D:45678912345': 'Leonardo DiCaprio',
    'C.654321': 'Leonardo DiCaprio',
    'D:45678912345': 'Leonardo DiCaprio',
    'C.987654 D:56789012345': 'Natalie Portman',
    'C.987654': 'Natalie Portman',
    'D:56789012345': 'Natalie Portman',
    'C.123789 D:67890123456': 'Tom Hanks',
    'C.123789': 'Tom Hanks',
    'D:67890123456': 'Tom Hanks',
    'C.345678 D:78901234567': 'Jennifer Lawrence',
    'C.345678': 'Jennifer Lawrence',
    'D:78901234567': 'Jennifer Lawrence',
    'C.321654 D:89012345678': 'Robert Downey Jr.',
    'C.321654': 'Robert Downey Jr.',
    'D:89012345678': 'Robert Downey Jr.',
    'C.987654321012 D:90123456789': 'Emma Stone',
    'C.987654321012': 'Emma Stone',
    'D:90123456789': 'Emma Stone',
    'DNI 98765432': 'Brad Pitt',
    'C.246801 D:23456789012': 'Angelina Jolie',
    'C.246801': 'Angelina Jolie',
    'D:23456789012': 'Angelina Jolie',
    'C.135790 D:34567890123': 'Matthew McConaughey',
    'C.135790': 'Matthew McConaughey',
    'D:34567890123': 'Matthew McConaughey',
    'C.864209 D:45678901234': 'Margot Robbie',
    'C.864209': 'Margot Robbie',
    'D:45678901234': 'Margot Robbie',
    'C.357159 D:56789012345': 'Will Smith',
    'C.357159': 'Will Smith',
    'D:56789012345': 'Will Smith',
    'C:78945612378': 'Zendaya',
    'S.258963 C:78945612378': 'Zendaya',
    'S.258963': 'Zendaya',
    'C.159753 D:98765432100': 'Denzel Washington',
    'D:98765432100': 'Denzel Washington',
    'C.159753': 'Denzel Washington',
    'C.753951 D:12345678901': 'Meryl Streep',
    'C.753951': 'Meryl Streep',
    'D:12345678901': 'Meryl Streep',
    'C.258147 D:23456789012': 'Harrison Ford',
    'C.258147': 'Harrison Ford',
    'D:23456789012': 'Harrison Ford',
    'C.321987 D:45678901234': 'Ryan Reynolds',
    'C.321987': 'Ryan Reynolds',
    'D:45678901234': 'Ryan Reynolds',
    'C.654789 D:12345678901': 'Charlize Theron',
    'C.654789': 'Charlize Theron',
    'D:12345678901': 'Charlize Theron',
    'C.789321 D:23456789012': 'Jason Momoa',
    'C.789321': 'Jason Momoa',
    'D:23456789012': 'Jason Momoa',
    'C.987321 D:34567890123': 'Gal Gadot',
    'C.987321': 'Gal Gadot',
    'D:34567890123': 'Gal Gadot',
    'C.159753 D:78901234567': 'Chris Hemsworth',
    'C.159753': 'Chris Hemsworth',
    'D:78901234567': 'Chris Hemsworth',
}

fila_encabezado = 1

# Leemos el archivo Excel y usamos la fila especificada como encabezado de columnas.
df = pd.read_excel('ExtractoBancario.xlsx', header=fila_encabezado)

# Creamos una lista donde vamos a guardar los resultados.
resultados = []

# Acá bajamos el extracto bancario, en este caso es del Banco Provincia, pero este proyecto se adapta a cualquier banco con un par de ajustes.
# Elegimos la fecha que queremos analizar, tipo "20-9-2024 al 13-10-2024". Es clave que el banco solo traiga los créditos en lugar de débitos y créditos
#  que son los pagos que hacen los propietarios, una vez que leímos el archivo ExtractoBancario.

for index, row in df.iterrows():
    descripcion_pago = row['Descripción Extendida']  # Acá vemos la descripción del pago que el banco le pone al propietario.
    fecha = row['Fecha']  # La fecha del pago.
    importe = row['Importe']  # El importe total que ingresó.
    encontrado = False
    # Iteramos sobre cada propietario para buscar coincidencias.
    # Cuando llega un pago que no tenemos reconocido, chequeamos si el propietario avisó por algún medio.
    # Luego, separamos la descripción extendida en sus partes (por ejemplo, C:, D:, ORI:).
    # Una vez que identificamos a quién pertenece, cargamos en la base de datos el propietario 
    # con la descripción dividida en partes, ya que a veces el DNI ("D:") aparece si el pago se realiza 
    # desde otra cuenta o banco diferente.

    for codigo, propietario in propietarios.items():
        if re.search(r'\b' + re.escape(codigo) + r'\b', descripcion_pago):
            resultados.append({
                'propietario': propietario,
                'Pago': importe,
                'Fecha': fecha,
                'identificado': 'SI',
                'Descripción Extendida': descripcion_pago,
            })
            encontrado = True
            break  # Salimos del bucle una vez que se encuentra una coincidencia.
    
    if not encontrado:
        resultados.append({
            'propietario': 'No identificado',
            'Pago': importe,
            'Fecha': fecha,
            'identificado': 'NO',
            'Descripción Extendida': descripcion_pago,
        })
        # SE AGREGA la columna identificado "sí o no" para poder filtrar fácilmente entre los que no se encontraron.

# Convertimos la lista de resultados en un DataFrame.
df_resultados = pd.DataFrame(resultados)

# Invertimos el orden del DataFrame para que los pagos más recientes aparezcan primero, esto se hace con el objetivo de cargarlo
#posteriormente en un google drive.
df_resultados = df_resultados[::-1]

# Una vez listo lo guardamos en un archivo Excel.
df_resultados.to_excel('pagos_reconocidos.xlsx', index=False)
