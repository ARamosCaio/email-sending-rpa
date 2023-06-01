from email.message import EmailMessage
import smtplib
import imghdr

email = 'caio.araujo.cvo@gmail.com'
senha = input('Digite a senha do email: ')

msg = EmailMessage()
msg['Subject'] = 'Email automático'
msg['From'] = email
msg['To'] = 'lety5000.amarante@gmail.com'
msg.set_content('Teste de e-mail automático utilizando python')

files = ['1.png', '2.png']

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, senha)
    smtp.send_message(msg)