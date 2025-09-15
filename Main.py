from Tasks.WriteupAlertTask import *
from Tasks.SendAlertsTask import *
from Tasks.GetSleeper import *
from Tasks.GetGameHistory import *
from Tasks.AddLastWeeksGame import *
from Tasks.SQL import *
from Tasks.ForceAddWeekToNotion import *

RunWriteupAlert()
RunGeneralAlerts()
AddLastWeeksGame()
#GetAllGameHistory()
#GetSleeper()
#GetWeeklySQL(2)
#ForceAddWeekToNotion(1)