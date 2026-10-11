import ssl
from smtplib import SMTP_SSL, SMTPResponseException
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMail(receiverEmail, capturedImageName):

    smtp_server = "smtp.gmail.com"
    # port = 587  # For starttls
    port = 465  # For SSL

    sender_email = "a@gmail.com"
    password = "pass"

    receiver_email = receiverEmail

    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Add File
    filename = f"{capturedImageName}"  # In same directory as script
    print(receiver_email)
    print(filename)
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        with SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
    except SMTPResponseException as error:
        print(error.smtp_code)
        print(error.smtp_error)
