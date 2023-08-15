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
        nameOfAlert = getNotionColumn(page, "NameOfAlert", NotionColumnType.TITLE)
        dateToSendAlert = getNotionColumn(page, "DateToSendAlert", NotionColumnType.DATE)
        alertContent = getNotionColumn(page, "AlertContent", NotionColumnType.TEXT)
        alertRecipients = getNotionColumn(page, "AlertRecipients", NotionColumnType.TEXT)

        alertList.append(Alert(nameOfAlert, dateToSendAlert, alertContent, alertRecipients))
    
    return alertList