from Core import *
import os
from dotenv import load_dotenv

class Alert:
    # Define the fields and their notion column types
    FIELDS = {
        "NameOfAlert": NotionColumnType.TITLE,
        "DateToSendAlert": NotionColumnType.DATE,
        "AlertContent": NotionColumnType.TEXT,
        "AlertRecipients": NotionColumnType.TEXT
    }

    def __init__(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)

def getAlerts():
    load_dotenv()
    tableId = os.getenv("ALERTS_PAGE_ID")
    pages = getPages(tableId, "DateToSendAlert")
    alertList = []

    for page in pages:
        # Dynamically fetch each field
        fields_data = {field: getNotionColumn(page, field, column_type) 
                       for field, column_type in Alert.FIELDS.items()}

        alertList.append(Alert(**fields_data))
    
    return alertList
