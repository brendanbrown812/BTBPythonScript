from Tasks.GetSleeperUsers import *
from Tasks.GetNflPlayers import *
from Tasks.GetUserRosters import *

def GetSleeper():
    GetSleeperUserData(False)
    GetUserRosterData(False)
    GetNFLPlayersData(False)