
import smtplib  # python built-in library for sending emails.
import time  # for delay between emails
from email.mime.text import MIMEText  # formats plain-text message into email format message

# sender email and app password 
sender = "abdulrahmanghourabi201@gmail.com"
password = "avbe rpeq gqxs fews" 
# example receiver
receiver = "Claudeo02@gmail.com"  

# list of recipients with email and name
recipients = [
    {"email": "a@gmail.com", "name": "Alice"},
    {"email": "b@gmail.com", "name": "Bob"},
]

# subjects for each email
subjects = [
    "Daily Operations Summary",
    "Reminder: Scheduled Meeting on October 4, 2025 at 10AM",
]

# messages for each email
messages = [
    "Managed daily operations to ensure smooth workflow and system uptime.",
    "Scheduled and coordinated team activities for the October 4, 2025, 10AM meeting.",
]


def send_emails():
    try:
        # connect securely to Gmail SMTP server using SSL on port 465(we can use 587 but it isn't encrypted at start)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)  # login with sender email and app password
            print("Logged in successfully.")

            # send email to each recipient with corresponding subject and message
            for r, subject, msg_text in zip(recipients, subjects, messages):
                # personalize message body
                body = f"Hello {r['name']},\n\n{msg_text}"

                # format message as email
                msg = MIMEText(body)
                msg['Subject'] = subject
                msg['From'] = sender
                msg['To'] = r["email"]

                time.sleep(2)  # delay between emails to avoid spam detection

                try:
                    server.sendmail(sender, r["email"], msg.as_string())  # send email
                    print(f"Email sent to {r['name']} ({r['email']})")
                except Exception as e:
                    print(f"Failed to send email to {r['email']}: {e}")

    except Exception as e:
        print(f"Failed to login or connect to SMTP server: {e}")


if __name__ == "__main__":
    send_emails()
       
         

   
