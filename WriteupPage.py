import os
from dotenv import load_dotenv
from datetime import datetime
from Core import *

class WriteupPage:
    def __init__(self, email, writeupDate):
        self.email = email
        self.writeupDate = writeupDate

def getWriteupPages():
    load_dotenv()
    tableId = os.getenv("WRITEUP_ALERT_ID")

    pages = getPages(tableId)
    pagesList = []

    for page in pages:
        email = page['properties']['Email']['text'][0]['plain_text']
        writeupDate = page["properties"]["WriteupDate"]["date"]["start"]

        pagesList.append(WriteupPage(email, writeupDate))
    
    return pagesList