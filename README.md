# Email Automation Script

A simple Python script to send personalized emails using Gmail’s SMTP server (SSL, port 465).

## What it does

- Logs in with your Gmail and app password  
- Sends emails with custom names, subjects, and messages  
- Waits 2 seconds between emails  
- Handles errors if login or sending fails

## Tech used

- Python 3  
- Built-in libraries: `smtplib`, `email.mime.text`, `time`  
- No extra installs needed

## How to use

1. Add your Gmail and app password in the `sender` and `password` fields  
2. Edit the recipients, subjects, and messages lists  
3. Run the file:

```bash
python automatemail.py
