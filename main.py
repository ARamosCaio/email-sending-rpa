from email.message import EmailMessage
import smtplib
import imghdr
from info import EMAIL, PASSWORD

msg = EmailMessage()
msg['Subject'] = 'Email automático pelo python'
msg['From'] = EMAIL
msg['To'] = input('Insira o email destinatário: ')
msg.set_content('Prezado(a), boa noite\n\nSegue em anexo a tabela IGP-DI atualizada\n\nAtenciosamente,\n\nCaio Ramos')

pdf_file = 'igpdi.pdf'
    
with open(pdf_file, 'rb') as f:
    file_data = f.read()
    file_name = f.name

    msg.add_attachment(
        file_data,
        maintype='application',
        subtype='octect-stream',
        filename = file_name
    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL,PASSWORD)
    smtp.send_message(msg)