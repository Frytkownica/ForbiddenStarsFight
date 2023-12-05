import random
from PlayerClass import Player
from DiceClass import *
from typing import List
from MainGame import displayInfo

def selectCards(unlockedcardList: List[bool]):
    if len(unlockedcardList) != 28:
        raise ValueError("unlockedcardList must have 28 elements.")

    def selectRange(startIndex: int):
        return [unlockedcardList[element] for element in range(startIndex, startIndex + 14)]

    def selectPlayerCards(rangedList: List[int]):
        availableTypes = [cardNumber for cardNumber in range(14) if rangedList[cardNumber]]
        # Making doublets
        selectionPool = [cardNumber for cardNumber in availableTypes for _ in range(2)]
        # Shuffle Deck
        random.shuffle(selectionPool)
        selectedCards = selectionPool[0:5]
        remainingCards = selectionPool[5:10]
        return selectedCards, remainingCards

    player1Cards = selectPlayerCards(selectRange(0))
    player2Cards = selectPlayerCards(selectRange(14))

    return player1Cards, player2Cards


def cardParameters(faction: int, cardNumber: int):
    mapping = {
        0: {
            # Reconnaissance
            0: {'Bolter': 0, 'Shield': 1, 'Morale': 0},
            # Faith in the Emperor
            1: {'Bolter': 0, 'Shield': 0, 'Morale': 1},
            # Ambush
            2: {'Bolter': 1, 'Shield': 0, 'Morale': 0},
            # Fury of the Ultramar
            3: {'Bolter': 1, 'Shield': 0, 'Morale': 0},
            # Blessed Power armour
            4: {'Bolter': 0, 'Shield': 1, 'Morale': 0},
            # Hold the line
            5: {'Bolter': 0, 'Shield': 1, 'Morale': 1},
            # Glory and death
            6: {'Bolter': 1, 'Shield': 0, 'Morale': 1},
            # Veteran scouts
            7: {'Bolter': 1, 'Shield': 1, 'Morale': 1},
            # Drop Pod assault
            8: {'Bolter': 1, 'Shield': 1, 'Morale': 0},
            # Show no fear
            9: {'Bolter': 0, 'Shield': 2, 'Morale': 1},
            # Break the line
            10: {'Bolter': 1, 'Shield': 2, 'Morale': 0},
            # Armoured advance
            11: {'Bolter': 2, 'Shield': 1, 'Morale': 0},
            # Emperor's glory
            12: {'Bolter': 0, 'Shield': 2, 'Morale': 2},
            # Emperor's might
            13: {'Bolter': 3, 'Shield': 0, 'Morale': 0}
        },
        1: {
            # Slugga Boyz
            0: {'Bolter': 1, 'Shield': 1, 'Morale': 0},
            # Shoota Boyz
            1: {'Bolter': 2, 'Shield': 0, 'Morale': 0},
            # 'Ard Boyz
            2: {'Bolter': 0, 'Shield': 2, 'Morale': 0},
            # Gretchin
            3: {'Bolter': 0, 'Shield': 0, 'Morale': 0},
            # Mek Boyz
            4: {'Bolter': 0, 'Shield': 0, 'Morale': 1},
            # Biker Nobz
            5: {'Bolter': 2, 'Shield': 1, 'Morale': 0},
            # Sea of green
            6: {'Bolter': 1, 'Shield': 1, 'Morale': 0},
            # Waaagh!!!!
            7: {'Bolter': 0, 'Shield': 0, 'Morale': 3},
            # Mega Nobz
            8: {'Bolter': 1, 'Shield': 2, 'Morale': 0},
            # Rokkit wagon
            9: {'Bolter': 3, 'Shield': 0, 'Morale': 0},
            # Weirdboyz
            10: {'Bolter': 1, 'Shield': 1, 'Morale': 1},
            # Party wagon
            11: {'Bolter': 1, 'Shield': 2, 'Morale': 0},
            # Snapper Gargant
            12: {'Bolter': 4, 'Shield': 1, 'Morale': 0},
            # Smasher Gargant
            13: {'Bolter': 2, 'Shield': 3, 'Morale': 0}
        }
    }
    return mapping.get(faction, {}).get(cardNumber, {})


