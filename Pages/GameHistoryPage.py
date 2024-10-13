from Core import *
from Pages.WriteupPage import *
from datetime import datetime

class Game:
    FIELDS = {
        "Year": NotionColumnType.NUMBER,
        "Week": NotionColumnType.TITLE,
        "Team1Name": NotionColumnType.TEXT,
        "Team1Score": NotionColumnType.NUMBER,
        "Team2Name": NotionColumnType.TEXT,
        "Team2Score": NotionColumnType.NUMBER,
        "Winner": NotionColumnType.TEXT,
        "WasPTGOTW": NotionColumnType.CHECKBOX
    }

    def __init__(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)

def getGames():
    tableId = getTableId()
    pages = getPages(tableId, "Year")
    gameList = []

    for page in pages:
        fields_data = {field: getNotionColumn(page, field, column_type)
                        for field, column_type in Game.FIELDS.items()}
        
        gameList.append(Game(**fields_data))

    return gameList

def getTableId():
    load_dotenv()
    return os.getenv("GAME_HISTORY_PAGE_ID")