import random
from Lib.UnitsPrepare import *
from Lib.PlayerClass import PlayerInfo
from Lib.MainGame import playTheGame


# Example usage
# SM,  # Orc
factionList = [0,1]
# Example list with 28 elements
unlockedcardList = [True, True, True, True, True, False, False, False, False, False, False, False, False, False,
                    True, True, True, True, True, False, False, False, False, False, False, False, False, False]
unitList = [Unit(1, 0, False, False),
            Unit(1, 0, False, False),
            Unit(0, 0, False, False),
            Unit(0, 0, False, False),
            ]

playerInfo = PlayerInfo(factionList, unlockedcardList, unitList)

playTheGame(playerInfo)