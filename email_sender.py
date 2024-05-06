import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipients, subject, message):
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender_email, sender_password)

        for recipient in recipients:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            smtp_server.sendmail(sender_email, recipient, msg.as_string())

        smtp_server.quit()
        print("Email(s) sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    sender_email = "sender_email@gmail.com"  
    sender_password = "your_password"  
    recipients = ["targetemail1@gmail.com", "targetemail2@gmail.com"] 
    subject = "Test Email"
    message = "This is a test email sent using Python. This script is using for loop to send the same email to everyone"

    send_email(sender_email, sender_password, recipients, subject, message)
