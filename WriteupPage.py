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
    tableId = os.getenv("WRITEUP_ALERT_ID")

    pages = getPages(tableId)
    pagesList = []

    for page in pages:
        email = page['properties']['Email']['rich_text'][0]['text']['content']
        date = page["properties"]["Date"]["date"]["start"]
        name = page['properties']['Name']['title'][0]['text']['content']
        weekNumber = page['properties']['Week Number']['rich_text'][0]['text']['content']
        completed = page['properties']['Completed']['rich_text'][0]['text']['content']

        pagesList.append(WriteupPage(email, date, name, weekNumber, completed))
    
    return pagesList