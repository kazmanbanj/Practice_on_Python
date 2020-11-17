import smtplib      # this creates a smtp server to send email
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Banjoko Kazeem'
email['to'] = 'banjoko10@gmail.com'
email['subject'] = 'Hello there'

email.set_content('I am using Python to send this email, expect more from me later... Bye for now')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('banjoko2020@gmail.com', 'input_password')
    smtp.send_message(email)
    print('email sent!!!')


# to send email, run: python email_sender.py