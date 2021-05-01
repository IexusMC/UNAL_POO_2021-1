import sqlite3  #Librería sqlite3. Está incluída por defecto. Permite elaborar y manipular bases de datos
from sqlite3 import Error 
from PIL import Image #Librería PIL. Está incluída por defecto. Importa el método Image con el fin de producir una imagen.

## TODO comments

try:
    con = sqlite3.connect('Vacunacion.db')
except Error:
    print(Error)
cursorObj = con.cursor()
cursorObj.execute('''
            CREATE TABLE if not exists image (
                noId	INTEGER PRIMARY KEY AUTOINCREMENT,
                image LARGEBLOB
            );
            ''')
con.commit()
def insert(filePath):
    with open(filePath, "rb") as File:
        imagenBinaria = sqlite3.Binary(File.read())
    sqlStatement = "insert into image (image) VALUES ({})"
    cursorObj.execute(sqlStatement.format(sqlite3.Binary(imagenBinaria)))
    cursorObj.commit()
    con.close()

def leer(noLote):
    sqlStatement = "select * from lote_vacunas where noLote = {}"
    cursorObj.execute(sqlStatement.format(noLote))
    imagenBinaria = cursorObj.fetchone()
    rutaDeGuardado = '/Downloads/{}.jpg'.format(imagenBinaria[1])
    with open(rutaDeGuardado, "wb") as File:
        File.write(imagenBinaria[11])
    imagen = Image.open(rutaDeGuardado)
    imagen.show()

# insert('./imagenes/pfizer.jpg')
leer(123456)
