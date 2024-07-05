from twilio.rest import Client

# Twilio credentials
account_sid = 'AC848574a9766acd229ffa61d04d64ef6b'
auth_token = '751f33e99f02bf67cb054d0f9c62abb8'
from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox number
to_whatsapp_number = 'whatsapp:+6589116194'    # Your phone number

# Initialize Twilio client
client = Client(account_sid, auth_token)


message =client.messages.create(
    to=to_whatsapp_number,
    from_=from_whatsapp_number,
    body='👋This is a reminder to complete your course on www.course.com by 20/03/2025'
)

print(message.sid)
