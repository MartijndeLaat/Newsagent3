import os
import requests

def send_email(token, content, recipient):
    """Send an email via Microsoft Graph API."""
    url = "https://graph.microsoft.com/v1.0/me/sendMail"
    email = {
        "message": {
            "subject": "Weekly Client Insights",
            "body": {"contentType": "Text", "content": content},
            "toRecipients": [{"emailAddress": {"address": recipient}}]
        }
    }
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=email)
    return response.status_code, response.text
