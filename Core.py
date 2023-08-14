import os
from dotenv import load_dotenv
import requests
import calendar
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

def getPages(database_id, sortBy, num_pages = None):
    NOTION_TOKEN = os.getenv("NOTION_TOKEN")

    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    headers = {
        "Authorization": "Bearer " + NOTION_TOKEN,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {
        "page_size": page_size,
        "sorts": [
            {
                "property": sortBy,
                "direction": "descending"
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    results = data["results"]

    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results

def isTestMode():
    return os.getenv("TEST_MODE").lower() == "true"

def sendEmail(recipientEmail, subject, body):
    if os.getenv("SEND_EMAILS").lower() == "true":
        senderEmail = os.getenv("GMAIL_SENDER_EMAIL")
        gmailAppPassword = os.getenv("GMAIL_APP_PASSWORD")
        smtpServer = "smtp.gmail.com" 
        smtpPort = 587

        msg = MIMEMultipart()
        msg['From'] = senderEmail
        msg['To'] = recipientEmail
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtpServer, smtpPort) as server:
            server.starttls()
            server.login(senderEmail, gmailAppPassword)
            server.sendmail(senderEmail, recipientEmail, msg.as_string())