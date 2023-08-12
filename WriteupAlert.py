from Core import *
from WriteupPage import *
from datetime import datetime

def RunWriteupAlert():
    writeupPages = getWriteupPages()

    for writeup in writeupPages:
        writeupDate = datetime.strptime(writeup.date, "%Y-%m-%d")
        currentDate = datetime.now()
        daysUntilWriteup = (currentDate - writeupDate).days * -1

        email = ""
        subject = ""
        body = ""
        sendItDaddy = False

        if daysUntilWriteup == 1:
            sendItDaddy = True
            email = writeup.email
            subject = "Writeup Alert: One Day"
            body = "Your writeup is due in 1 day"
        
        if daysUntilWriteup == 7:
            sendItDaddy = True
            email = writeup.email
            subject = "Writeup Alert: One Week"
            body = "Your writeup is due in one week"

        if daysUntilWriteup == 14:
            sendItDaddy = True
            email = writeup.email
            subject = "Writeup Alert: Two Weeks"
            body = "Your writeup is due in two weeks"

        if sendItDaddy:
            sendEmail(email, subject, body)
            print(f"Email sent to {writeup.email}\n\n")