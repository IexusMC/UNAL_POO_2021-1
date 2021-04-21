import sqlite3
from sqlite3 import Error

## TODO comments

try:
    con = sqlite3.connect('prueba.db')
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
    cursorObj.execute(sqlStatement.format(imagenBinaria))
    cursorObj.commit()
    con.close()

insert('/home/alpha23/Pictures/Screenshot_20210316_011734.png')
