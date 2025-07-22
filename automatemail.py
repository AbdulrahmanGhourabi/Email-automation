
import smtplib # python built-in library for sending emails.
import time # for delay 
from email.mime.text import MIMEText #email.mime.text is a module , MIMEText is a class inside this module to format plain-text message into an email format message.

sender = "abdulrahmanghourabi201@gmail.com"
password = "avbe rpeq gqxs fews" # app password for my account to be more secure in case  this code gets exposed.

receiver = "Claudeo02@gmail.com"

recipients=[
     {"email":"a@gmail.com", "name":"Alice"},
     {"email":"b@gmail.com" , "name":"Bob"},
]

subjects = [
    "Daily Operations Summary",
    "Reminder: Scheduled Meeting on October 4, 2025 at 10AM",
]



messages = [
    "Managed daily operations to ensure smooth workflow and system uptime.",
    "Scheduled and coordinated team activities for the October 4, 2025, 10AM meeting.",
]  
    
       
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: # SMTP protocol for sending email. we use 465 port for SSL(secure from start because encrypted ) , and 587 for STARTTLS(start unencrypted,then upgrade to secure)
    server.login(sender, password)
    for r, subject, msg in zip (recipients,subjects,messages) :
       
       body= f"Hello {r['name']} ,\n\n {msg} "
       msg = MIMEText(body) # what's the body
       msg['Subject']= subject # what's the subject
       msg['From']= sender # who's the sender
       msg['To']= r["email"] # who's the receiver 
       time.sleep(2)
       server.sendmail(sender,r["email"], msg.as_string()) # sending the email.
       
         

   