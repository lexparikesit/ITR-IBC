from email.mime.text import MIMEText
import smtplib

class emailService:

    def __init__(self):
        self.sender = "email"
        self.password = "password"

    def send_email(self, to_email, subject, body):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["Form"] = self.sender
        msg["To"] = to_email

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.sendmail(self.sender, to_email, msg.as_string())
        
        except Exception as e:
            print(f"[EMAIL ERROR] {e}")