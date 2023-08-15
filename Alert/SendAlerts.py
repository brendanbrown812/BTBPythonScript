from Core import *
from Alert.AlertPage import *
from datetime import datetime

def RunGeneralAlerts():
    alerts = getAlerts()

    for alert in alerts:
        dateToSendAlert = datetime.strptime(alert.dateToSendAlert, "%Y-%m-%d")
        currentDate = datetime.now()
        
        if dateToSendAlert.date() == currentDate.date():
            subject = "New BTB Alert"
            body = alert.alertContent

            if alert.alertRecipients.lower() == "all":
                alert.alertRecipients = os.getenv("ALL_LEAGUE_EMAILS")

            email_list = alert.alertRecipients.split(',')
            for email in email_list:
                sendEmail(email, subject, body)
                print(f"Sent an email to {email} saying {body}")
                