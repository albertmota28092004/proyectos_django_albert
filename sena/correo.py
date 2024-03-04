from email.message import EmailMessage
import smtplib

remitente = "andresmao606@gmail.com"
destinatario = "andresmao606@gmail.com"
mensaje = """
 
 <h1 style="color:green;"> +cotitas </h1>
<p>Su pedido esta en camino</p> 
 """

email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Correo de prueba"
email.set_content(mensaje, subtype="html")
email.set_content(mensaje)

smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "ipuhlxibhijcilzf")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()