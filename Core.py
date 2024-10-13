import os
from dotenv import load_dotenv
import requests
import calendar
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enum import Enum
import json

load_dotenv()

class NotionColumnType(Enum):
    TEXT = "TEXT"
    DATE = "DATE"
    TITLE = "TITLE"
    CHECKBOX = "CHECKBOX"
    NUMBER = "NUMBER"
    SELECT = "SELECT"
    MULTISELECT = "MULTISELECT"

def getNotionColumn(page, columnName, columnType):
    if columnType == NotionColumnType.TEXT:
        return page['properties'][columnName]['rich_text'][0]['text']['content']
    
    if columnType == NotionColumnType.DATE:
        return page["properties"][columnName]["date"]["start"]
    
    if columnType == NotionColumnType.TITLE:
        return page['properties'][columnName]['title'][0]['text']['content']
    
    if columnType == NotionColumnType.CHECKBOX:
        return page["properties"][columnName]["checkbox"]
    
    if columnType == NotionColumnType.NUMBER:
        return page['properties'][columnName]['number']
    
    if columnType == NotionColumnType.SELECT:
        return page['properties'][columnName]['select']['name']
    
    if columnType == NotionColumnType.MULTISELECT:
        email_list = page['properties'][columnName]['multi_select']
        email_addresses = [item['name'] for item in email_list]
        email_string = ','.join(email_addresses)
        return email_string
    
def getHeaders():
    NOTION_TOKEN = os.getenv("NOTION_TOKEN")

    return {
        "Authorization": "Bearer " + NOTION_TOKEN,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    

def getPages(database_id, sortBy = "Date", num_pages = None):
    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    headers = getHeaders()

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
        payload = {"page_size": page_size, "sorts": [{"property": sortBy,"direction": "descending"}], "start_cursor": data["next_cursor"]}
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results

def insertPage(databaseId, dataJson):
    if isTestMode():
        return
    
    url = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": { "database_id": databaseId },
        "properties": dataJson
    }
    data = json.dumps(newPageData)
    headers = getHeaders()
    
    result = requests.request('POST', url, headers=headers, data=data)
    if result.status_code != 200:
        print(f"ERROR writing to DB: {result.status_code}")
        print(result.text)


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