import smtplib #Librería smtplib esta incluida por defecto. Permite la creación y envío de correos electrónicos.
from email.mime.multipart import MIMEMultipart #Librería incluída por defecto MIMEMultipart, con el fin de organizar los datos relacionados a la aplicación de correos electrónicos (remitente y destinatario).
from email.mime.text import MIMEText #Librería incluída por defecto. Se importa MIMEText para permitir la redacción del mensaje a enviar por correo electrónico.

mensajeObj = MIMEMultipart()
mensaje = 'Hola\nEste es un mensaje de prueba para mi app'


mensajeObj['From'] = 'pruebas.vacunacion@gmail.com'
mensajeObj['To'] = 'jugarciale@unal.edu.co'
mensajeObj['Subject'] = 'Email de prueba'
password = 'TEST_123*'

mensajeObj.attach(MIMEText(mensaje, 'plain'))

try:
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(mensajeObj['From'], password)

    server.sendmail(mensajeObj['From'], mensajeObj['To'], mensajeObj.as_string())
    print('correo enviado')
    server.quit()
except:
    print('error')
