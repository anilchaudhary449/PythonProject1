# email_utils.py

import smtplib
from email.message import EmailMessage
import os

def send_email_on_failure(subject, body, to_email, attachment_path=None):
    # Email config
    from_email = "lenix.jacori@dsitip.com"
    from_password = "pubxz4J@"  # Use App Password if 2FA is enabled

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)

    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, 'rb') as file:
            file_data = file.read()
            file_name = os.path.basename(attachment_path)
            msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_email, from_password)
            smtp.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
