import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    smtp_server = 'email-smtp.ap-southeast-1.amazonaws.com'  # SES SMTP endpoint for Asia Pacific (Singapore)
    smtp_port = 587
    username = 'AKIAWN5LEG7IWZCYK5PN'  # Replace with your SES SMTP username
    password = 'BDZJAVVdDfkqGb5YUfgF16kCNNxSQao/NzbqseZF31Rv'  # Replace with your SES SMTP password
    from_email = 'hoxiaoyang321@gmail.com'  # Must be verified in SES
    to_email = 'xiaoyang_ho@mymail.sutd.edu.sg'  # 2nd verified email

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Hello from Python SES SMTP'

    body = 'This is an email sent from Python using Amazon SES SMTP in the Asia Pacific (Singapore) region.'
    msg.attach(MIMEText(body, 'plain'))

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
