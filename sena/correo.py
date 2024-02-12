from email.message import EmailMessage
import smtplib

remitente = "argenisgaray28@gmail.com"
destinatario = "juanestebanhernandezr913@gmail.com"
mensaje = "¡Hola, gay!"
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Correo de prueba ADSO Python"
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "yaglmdpripqilfdz")
try:
    smtp.sendmail(remitente, destinatario, email.as_string())
    print("Correo enviado")
except Exception as e:
    print(f"Error: {e}")
smtp.quit()
