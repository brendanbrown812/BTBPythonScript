from Core import *
from PTGOTW.WriteupPage import *
from datetime import datetime

def RunWriteupAlert():
    writeupPages = getWriteupPages()

    for writeup in writeupPages:
        writeupDate = datetime.strptime(writeup.Date, "%Y-%m-%d")
        currentDate = datetime.now()
        daysUntilWriteup = (currentDate - writeupDate).days * -1

        email = ""
        subject = ""
        body = ""
        sendItDaddy = False

        if daysUntilWriteup == 1:
            sendItDaddy = True
            email = writeup.Email
            subject = "BTB PTGOTW Writeup 1 Day reminder"
            body = f"{writeup.Name}\nThis is your third reminder that your writeup of week {writeup.WeekNumber} is due on {writeup.Date}. You have only 1 day to send it."
        
        if daysUntilWriteup == 7:
            sendItDaddy = True
            email = writeup.Email
            subject = "BTB PTGOTW Writeup 1 week reminder"
            body = f"{writeup.Name}\nThis is your second reminder that your writeup of week {writeup.WeekNumber} is due on {writeup.Date}. You have a week day to send it."

        if daysUntilWriteup == 14:
            sendItDaddy = True
            email = writeup.Email
            subject = "BTB PTGOTW Writeup 2 week reminder"
            body = f"{writeup.Name}\nThis is your first reminder that your writeup of week {writeup.WeekNumber} is due on {writeup.Date}. You have 2 weeks to send it."

        if sendItDaddy and writeup.Completed.lower() != "true":
            sendEmail(email, subject, body)
            if os.getenv("TEST_MODE").lower() == "true":
                print(f"Email sent to {writeup.Email}\n\nIt would have said:\n{body}\n\nWith a subject of:\n{subject}")