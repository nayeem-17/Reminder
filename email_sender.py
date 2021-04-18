import smtplib
import ssl
import os


def send_email(receiver_email, subject, message):
    smtp_server = "smtp.gmail.com"
    port = os.getenv('PORT')
    password = os.getenv('EMAIL_PASS')
    sender_email = os.getenv('EMAIL_ID')

    context = ssl.create_default_context()

    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email,
                        f"Subject:{subject}\n\n{message}")
        print('Successfull')
        server.quit()
    except:
        print("Something's wrong!! i can feel it!")
