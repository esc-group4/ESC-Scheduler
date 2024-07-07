import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# TODO : PUT IN LOGGING


load_dotenv()


def send_email():
    smtp_server = os.getenv(
        "SMTP_SERVER"
    )  # SES SMTP endpoint for Asia Pacific (Singapore)
    smtp_port = os.getenv("SMTP_PORT")
    username = os.getenv("SMTP_USER")  # Replace with your SES SMTP username
    password = os.getenv("SMTP_PASS")  # Replace with your SES SMTP password
    from_email = os.getenv("EMAIL_SENDER")  # Must be verified in SES
    to_email = "xiaoyang_ho@mymail.sutd.edu.sg"  # 2nd verified email

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = "Hello from Python SES SMTP"

    body = "This is an email sent from Python using Amazon SES SMTP in the Asia Pacific (Singapore) region."
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print("Email sent successfully to the SES simulator")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()


if __name__ == "__main__":
    send_email()
