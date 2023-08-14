from Core import *
from WriteupPage import *
from datetime import datetime

def RunGeneralAlerts():
    alerts = getAlerts()

    for alert in alerts:
        dateToSendAlert = datetime.strptime(alert.dateToSendAlert, "%Y-%m-%d")
        currentDate = datetime.now()
        daysUntilAlertIsSent = (currentDate - dateToSendAlert).days * -1

        #If daysUntilAlertIsSent == 0, send email to alertRecipients

        subject = "New BTB Alert"
        body = alert.alertContent

        email_list = alert.alertRecipients.split(',')
        for email in email_list:
            #print(f"I would have sent an email to {email} saying {body}")
            sendEmail(email, subject, body)

        

class Alert:
    def __init__(self, nameOfAlert, dateToSendAlert, alertContent, alertRecipients):
        self.nameOfAlert = nameOfAlert
        self.dateToSendAlert = dateToSendAlert
        self.alertContent = alertContent
        self.alertRecipients = alertRecipients

def getAlerts():
    load_dotenv()
    tableId = os.getenv("GENERAL_ALERT_ID")

    pages = getAllAlerts(tableId)
    alertList = []

    for page in pages:
        nameOfAlert = page['properties']['NameOfAlert']['title'][0]['text']['content']
        dateToSendAlert = page["properties"]["DateToSendAlert"]["date"]["start"]
        alertContent = page['properties']['AlertContent']['rich_text'][0]['text']['content']
        alertRecipients = page['properties']['AlertRecipients']['rich_text'][0]['text']['content']

        alertList.append(Alert(nameOfAlert, dateToSendAlert, alertContent, alertRecipients))
    
    return alertList