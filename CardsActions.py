import random
from PlayerClass import Player
from DiceClass import *
from typing import List
from InformationHandling import displayInfo


def cardAction(gameRound: int, activePlayer: Player, enemy: Player, cardNumber: int):
    match activePlayer.faction:
        case 0:
            match cardNumber:
                # Reconnaissance
                case 0:
                    enemy.turnCard()
                    if (chooseTokens(gameRound, activePlayer, enemy, 2, 2) == 1):
                        activePlayer.bolterTokens += 2
                    else:
                        activePlayer.shieldTokens += 2
                # Faith in the Emperor
                case 1:
                    activePlayer.addRandomDie()
                # Ambush
                case 2:
                    activePlayer.bolterTokens += 2
                # Fury of the Ultramar
                case 3:
                    enemy.reRollDie('Shield')
                    enemy.recount()
                    if (chooseReroll(gameRound, activePlayer, enemy, 'Shield') == 1):
                        activePlayer.reRollDie('Shield')
                # Blessed Power armour
                case 4:
                    activePlayer.shieldTokens += 2
                # Hold the line
                case 5:
                    activePlayer.shieldTokens += 2
                    #toDo Check who is who in this situation, add rally
                # Glory and death
                case 6:
                    activePlayer.bolterTokens += 2
                    #toDo Check who is who in this situation, add rally
                # Veteran scouts
                case 7:
                    for _ in activePlayer.dice.count('Morale'):
                        activePlayer.recount()
                        if (chooseTokens(gameRound, activePlayer, enemy, 1, 1) == 1):
                            activePlayer.bolterTokens += 1
                        else:
                            activePlayer.shieldTokens += 1
                # Drop Pod assault
                case 8:
                    activePlayer.addRandomDie()
                # Show no fear
                case 9:
                    #toDo Add blocking routing in player parameters
                    pass
                # Break the line
                case 10:
                    amount = activePlayer.dice.count('Morale')
                    for _ in range(amount):
                        activePlayer.recount()()
                        if (chooseSpend(gameRound, activePlayer, enemy, 'Morale') == 1):
                            chooseGainDie(activePlayer, 1, 1)
                        else:
                            break
                # Armoured advance
                case 11:
                    activePlayer.addRandomDie()
                # Emperor's glory
                case 12:
                    activePlayer.addRandomDie(2)
                # Emperor's might
                case 13:
                    activePlayer.addRandomDie(2)
        case 1:
            match cardNumber:
                # Slugga Boyz
                case 0:
                    activePlayer.reRollDie('Morale', activePlayer.dice.count('Morale'))
                    enemy.reRollDie('Morale', enemy.dice.count('Morale'))
                # Shoota Boyz
                case 1:
                    activePlayer.reRollDie('Shield', activePlayer.dice.count('Shield'))
                # 'Ard Boyz
                case 2:
                    activePlayer.reRollDie('Bolter', activePlayer.dice.count('Bolter'))
                # Gretchin
                case 3:
                    activePlayer.shieldTokens += 1
                    activePlayer.bolterTokens += 1
                    chooseEnemyReroll(gameRound, activePlayer, enemy)
                # Mek Boyz
                case 4:
                    activePlayer.addRandomDie()
                # Biker Nobz
                case 5:
                    enemy.reRollDie('Bolter', enemy.dice.count('Bolter'))
                # Sea of green
                case 6:
                    activePlayer.addReinforce()
                # Waaagh!!!!
                case 7:
                    chooseRally(gameRound, activePlayer, enemy)
                # Mega Nobz
                case 8:
                    enemy.reRollDie('Shield', enemy.dice.count('Shield'))
                # Rokkit wagon
                case 9:
                    pass
                # Weirdboyz
                case 10:
                    activePlayer.reRollAllDie()
                    enemy.reRollAllDie()
                # Party wagon
                case 11:
                    activePlayer.addReinforce()
                # Snapper Gargant
                case 12:
                    pass
                # Smasher Gargant
                case 13:
                    pass



def chooseTokens(gameRound, player, enemy, bolterTokens, shieldTokens):
    displayInfo(gameRound, player, enemy)
    while True:
        try:
            selectedToken = int(input(f"Choose between {bolterTokens} bolterT and {shieldTokens} shitelT: "))
            if 0 <= selectedToken < 2:
                break
            else:
                print("Number out of range. Please try again.")
        except ValueError:
            print(f"Invalid input. Choose between {bolterTokens} and {shieldTokens}:  ")
    return selectedToken

def chooseReroll(gameRound:int, player:Player, enemy:Player, whatDie:str):
    displayInfo(gameRound, player, enemy)
    while True:
        try:
            rerollChoice = int(input(f"Do you reroll {whatDie} or Not: "))
            if 0 <= rerollChoice < 2:
                break
            else:
                print("Number out of range. Please try again.")
        except ValueError:
            print(f"Invalid input. Do you reroll {whatDie} or Not:  ")
    return rerollChoice

def chooseEnemyReroll(gameRound:int, player:Player, enemy:Player):
    displayInfo(gameRound, player, enemy)
    while True:
        try:
            rerollChoice = int(input("What enemy die reroll: Bolter, Shield or Morale?"))
            if 0 <= rerollChoice < 3:
                break
            else:
                print("Number out of range. Please try again.")
        except ValueError:
            print(f"Invalid input. What enemy die reroll: Bolter, Shield or Morale?")
    enemy.reRollDie(dieNumberToName(rerollChoice))

def chooseRally(gameRound:int, player:Player, enemy:Player):
    routedUnitList = [routedUnit for routedUnit in player.unitList if routedUnit.routed]
    if len(routedUnitList) > 1:
        routedUnitCommandLevel = list(set(singleUnit.cl for singleUnit in routedUnitList))
        routedUnitString = ", ".join(str(singleUnit) for singleUnit in routedUnitCommandLevel)
        displayInfo(gameRound, player, enemy)
        while True:
            try:
                unitToRally = int(input(f"What unit to rally: {routedUnitString}"))
                if 0 <= unitToRally < len(routedUnitCommandLevel)-1:
                    break
                else:
                    print("Number out of range. Please try again.")
            except ValueError:
                print(f"Invalid input. What unit to rally: {routedUnitString}?")
        for singleUnit in player.unitList:
            if singleUnit.cl == routedUnitCommandLevel[unitToRally-1]:
                singleUnit.routed = False
                break
    elif len(routedUnitList) == 1:
        for singleUnit in player.unitList:
            if singleUnit.cl == routedUnitList[0].cl:
                singleUnit.routed = False
                break

def chooseSpend():
    pass
    #ToDo chooses if loose something or not

def chooseGainDie(player, bolterDies:int = 0, shieldDies:int = 0, moraleDies:int = 0):
    pass
    #ToDo let player choose what die to gain