import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to: str, subject: str, body: str):

    sender_email = "hegdenishanth17@gmail.com"
    sender_password = "ojnu voxk hqyh ueyf"

    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, to, msg.as_string())
        server.quit()

        return {
            "status": "success",
            "message": f"Email sent to {to}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }