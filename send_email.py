import smtplib
from email.message import EmailMessage
import mimetypes
from datetime import datetime

d = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# Create the container email message.
msg = EmailMessage()
msg['Subject'] = "subject"
msg['From'] = 'sender\'s email address'

text1 = """\
Dear,

Email Body.

Good Luck.

"""+d+" [EndOfMessage]"

# add username and password email. might require app password for most email SMTPS/clients.
username = ''
password = ''

# add attachment by passing full filename with path
def create_mail(filename):
    msg.set_content(text1)

    # for pdfs
    with open(filename, 'rb') as file:
        attachment = file.read()
    msg.add_attachment(attachment, maintype='application', subtype='pdf', filename=filename)

    # for images, change type if necessary
    """with open(img, 'rb') as fp:
        img_data = fp.read()
    msg.add_attachment(img_data, maintype='image', subtype='jpg', filename=img)"""

# send email
def s_mail():
    try:
        # define SMTP
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        return 1
    except:
        print('Couldn\'t send email')
        return 0