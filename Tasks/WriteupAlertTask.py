from Core import *
from Pages.WriteupPage import *
from Tasks.GetSleeperMatchup import *
from Tasks.GetSleeper import *
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
            historicalMatchupData = GetSleeper(writeup.WeekNumber)
            subject = f"BTB Week {writeup.WeekNumber} Historical Data"
            body = historicalMatchupData
            for memberEmail in os.getenv("ALL_LEAGUE_EMAILS").split(','):
                if memberEmail != writeup.Email:
                    sendEmail(memberEmail, subject, body)
                    print(f"\nEmail sent to {memberEmail}\nIt would have said:\n{body}\n\nWith a subject of:\n{subject}\n\n\n\n")
            sendItDaddy = True
            email = writeup.Email
            subject = "BTB PTGOTW Writeup 1 Day reminder"
            body = f"{writeup.Name},\nThis is your third reminder that your writeup of week {writeup.WeekNumber} is due on {writeup.Date}. You have only 1 day to send it."
            body += f"\n\nHistorical Data for Your Week's Matchups:\n"
            body += historicalMatchupData
            
        
        if daysUntilWriteup == 7:
            sendItDaddy = True
            email = writeup.Email
            subject = "BTB PTGOTW Writeup 1 week reminder"
            body = f"{writeup.Name},\nThis is your second reminder that your writeup of week {writeup.WeekNumber} is due on {writeup.Date}. You have a week day to send it."
            body += f"\n\nHistorical Data for Your Week's Matchups:\n"
            body += f"{GetSleeper(writeup.WeekNumber)}"

        if daysUntilWriteup == 14:
            sendItDaddy = True
            email = writeup.Email
            subject = "BTB PTGOTW Writeup 2 week reminder"
            body = f"{writeup.Name},\nThis is your first reminder that your writeup of week {writeup.WeekNumber} is due on {writeup.Date}. You have 2 weeks to send it."
            body += f"\n\nHistorical Data for Your Week's Matchups:\n"
            body += f"{GetSleeper(writeup.WeekNumber)}"

        if sendItDaddy and not writeup.Completed:
            sendEmail(email, subject, body)
            if os.getenv("TEST_MODE").lower() == "true":
                print(f"\nEmail sent to {writeup.Email}\nIt would have said:\n{body}\n\nWith a subject of:\n{subject}\n")