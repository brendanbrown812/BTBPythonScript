import os
from dotenv import load_dotenv
from datetime import datetime
from Core import *

class WriteupPage:
    def __init__(self, email, date, name, weekNumber):
        self.email = email
        self.date = date
        self.name = name
        self.weekNumber = weekNumber

def getWriteupPages():
    load_dotenv()
    tableId = os.getenv("WRITEUP_ALERT_ID")

    pages = getPages(tableId)
    pagesList = []

    for page in pages:
        email = page['properties']['Email']['text'][0]['plain_text']
        date = page["properties"]["Date"]["date"]["start"]
        name = page['properties']['Name']['text'][0]['plain_text']
        weekNumber = page['properties']['Week Number']['text'][0]['plain_text']

        pagesList.append(WriteupPage(email, date, name, weekNumber))
    
    return pagesList