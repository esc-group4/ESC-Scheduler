from twilio.rest import Client
from dotenv import load_dotenv
import os


# TODO : PUT IN LOGGING


# Twilio credentials
account_sid = os.getenv("SMTP_PORT")
auth_token = os.getenv("MSG_SID")
from_whatsapp_number = os.getenv("MSG_NUMBER")  # Twilio sandbox number
to_whatsapp_number = "whatsapp:+6589116194"  # Your phone number

# Initialize Twilio client
client = Client(account_sid, auth_token)


message = client.messages.create(
    to=to_whatsapp_number,
    from_=from_whatsapp_number,
    body="👋This is a reminder to complete your course on www.course.com by 20/03/2025",
)

print(message.sid)
