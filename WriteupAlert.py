from Core import *
from WriteupPage import *
from datetime import datetime

def RunWriteupAlert():
    writeupPages = getWriteupPages()

    for writeup in writeupPages:
        writeupDate = datetime.strptime(writeup.date, "%Y-%m-%d")
        currentDate = datetime.strptime(datetime.now(), "%Y-%m-%d")
        daysUntilWriteup = (currentDate - writeup)

        email = ""
        subject = ""


        if daysUntilWriteup < 0:
            continue

        if daysUntilWriteup == 1:
            email = writeup.email
            subject = "Writeup Alert: One Day"
            body = "Your writeup is due in 1 day"
        
        if daysUntilWriteup == 7:
            email = writeup.email
            subject = "Writeup Alert: One Week"
            body = "Your writeup is due in one week"

        if daysUntilWriteup == 14:
            email = writeup.email
            subject = "Writeup Alert: Two Weeks"
            body = "Your writeup is due in two weeks"

        sendEmail(email, subject, body)