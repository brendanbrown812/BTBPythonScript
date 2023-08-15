import os
from dotenv import load_dotenv
from datetime import datetime
from Core import *

class WriteupPage:
    def __init__(self, email, date, name, weekNumber, completed):
        self.email = email
        self.date = date
        self.name = name
        self.weekNumber = weekNumber
        self.completed = completed

def getWriteupPages():
    load_dotenv()
    tableId = os.getenv("PTGOTW_REMINDERS_PAGE_ID")

    pages = getPages(tableId, "Date")
    pagesList = []

    for page in pages:
        email = getNotionColumn(page, "Email", NotionColumnType.TEXT)
        date = getNotionColumn(page, "Date", NotionColumnType.DATE)
        name = getNotionColumn(page, "Name", NotionColumnType.TITLE)
        weekNumber = getNotionColumn(page, "Week Number", NotionColumnType.TEXT)
        completed = getNotionColumn(page, "Completed", NotionColumnType.TEXT)

        pagesList.append(WriteupPage(email, date, name, weekNumber, completed))
    
    return pagesList