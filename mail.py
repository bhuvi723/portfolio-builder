import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv("SENDER_MAIL")
pw = os.getenv("PASS_WORD")
subject = "Regarding the query you sent through my portfolio!"

def send_email(name,email,message):
    body = f'''Thank you for the query. Here is the copy of your response. We'll reach back to you in 24 hours.
    
    Name : {name}
    
    Email : {email}
    
    Message : {message} 
    '''
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = my_email
    msg['To'] = email
    
    try :  
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
            smtp_server.login(my_email,pw)
            smtp_server.sendmail(my_email,email,msg.as_string())    
        return "Message Sent!"
    except Exception as e:
        return str(e)