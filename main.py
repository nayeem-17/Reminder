from .emai_sender import email_sender

if __name__ == "__main__":
    subject = "Make it Quick"
    message = "Check facebook and make me admin T-T"
    email_sender(receiver_email='',
                 subject=subject,
                 message=message)
