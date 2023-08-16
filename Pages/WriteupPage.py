from Core import *
import os
from dotenv import load_dotenv

class WriteupPage:
    # Define the fields and their notion column types
    FIELDS = {
        "Email": NotionColumnType.SELECT,
        "Date": NotionColumnType.DATE,
        "Name": NotionColumnType.TITLE,
        "WeekNumber": NotionColumnType.TEXT,
        "Completed": NotionColumnType.CHECKBOX
    }

    def __init__(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)

def getWriteupPages():
    load_dotenv()
    tableId = os.getenv("PTGOTW_REMINDERS_PAGE_ID")
    pages = getPages(tableId, "Date")
    pagesList = []

    for page in pages:
        # Dynamically fetch each field
        fields_data = {field: getNotionColumn(page, field.replace('_', ' '), column_type) 
                       for field, column_type in WriteupPage.FIELDS.items()}

        pagesList.append(WriteupPage(**fields_data))
    
    return pagesList
