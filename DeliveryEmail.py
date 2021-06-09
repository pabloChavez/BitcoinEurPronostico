import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def deliveryEmail(Puntuacion_Train, Puntuacion_Test, proximodia, datosUlt):
    msg = MIMEMultipart()
    body = "Estimados " \
           "\n\nEsta es la puntuacion del modelo para predecir el siguiente valor del Bitcoin" \
           "\n\nPuntuacion Train: {} RMSE\nPuntuacion Test: {} RMSE" \
           "\n\nPronostico: {}" \
           "\n\nValor Real: {}".format(Puntuacion_Train, Puntuacion_Test, proximodia, datosUlt)
    msg = MIMEText(body)

    msg['From'] = ''
    msg['To'] = ''
    msg['Subject'] = 'Pronostico Bitcoin'

    # Reemplaza estos valores con tus credenciales de Google Mail
    username = ''
    password = ''

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username, password)
    server.sendmail('','' ,msg.as_string())
    server.quit()

    return print('Mensaje enviado con exito')