def cardAction(gameRound: int, player: Player, enemy: Player, cardNumber: int):
    match player.faction:
        case 0:
            match cardNumber:
                # Reconnaissance
                case 0:
                    enemy.playedCardList.append(enemy.playedCard)
                    enemy.turnedCard = []
                    enemy.recount()
                    if (chooseTokens(gameRound, player, enemy, 2, 2) == 1):
                        player.bolterTokens+=2
                    else:
                        player.shieldTokens+=2
                # Faith in the Emperor
                case 1:
                    player.addRandomDie()
                # Ambush
                case 2:
                    player.bolterTokens += 2
                # Fury of the Ultramar
                case 3:
                    enemy.reRollDie('Shield')
                    enemy.recount()
                    if (chooseReroll(gameRound,player, enemy, 'Shield') == 1):
                        player.reRollDie('Shield')
                # Blessed Power armour
                case 4:
                    player.shieldTokens += 2
                # Hold the line
                case 5:
                    player.shieldTokens += 2
                    #toDo Check who is who in this situation, add rally
                # Glory and death
                case 6:
                    player.bolterTokens += 2
                    #toDo Check who is who in this situation, add rally
                # Veteran scouts
                case 7:
                    for _ in player.dice.count('Morale'):
                        player.recount()
                        if (chooseTokens(gameRound, player, enemy, 1, 1) == 1):
                            player.bolterTokens += 1
                        else:
                            player.shieldTokens += 1
                # Drop Pod assault
                case 8:
                    player.addRandomDie()
                # Show no fear
                case 9:
                    #toDo Add blocking routing in player parameters
                    pass
                # Break the line
                case 10:
                    amount = player.dice.count('Morale')
                    for _ in range(amount):
                        player.recount()()
                        if (chooseSpend(gameRound, player, enemy, 'Morale') == 1):
                            chooseGainDie(player,1,1)
                        else:
                            break
                # Armoured advance
                case 11:
                    player.addRandomDie()
                # Emperor's glory
                case 12:
                    player.addRandomDie(2)
                # Emperor's might
                case 13:
                    player.addRandomDie(2)
        case 1:
            match cardNumber:
                # Slugga Boyz
                case 0:
                    player.reRollDie('Morale', player.dice.count('Morale'))
                    enemy.reRollDie('Morale', enemy.dice.count('Morale'))
                # Shoota Boyz
                case 1:
                    player.reRollDie('Shield', player.dice.count('Shield'))
                # 'Ard Boyz
                case 2:
                    player.reRollDie('Bolter', player.dice.count('Bolter'))
                # Gretchin
                case 3:
                    player.shieldTokens += 1
                    player.bolterTokens += 1
                    chooseEnemyReroll(gameRound,player,enemy)
                # Mek Boyz
                case 4:
                    player.addRandomDie()
                # Biker Nobz
                case 5:
                    enemy.reRollDie('Bolter', enemy.dice.count('Bolter'))
                # Sea of green
                case 6:
                    player.addReinforce()
                # Waaagh!!!!
                case 7:
                    chooseRally(gameRound,player,enemy)
                # Mega Nobz
                case 8:
                    enemy.reRollDie('Shield', enemy.dice.count('Shield'))
                # Rokkit wagon
                case 9:
                    pass
                # Weirdboyz
                case 10:
                    player.reRollAllDie()
                    enemy.reRollAllDie()
                # Party wagon
                case 11:
                    player.addReinforce()
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
            selectedToken = int(input(f"Choose between {bolterTokens} and {shieldTokens}: "))
            if 1 <= selectedToken <= 2:
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
            if 1 <= rerollChoice <= 2:
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
            rerollChoice = int(input("What enemy die reroll: Bolter Shield or Morale?"))
            if 1 <= rerollChoice <= 3:
                break
            else:
                print("Number out of range. Please try again.")
        except ValueError:
            print(f"Invalid input. What enemy die reroll: Bolter Shield or Morale?")
    enemy.reRollDie(dieNumberToName(rerollChoice))

def chooseRally(gameRound:int, player:Player, enemy:Player):
    routedUnitList = [routedUnit for routedUnit in player.unitList if routedUnit.routed == True]
    if len(routedUnitList) > 1:
        routedUnitCommandLevel = list(set(singleUnit.cl for singleUnit in routedUnitList))
        routedUnitString = ", ".join(str(singleUnit) for singleUnit in routedUnitCommandLevel)
        displayInfo(gameRound, player, enemy)
        while True:
            try:
                unitToRally = int(input(f"What unit to rally: {routedUnitString}"))
                if 1 <= unitToRally <= len(routedUnitCommandLevel):
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