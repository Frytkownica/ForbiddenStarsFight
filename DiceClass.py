import random
from UnitsPrepare import Unit
from typing import List
def selectDice(player1UnitList:List[Unit], player2UnitList:List[Unit]):
    def selectDiceOnePlayer(playerUnit):
        def sumDice(unitList):
            sumOfDice = [unit.dice for unit in unitList]
            return sum(sumOfDice)
        playerDice = rollNdice(sumDice(playerUnit))
        return playerDice
    player1Dice = selectDiceOnePlayer(player1UnitList)
    player2Dice = selectDiceOnePlayer(player2UnitList)
    player1Dice.sort(key=sortDie)
    player2Dice.sort(key=sortDie)
    return player1Dice,player2Dice

def addRandomDie(playerDice:List[str], amount:int = 1):
    for _ in range(amount):
        if playerDice.count()<8:
            playerDice.append(rollDice())
    playerDice.sort(key=sortDie)

def reRollDie(playerDice:List[str], whatDie:str, amount:int = 1):
    for _ in range(amount):
            if whatDie in playerDice:
                playerDice.remove(whatDie)
                playerDice.append(rollDice())
    playerDice.sort(key=sortDie)

def rollNdice(diceAmount:int):
    rolledDice = []
    for _ in range(diceAmount):
        rolledDice.append(rollDice())
    return rolledDice

def rollDice():
    rand_num = random.randint(1, 1000)
    if 1 <= rand_num <= 500:
        return 'Bolter'
    elif 500 < rand_num <= 833:
        return 'Shield'

    else:
        return 'Morale'

def sortDie(list:any):
    return {'Bolter':1, 'Shield':2, 'Morale':3}[list]