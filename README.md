# ESC-Scheduler

**SMTP client** (with AWS SES for testing because it is a free option)
1. Create an SES account
2. (include domain in the future for mass email sending to a particular domain)
3. edit smtp_aws_client.py with smtp credentials and verified testing emails
4. pip install boto3, botocore, smtp, email
5. run python smtp_aws_client.py

**Whatsapp twilio client** (scrapped for now)
To use: 
1. Create an account on twilio, replace script's account sid and auth token with personal account, modify phone numbers
2. run python twilio_client.py
