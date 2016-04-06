#!/usr/local/bin/python3
"""
Function to create a MIME standard email which can be multipart
Input 1: str[from address, to address, subject] - required
Input 2: list[name(s) of files to be attached] - Optional
"""

def e_create(sender, receiver, subject, action='return', attachments=None):
    import smtplib
    import mimetypes
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.audio import MIMEAudio
    
    mimemod_to_use = {'text': MIMEText, 'image': MIMEImage, 'audio': MIMEAudio}

    msg = MIMEMultipart()
    msg['To'] = receiver
    msg['From'] = sender
    msg['Subject'] = subject
    body = open('body.txt', 'r').read()
    msg.attach(MIMEText(body))
    
    if attachments:
        for attachment_file in attachments:
            contenttype, encoding = mimetypes.guess_type(attachment_file)
            maintype, subtype = contenttype.split('/', 1)
            try:
                attachment = mimemod_to_use[maintype](open(attachment_file, 'rb')
                                                      .read(),maintype)
            except AttributeError:
                attachment = mimemod_to_use[maintype](open(attachment_file, 'r')
                                                      .read(),maintype)
            attachment.add_header('Content-Disposition', 'attachment', 
                                  filename=attachment_file)
            msg.attach(attachment)

    if action == 'send':
        srv = smtplib.SMTP('mail.oreillyschool.com', 25)
        srv.sendmail(msg['From'], msg['To'], msg.as_string())
        srv.quit()
    else:
        return msg.as_string()
    
if __name__ == "__main__":
    email_msg = e_create(
             'tsikanovski@actrix.co.nz',
#             'tsikanovski@actrix.co.nz',
             'learn@oreillyschool.com',
             'The New Zealand Owl',
             'send',
             ['morepork.html', 'morepork.jpg', 'morepork.mp3']
             )
    print(email_msg)