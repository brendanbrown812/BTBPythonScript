from dotenv import load_dotenv
from Core import *

class Alert:
    def __init__(self, nameOfAlert, dateToSendAlert, alertContent, alertRecipients):
        self.nameOfAlert = nameOfAlert
        self.dateToSendAlert = dateToSendAlert
        self.alertContent = alertContent
        self.alertRecipients = alertRecipients

def getAlerts():
    load_dotenv()
    tableId = os.getenv("ALERTS_PAGE_ID")

    pages = getPages(tableId, "DateToSendAlert")
    alertList = []

    for page in pages:
        nameOfAlert = page['properties']['NameOfAlert']['title'][0]['text']['content']
        dateToSendAlert = page["properties"]["DateToSendAlert"]["date"]["start"]
        alertContent = page['properties']['AlertContent']['rich_text'][0]['text']['content']
        alertRecipients = page['properties']['AlertRecipients']['rich_text'][0]['text']['content']

        alertList.append(Alert(nameOfAlert, dateToSendAlert, alertContent, alertRecipients))
    
    return alertList