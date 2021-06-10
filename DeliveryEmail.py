import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def deliveryEmail(puntuaciontrain, puntuaciontest, pronostico, datosUlt):
    msg = MIMEMultipart()
    body = "Estimados " \
           "\n\nEsta es la puntuacion del modelo para predecir el siguiente valor del Bitcoin" \
           "\n\nPuntuacion Train: {} RMSE\nPuntuacion Test: {} RMSE" \
           "\n\nPronostico: {}" \
           "\n\nValor Real: {}" \
           "\n\n\nSaludos".format(puntuaciontrain, puntuaciontest, pronostico, datosUlt)
    msg = MIMEText(body)

    msg['From'] = 'pablo.chavez1992@gmail.com'
    msg['To'] = 'pablo.chavez1992@gmail.com'
    msg['Subject'] = 'Pronostico Bitcoin'

    # Reemplaza estos valores con tus credenciales de Google Mail
    username = 'pablo.chavez1992@gmail.com'
    password = 'pablo09291017'

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username, password)
    server.sendmail('pablo.chavez1992@gmail.com','pablo.chavez1992@gmail.com' ,msg.as_string())
    server.quit()

    return print('Mensaje enviado con exito')
