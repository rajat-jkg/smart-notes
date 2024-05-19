import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def mailTo(toEmail, title,text):
    try:
        print(f'Request To email {title}')
        server = smtplib.SMTP('smtp.hostinger.com',587)
        print('SMTP server started')
        server.starttls()
        print('tls connections started')
        server.login('emailer@rajat-gupta.in', os.environ['MAILPASS'])
        print('login successful')
        message = MIMEMultipart('alternative')
        message['From'] = 'Smart Notes <emailer@rajat-gupta.in>'
        message['Subject'] = title
        message['To'] = toEmail
        message['Cc'] = None
        message['Bcc'] = None
        print('message generated')
        HTMLmessageText = f'''
<div style="border: solid 2px; padding: 5px;">
<h3>Hello! Here's your note to remember</h3>
<h4>{title}</h4>
<pre>{text}</pre>
<div style="height:20px"></div>
</div>
<div style="background-color: #070707; color:#F5F5F5; text-align:center; padding:5px;">
<p>This email was sent to you from <b>Smart Notes</b></p>
</div>
'''
        meassageObject = MIMEText(HTMLmessageText,'html')
        message.attach(meassageObject)
        print('message attached')

        server.sendmail(from_addr='emailer@rajat-gupta.in', to_addrs=toEmail,msg=message.as_string())
        print('message sent')
        
        server.close()
        return True
    except Exception as E:
        print(E)
        return False