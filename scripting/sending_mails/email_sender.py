import smtplib      # this creates a smtp server to send email
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Banjoko Kazeem'
email['to'] = 'banjoko10@gmail.com'
email['subject'] = 'Hello there'

email.set_content(html.substitute({'name': 'Jaho'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('banjoko2020@gmail.com', 'mail_password_here')
    smtp.send_message(email)
    print('email sent!!!')


# to send email, run: python email_sender.py