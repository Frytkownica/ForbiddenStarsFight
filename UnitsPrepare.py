from UnitClass import Unit
from typing import List
def selectUnits(factionList: List[int], unitList: List[Unit]):
    player1Units = [unit for unit in unitList if unit.faction == factionList[0]]
    player2Units = [unit for unit in unitList if unit.faction == factionList[1]]
    return player1Units, player2Units