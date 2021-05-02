import smtplib
from email.message import EmailMessage

from config import sender, receiver, smtp
from setting import render


def send_smtp_mail_sample(subject, body):
    """
    Send a plain text email
    """
    message = f'To : {receiver["email"]} \r\n'
    message = message + f'Subject : {subject} \r\n'
    message = message + body
    """
        To: Receiver
        Subject: Subject
        
        Body...
    """

    try:
        with smtplib.SMTP(smtp['server'], smtp['port']) as server:
            server.ehlo()
            server.starttls()
            server.login(user=sender['email'], password=sender['password'])

            server.sendmail(
                sender['email'],
                receiver['email'],
                message
            )
        print('Successfully send the mail')
    except Exception:
        print('Failed to send mail')


def send_smtp_mail(body):
    """
    Send an email with more advanced settings(HTML page)
    """
    message = EmailMessage()

    message['from'] = sender['email']
    message['to'] = receiver['email']
    message['subject'] = '<<<Report exchange rates in fixer.io>>>'

    html_message = body

    message.set_content(html_message, 'html')

    try:
        with smtplib.SMTP(smtp['server'], smtp['port']) as server:
            server.ehlo()
            server.starttls()
            server.login(user=sender['email'], password=sender['password'])

            server.send_message(message)
        print('Successfully send the mail')
    except Exception:
        print('Failed to send mail')


send_smtp_mail(body=render)
