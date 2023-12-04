import random
from PlayerClass import Player
from typing import List


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


def cardAction(round: int, player: Player, enemy: Player, cardNumber: int):
    match player.faction:
        case 0:
            match cardNumber:
                # Reconnaissance
                case 0:
                    enemy.playedCardList.append(enemy.playedCard)
                    enemy.turnedCard = []
                    enemy.recount()
                    if (chooseTokens(round, player, enemy, 2, 2) == 1):
                        player.bolterTokens+=2
                    else:
                        player.shieldTokens+=2
                # Faith in the Emperor
                case 1:
                    addRandomDie(player.dice)
                # Ambush
                case 2:
                    player.bolterTokens += 2
                # Fury of the Ultramar
                case 3:
                    reRollDie(enemy.dice, 'Shield')
                    enemy.recount()
                    if (chooseReroll(round,player, enemy, 'Shield') == 1):
                        reRollDie(player.dice, 'Shield')
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
                        if (chooseTokens(round, player, enemy, 1, 1) == 1):
                            player.bolterTokens += 1
                        else:
                            player.shieldTokens += 1
                # Drop Pod assault
                case 8:
                    addRandomDie(player.dice)
                # Show no fear
                case 9:
                    #toDo Add blocking routing in player parameters
                    pass
                # Break the line
                case 10:
                    amount = player.dice.count('Morale')
                    for
                # Armoured advance
                case 11:
                # Emperor's glory
                case 12:
                # Emperor's might
                case 13:
        case 1:
            match cardNumber:
                # Slugga Boyz
                case 0:
                # Shoota Boyz
                case 1:
                # 'Ard Boyz
                case 2:
                # Gretchin
                case 3:
                # Mek Boyz
                case 4:
                # Biker Nobz
                case 5:
                # Sea of green
                case 6:
                # Waaagh!!!!
                case 7:
                # Mega Nobz
                case 8:
                # Rokkit wagon
                case 9:
                # Weirdboyz
                case 10:
                # Party wagon
                case 11:
                # Snapper Gargant
                case 12:
                # Smasher Gargant
                case 13:


def chooseTokens(round, player, enemy, bolterTokens, shieldTokens):
    displayInfo(round, player, enemy)
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

def chooseReroll(round, player, enemy, whatDie):
    displayInfo(round, player, enemy)
    while True:
        try:
            selectedToken = int(input(f"Do you reroll {whatDie} or Not: "))
            if 1 <= selectedToken <= 2:
                break
            else:
                print("Number out of range. Please try again.")
        except ValueError:
            print(f"Invalid input. Do you reroll {whatDie} or Not:  ")
    return selectedToken

def chooseSpend()
    #ToDo