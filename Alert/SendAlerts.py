from Core import *
from Alert.AlertPage import *
from datetime import datetime

def RunGeneralAlerts():
    alerts = getAlerts()

    for alert in alerts:
        dateToSendAlert = datetime.strptime(alert.DateToSendAlert, "%Y-%m-%d")
        currentDate = datetime.now()
        
        if dateToSendAlert.date() == currentDate.date():
            subject = "New BTB Alert"
            body = alert.AlertContent

            if alert.AlertRecipients.lower() == "all":
                alert.AlertRecipients = os.getenv("ALL_LEAGUE_EMAILS")

            email_list = alert.AlertRecipients.split(',')
            for email in email_list:
                sendEmail(email, subject, body)
                print(f"Sent an email to {email} saying {body}")
                